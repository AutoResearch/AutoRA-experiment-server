from pathlib import Path

import logger
import json
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse, RedirectResponse

app = FastAPI()

log = logger.config(True)

app.mount("/experiment", StaticFiles(directory="dist"), name="frontend")


@app.get("/")
def default() -> RedirectResponse:
    """
    Make sure to redirect bare IP/url to form landing page
    """
    return RedirectResponse(url="/experiment")


@app.get("/experiment")
def serve_frontend() -> FileResponse:
    """
    Serves static UI
    """
    project_path = Path(__file__).parent.resolve()
    response = FileResponse(
        str(project_path / "dist/index.html"), media_type="text/html"
    )
    return response


@app.post("/data")
async def receive_data(request: Request):
    """Receive trial results and write to autora_out.json

    Args:
        request (Request): incoming array of [id, trial_result]

    Returns:
        data: trial result
    """
    project_parent_path = Path(__file__).parent.resolve()
    input = await request.json()

    id, data = input[0], input[1]

    # TODO: ensure file path exists
    # TODO: change to append
    with open(
        project_parent_path / "../experiment/autora_out/autora_out.json", "w"
    ) as f:
        json.dump({id: data}, f)

    return data
