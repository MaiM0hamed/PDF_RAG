from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from helpers.config import get_settings, settings
from controllers import DataController


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["/api_v1", "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str,
    file: UploadFile = File(...),
    app_settings: settings = Depends(get_settings)
):
    is_valid = await DataController().validate_uploaded_file(file=file)

    if not is_valid:
        raise HTTPException(status_code=400, detail="Invalid file type or size")

    return {
        "signal": "ok",
        "file_valid": True,
        "filename": file.filename,
        "file_type": file.content_type
    }