def analyze_transcript(text: str):
    
    lines = text.split("\n")
    
    action_items = []
    
    for line in lines:
        if "will" in line.lower() or "action" in line.lower():
            action_items.append(line)

    summary = "This meeting discussed important tasks and responsibilities."

    return {
        "summary": summary,
        "action_items": action_items
    }