
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
# TODO: from fastapi.middleware.cors import CORSMiddleware. Note: Avoid server-side templating or direct frontend-backend dependencies. Only use the api for these interactions so we can migrate frontend to platforms like Vercel for better performance. 

app = FastAPI()

# TODO: Add middleware for CORS if I ever need to access the api from other domains (WhatsApp, Vercel, etc).

# API routes
@app.get("/api/search")
async def search(query: str):
    results = f"You searched for: {query}"
    return {"results": results}

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/{full_path:path}")
async def read_index(full_path: str):
    return FileResponse('static/index.html')


