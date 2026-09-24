import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from gemini_utils import get_home_recommendations

app = FastAPI()

# Setup Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    # 'request' MUST be passed as the first argument
    return templates.TemplateResponse(request, "index.html", context={"result": None})

@app.post("/home-budget", response_class=HTMLResponse)
def plan_home_budget(request: Request, budget: int = Form(...), room_type: str = Form(...)):
    try:
        recommendation = get_home_recommendations(budget, room_type)
    except Exception as e:
        recommendation = f"Error generating plan: {str(e)}"
    
    return templates.TemplateResponse(request, "index.html", context={"result": recommendation})