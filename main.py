from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "My First API with FastAPI"
app.version = "v0.0.1"

@app.get("/", tags=["Home", "Root"])
def home():
    return HTMLResponse("""
    <html>
        <head>
            <title>My First API with FastAPI</title>
        </head>
        <body>
            <h1>Welcome to my API</h1>
            <p>Try to go to <a href="/docs">/docs</a></p>
        </body>
    </html>
""")