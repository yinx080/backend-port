import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",
        "https://portfolio-frontend-production-ae40.up.railway.app",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Back to the clean, simple media route
@app.get("/media/{filename}")
def stream_video(filename: str):
    file_path = os.path.join("uploads", filename)
    return FileResponse(file_path, media_type="video/mp4")

@app.get("/api/projects")
def get_projects():
    return [
        {
            "id": 2,
            "title": "Narnya",
            "category": "Nightlife / Videography",
            # Notice the ?v=1 at the end!
            "video_url": "http://127.0.0.1:8000/media/narnya2.mp4?v=1"
        },
        {
            "id": 1,
            "title": "Narnya 2",
            "category": "Nightlife / Videography",
            # Notice the ?v=1 at the end!
            "video_url": "http://127.0.0.1:8000/media/test-edit.mp4?v=1"
        },
        {
            "id": 3,
            "title": "Narnya 3",
            "category": "Nightlife / Videography",
            # Notice the ?v=1 at the end!
            "video_url": "http://127.0.0.1:8000/media/narnya3.mp4?v=1"
        },
        {
            "id": 4,
            "title": "Pangea",
            "category": "Nightlife / Videography",
            # Notice the ?v=2 at the end!
            "video_url": "http://127.0.0.1:8000/media/pangea5.mp4?v=2"
        },
        {
            "id": 5,
            "title": "Pangea 2",
            "category": "Nightlife / Videography",
            # Notice the ?v=2 at the end!
            "video_url": "http://127.0.0.1:8000/media/pangea2.mp4?v=2"
        },
        {
            "id": 6,
            "title": "Pangea 3",
            "category": "Nightlife / Videography",
            # Notice the ?v=2 at the end!
            "video_url": "http://127.0.0.1:8000/media/pangea3.mp4?v=2"
        },
        {
            "id": 7,
            "title": "Pangea 4",
            "category": "Nightlife / Videography",
            # Notice the ?v=2 at the end!
            "video_url": "http://127.0.0.1:8000/media/pangea4.mp4?v=2"
        },
        {
            "id": 8,
            "title": "Pangea 5",
            "category": "Nightlife / Videography",
            # Notice the ?v=2 at the end!
            "video_url": "http://127.0.0.1:8000/media/16_2.mp4?v=2"
        },
        {
            "id": 9,
            "title": "Rumours Tibu",
            "category": "Nightlife / Videography",
            # Notice the ?v=2 at the end!
            "video_url": "http://127.0.0.1:8000/media/rumourstibu1.mp4?v=2"
        },
        {
            "id": 10,
            "title": "Rumours Tibu 2",
            "category": "Nightlife / Videography",
            # Notice the ?v=2 at the end!
            "video_url": "http://127.0.0.1:8000/media/rumourstibu2.mp4?v=2"
        },
    ]