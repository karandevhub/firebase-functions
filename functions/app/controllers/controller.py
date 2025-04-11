from app.services.scrap_service import scrape_webpage


def handle_scrape(data: dict) -> dict:
    try:
        url = data.get("url")
        if not url:
            return {"status": "error", "message": "URL is required"}
        
        result = scrape_webpage(url)
        return result
        
    except Exception as e:
        print(f"Error in handle_scrape function: {e}")
        return {"status": "error", "message": "An internal error occurred"}


def add_feedback(feedback_data):
    return "Feedback added successfully"

def get_project_info(project_id):
    return {"projectId": project_id, "info": "Sample project info"}
