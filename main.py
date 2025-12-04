from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from models import WaitlistUser
from database import waitlist_collection

app = FastAPI()

# Template folder
templates = Jinja2Templates(directory="templates")


# --------------------- HOME PAGE ---------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("claude.html", {"request": request})


# --------------------- FORM SUBMISSION ---------------------
@app.post("/join-waitlist", response_class=HTMLResponse)
async def join_waitlist(
    request: Request,
    name: str = Form(None),
    email: str = Form(...),
    role: str = Form(...),
    area: str = Form(None)
):
    # Create a Pydantic model instance
    user = WaitlistUser(
        name=name,
        email=email,
        role=role,
        area=area
    )

    # Insert into MongoDB
    waitlist_collection.insert_one(user.model_dump())

    # Render thank you page
    return templates.TemplateResponse(
        "thank_you.html",
        {"request": request, "name": name}
    )
