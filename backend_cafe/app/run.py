import logging
import uvicorn
from core.configs import settings


if __name__ == "__main__":
    try:
        logging.info("Starting FastAPI")
        uvicorn.run("main:main_app", host=settings.run.host, port=settings.run.port, reload=True)
    except Exception as error:
        print(error)