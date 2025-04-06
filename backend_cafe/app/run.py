import os
from pathlib import Path
import logging
import uvicorn
from backend_cafe.app.core.configs import settings


BASE_DIR = Path(__file__).resolve().parent.parent
contents = os.listdir(BASE_DIR)

if __name__ == "__main__":
    try:
        logging.info("Starting FastAPI")
        logging.info(f"Folder contents %s: %s", BASE_DIR, contents)
        uvicorn.run("main:main_app", host=settings.run.host, port=settings.run.port, reload=True)
    except Exception as error:
        print(error)