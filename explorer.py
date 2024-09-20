import uvicorn
import webbrowser
from zen_temple.config import config
import sys


if __name__ == "__main__":
    uvicorn_config = uvicorn.Config("zen_temple.main:app", port=8000, log_level="info")
    server = uvicorn.Server(uvicorn_config)
    webbrowser.open('http://localhost:8000/explorer', new=2)

    if len(sys.argv) > 1:
        config.SOLUTION_FOLDER = sys.argv[1]
    
    server.run()

