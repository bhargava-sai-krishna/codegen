import os
from daytona import Daytona, SessionExecuteRequest, DaytonaConfig
from .fileParser import parseFiles
from dotenv import load_dotenv

load_dotenv()

daytona = Daytona(DaytonaConfig(api_key=os.getenv("DAYTONA_API_KEY")))

sandbox = daytona.get(os.getenv("SANDBOX"))

exec_session_id = "python-app-session"
sandbox.process.create_session(exec_session_id)


def deploy():
    files=parseFiles() 

    sandbox.fs.create_folder("workspace/application", "755")

    sandbox.fs.upload_files(files)

    sandbox.process.execute_session_command(exec_session_id, SessionExecuteRequest(
        command="sudo kill -9 $(lsof -t -i:5000)",
        var_async=True
    ))

    sandbox.process.execute_session_command(exec_session_id, SessionExecuteRequest(
        command="pip install -r requirements.txt",
        var_async=True
    ))

    sandbox.process.execute_session_command(exec_session_id, SessionExecuteRequest(
        command="python workspace/application/app.py",
        var_async=True
    ))

    preview_info = sandbox.get_preview_link(5000)
    print(f"Flask app is available at: {preview_info.url}")
    return preview_info.url
