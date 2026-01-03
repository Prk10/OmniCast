from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from adapters.playwright_renderer import PlaywrightRenderer
from core.content_processor import ContentProcessor



class RenderRequest(BaseModel):
    content: str
    format_type: str

renderer_state = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("OmniCast API starting up...Launching Browser")
    renderer = PlaywrightRenderer()

    await renderer.__aenter__()

    renderer_state["renderer"] = renderer

    yield

    print("Omnicast API shutting down..closing browser")

    await renderer.__aexit__(None, None, None)
    renderer_state.clear()

app = FastAPI(lifespan=lifespan)

@app.post("/render")
async def render_endpoint(request: RenderRequest):
    renderer = renderer_state.get("renderer")

    if not renderer:
        raise HTTPException(status_code=500, detail="Renderer is not active.")
    
    try:
        html_content = ContentProcessor.process(request.content, request.format_type)

        image_bytes = await renderer.screenshot(html_content)

        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    