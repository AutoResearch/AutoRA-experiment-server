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
    input = await request.json()
    id, data = input[0], input[1]
    project_path = Path(__file__).parent.resolve().parent.resolve()
    out_file_location = project_path / "experiment-server" / "autora_out" / "autora_out.json"

    if out_file_location.exists():
        with open(out_file_location, "r") as f:
            existing_data = json.load(f)
            existing_data[id] = data

        with open(out_file_location, "w") as f:
            json.dump(existing_data, f)

    return data
