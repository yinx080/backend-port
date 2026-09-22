from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, timezone

# --- PORTFOLIO PROJECT MODEL ---
# This dictates how your camera and videography work is structured
class ProjectModel(BaseModel):
    title: str = Field(..., example="Coastal Highway Car Edit")
    description: str
    media_type: str = Field(..., example="video") # e.g., 'video', 'photo_gallery'
    media_url: str = Field(..., description="Link to the CDN or embedded video player")
    thumbnail_url: Optional[str] = None
    category: str = Field(..., example="automotive_videography")

# --- CLIENT INQUIRY MODEL ---
# This dictates what data the React contact form needs to send
class InquiryModel(BaseModel):
    client_name: str
    client_email: str 
    project_type: str = Field(..., example="Music Video")
    budget_range: Optional[str] = Field(None, example="1000-2000")
    message: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# --- THE ONE THE FORM ACTUALLY POSTS ---
# This is what POST /api/inquiries accepts. Lengths are capped so nobody can
# post a novel; anything longer is rejected before it reaches your inbox.
class InquiryRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    email: str = Field(..., min_length=3, max_length=200)
    package: Optional[str] = Field(None, max_length=120)
    budget: Optional[str] = Field(None, max_length=60)
    event_date: Optional[str] = Field(None, max_length=40)
    message: str = Field(..., min_length=1, max_length=5000)

    # Spam trap. It is hidden on the page, so a human always leaves it empty
    # and most bots fill it in. Filled in = silently dropped.
    website: Optional[str] = Field(None, max_length=200)