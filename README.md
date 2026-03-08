*Project Title :
Meeting Intelligence Hub – AI Powered Meeting Analyzer

*The Problem:
Modern teams conduct many meetings on platforms like Zoom, Microsoft Teams, and Google Meet. Important information such as key decisions, action items, and responsibilities are often lost in long meeting transcripts. Manually reading and extracting insights from these transcripts is time-consuming and inefficient.

*The Solution:
Meeting Intelligence Hub is a web application that automatically analyzes meeting transcripts and extracts useful insights. Users can upload a meeting transcript file (.txt or .pdf) or paste the transcript directly into the application.
The system processes the transcript and automatically generates a concise summary, identifies action items, highlights key discussion topics, and allows users to ask specific questions about the meeting. This helps teams quickly understand the outcomes of meetings without reading the entire transcript.

*Tech Stack:
Frontend:
 HTML,
 CSS,
 JavaScript

Backend:
 Python,
 FastAPI

Libraries & Tools:
 PyPDF (for reading PDF transcripts),
 Regex (for extracting action items and topics),
 Uvicorn (ASGI server)

Development Tools:
 Visual Studio Code,
 Git,
 GitHub

 *Setup Instructions:

1. Clone the Repository
git clone https://github.com/iammilanjojo/meeting-intelligence-hub.git
Navigate to the project folder
cd meeting-intelligence-hub

2. Create a Virtual Environment
python -m venv venv
Activate the environment
Windows:
venv\Scripts\activate

3. Install Dependencies
pip install fastapi uvicorn python-multipart pypdf

4. Start the Backend Server
Navigate to the backend folder
cd Backend
Run the FastAPI server
uvicorn main:app --reload
The backend will start at:
http://127.0.0.1:8000

5. Open the Frontend
Navigate to the frontend folder and open the file:
Frontend/index.html
Open it in any browser (Chrome, Edge, etc).

*Project demo:https://drive.google.com/file/d/1JkLEgF-6zfxWr5tQapjEmiUDiO7FhXry/view?usp=drivesdk
