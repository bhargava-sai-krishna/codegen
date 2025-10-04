import os
from daytona import FileUpload

def parseFiles(base_dir="generated_app", dest_root="workspace/application"):
    """
    Recursively finds all files inside base_dir and returns them as FileUpload objects
    with their contents read in binary mode, ready for upload.
    
    - `dest_root` is the root folder inside the sandbox where files will be uploaded.
    """
    file_uploads = []

    for root, _, files in os.walk(base_dir):
        for filename in files:
            local_path = os.path.join(root, filename)
            
            # Read the file in binary mode
            with open(local_path, "rb") as f:
                content = f.read()
            
            # Compute relative path for destination
            rel_path = os.path.relpath(local_path, base_dir)
            dest_path = os.path.join(dest_root, rel_path).replace("\\", "/")  # use / for sandbox
            
            file_uploads.append(FileUpload(source=content, destination=dest_path))

    return file_uploads
