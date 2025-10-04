import os
import re

CHECKPOINT_DIR = "checkpoints"

def _get_chat_file(chat_id: str) -> str:
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)
    return os.path.join(CHECKPOINT_DIR, f"{chat_id}.txt")

def save_version(chat_id: str, code: str) -> int:
    """
    Save a new version of code to chat's file.
    Versions are appended as markdown style blocks.
    Returns the new version number.
    """
    file = _get_chat_file(chat_id)
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        existing = content.count("### Version ")
    else:
        existing = 0

    version = existing + 1
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"\n### Version {version}\n{code}\n")
    return version

def get_version(chat_id: str, version: int) -> str:
    """
    Fetch a specific version block (1-based indexing).
    """
    file = _get_chat_file(chat_id)
    if not os.path.exists(file):
        return None

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    parts = content.split("### Version ")
    if version <= 0 or version >= len(parts):
        return None

    return parts[version].strip()

def get_latest_version(chat_id: str) -> str:
    """
    Fetch the latest version of code for a chat.
    """
    file = _get_chat_file(chat_id)
    if not os.path.exists(file):
        return None

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    parts = content.split("### Version ")
    if len(parts) <= 1:
        return None

    return parts[-1].strip()

def save_generated_files(output: str, base_dir="."):
    """
    Parses model output with file paths and code blocks, then saves them to disk.
    Example expected format:
        requirements.txt
        ```python
        print("hello")
        ```
    """
    pattern = r'([^\n]+)\n```(?:\w+)?\n([\s\S]*?)```'
    matches = re.findall(pattern, output)

    if not matches:
        print("⚠️ No files detected in model output.")
        return

    for filename, code in matches:
        # Clean filename: remove **, spaces, etc.
        clean_name = filename.strip().strip("*").strip()

        filepath = os.path.join(base_dir, clean_name)

        # Ensure parent directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Write the code into the file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code.strip())

        print(f"✅ Saved {filepath}")
