from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://portfolio-frontend-production-ae40.up.railway.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent

# Bump this whenever you replace a video/thumbnail/poster WITHOUT renaming it.
# It changes every ?v= in the API responses, so browsers fetch the new files
# instead of serving the cached ones.
VERSION = 3


class CachedStatic(StaticFiles):
    """StaticFiles + long-lived cache headers (files are versioned via ?v=)."""

    async def get_response(self, path, scope):
        response = await super().get_response(path, scope)
        if response.status_code in (200, 206, 304):
            response.headers["Cache-Control"] = "public, max-age=31536000, immutable"
        return response


# Serves everything inside uploads/, including uploads/compressed/.
# Handles Range requests (video seeking, Safari) and fails at startup if
# the folder is missing, so you'll see it in the Railway deploy logs.
app.mount("/media", CachedStatic(directory=BASE_DIR / "uploads"), name="media")


def project(id: int, title: str, filename: str, category: str = "Nightlife / Videography"):
    name = Path(filename).stem
    return {
        "id": id,
        "title": title,
        "category": category,
        "video_url": f"/media/{filename}?v={VERSION}",
        "thumb_url": f"/media/compressed/{name}_thumb.mp4?v={VERSION}",
        "poster_url": f"/media/compressed/{name}_poster.jpg?v={VERSION}",
    }


PROJECTS = [
    project(2, "Narnya", "narnya2.mp4"),
    project(1, "Narnya 2", "test-edit.mp4"),
    project(3, "Narnya 3", "narnya3.mp4"),
    project(4, "Pangea", "pangea5.mp4"),
    project(5, "Pangea 2", "pangea2.mp4"),
    project(6, "Pangea 3", "pangea3.mp4"),
    project(7, "Pangea 4", "pangea4.mp4"),
    project(8, "Pangea 5", "16_2.mp4"),
    project(9, "Rumours Tibu", "rumourstibu1.mp4"),
    project(10, "Rumours Tibu 2", "rumourstibu2.mp4"),
]


@app.get("/api/projects")
def get_projects():
    return PROJECTS