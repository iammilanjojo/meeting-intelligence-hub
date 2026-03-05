from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pypdf import PdfReader
import re

app = FastAPI(title="Meeting Intelligence Hub")

# -------------------------------
# CORS (Fix for browser requests)
# -------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# MODELS
# -------------------------------

class TranscriptInput(BaseModel):
    transcript: str

class QuestionInput(BaseModel):
    transcript: str
    question: str

# -------------------------------
# ROOT
# -------------------------------

@app.get("/")
def root():
    return {"message": "Meeting Intelligence Hub backend running 🚀"}

# -------------------------------
# UPLOAD TRANSCRIPT
# -------------------------------

@app.post("/upload-transcript")
async def upload_transcript(file: UploadFile = File(...)):

    transcript = ""

    try:

        # TXT FILE
        if file.filename.endswith(".txt"):

            content = await file.read()
            transcript = content.decode("utf-8", errors="ignore")

        # PDF FILE
        elif file.filename.endswith(".pdf"):

            reader = PdfReader(file.file)

            for page in reader.pages:
                text = page.extract_text()
                if text:
                    transcript += text + " "

        else:
            raise HTTPException(
                status_code=400,
                detail="Only .txt or .pdf files allowed"
            )

        return {"transcript": transcript}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -------------------------------
# ANALYZE MEETING
# -------------------------------

@app.post("/analyze-meeting")
def analyze_meeting(data: TranscriptInput):

    transcript = data.transcript.strip()

    if transcript == "":
        raise HTTPException(status_code=400, detail="Transcript is empty")

    # SUMMARY
    sentences = re.split(r'[.!?]', transcript)
    summary = ". ".join(sentences[:3]).strip()

    # ACTION ITEMS
    action_items = []

    patterns = [
        r"\bwill\b.*",
        r"\bneed to\b.*",
        r"\bmust\b.*",
        r"\bshould\b.*"
    ]

    for sentence in sentences:

        for pattern in patterns:

            if re.search(pattern, sentence, re.IGNORECASE):

                clean = sentence.strip()

                if clean != "":
                    action_items.append(clean)

                break

    # TOPIC DETECTION
    words = re.findall(r'\b[a-zA-Z]{4,}\b', transcript.lower())

    topic_count = {}

    for word in words:
        topic_count[word] = topic_count.get(word, 0) + 1

    sorted_topics = sorted(
        topic_count.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    topics = [t[0] for t in sorted_topics]
    counts = [t[1] for t in sorted_topics]

    return {
        "summary": summary,
        "action_items": action_items,
        "topics": topics,
        "counts": counts
    }

# -------------------------------
# ASK QUESTIONS
# -------------------------------

@app.post("/ask")
def ask_question(data: QuestionInput):

    transcript = data.transcript.lower()
    question = data.question.lower()

    sentences = re.split(r'[.!?]', transcript)

    results = []

    for sentence in sentences:

        if any(word in sentence for word in question.split()):

            clean = sentence.strip()

            if clean != "":
                results.append(clean)

    if len(results) == 0:

        return {"answer": "No relevant information found in the meeting."}

    return {"answer": ". ".join(results[:3])}