from daytona import Daytona

daytona = Daytona()
sandbox=daytona.get("fd56b0c9-18a4-4dc4-8aec-6b2692a9a6f9")

preview_info = sandbox.get_preview_link(8000)

print(f"Preview link url: {preview_info.url}")
print(f"Preview link token: {preview_info.token}")