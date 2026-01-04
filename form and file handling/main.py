from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI(title="Form and File handling")


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return {
        "username": username,
        "password": password,
    }


@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    return file
