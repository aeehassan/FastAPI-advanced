from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Creating our templating object
templates = Jinja2Templates(directory="templates")


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "name": "Abubakar"}
    )


@app.get("/home", response_class=HTMLResponse)
def home():
    return """
        <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta ipsa
            dolorem voluptatibus sequi! Recusandae modi ut totam ea, dolore
            voluptatibus porro natus quisquam sit dolor quos facere accusantium, sunt
            veritatis.
        </p>
        """


@app.get("/portal", response_class=HTMLResponse)
def portal(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="portal.html",
        context={"student_name": "Abubakar", "student_id": "U22CS1060"},
    )


# AI prompt box
@app.get("/generate", response_class=HTMLResponse)
def render_ui(request: Request):
    return templates.TemplateResponse(request=request, name="prompt.html")


@app.post("/generate", response_class=HTMLResponse)
def generate(request: Request, user_prompt: str = Form(...)):
    return templates.TemplateResponse(
        request=request, name="prompt.html", context={"response": user_prompt}
    )
