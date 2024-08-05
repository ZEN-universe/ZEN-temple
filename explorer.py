import uvicorn
import webbrowser

config = uvicorn.Config("src.main:app", port=8000, log_level="info")
server = uvicorn.Server(config)
webbrowser.open('http://localhost:8000/explorer', new=2)

server.run()

