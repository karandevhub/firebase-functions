from firebase_functions import https_fn
from firebase_admin import initialize_app, _apps
from app.controllers.controller import handle_scrape

if not _apps:
    app = initialize_app()
else:
    app = _apps[0]

on_call_param = {"region": "asia-south1"}


@https_fn.on_call(**on_call_param)
def scrape(req: https_fn.CallableRequest) -> dict:
    try:
        data = req.data
        url = data.get("url")
        
        if not url:
            return {"status": "error", "message": "URL is required"}

        result = handle_scrape({"url": url})
        return result

    except Exception as e:
        print(f"Error in scrape function: {e}")
        return {"status": "error", "message": "An internal error occurred"}
