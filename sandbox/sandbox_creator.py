from daytona import Daytona, CreateSandboxFromSnapshotParams

daytona = Daytona()

# Create a basic Sandbox

sandbox = daytona.create()

# Create a Sandbox with specific language

params = CreateSandboxFromSnapshotParams(language="python")
sandbox = daytona.create(params)

# Create a Sandbox with custom labels

params = CreateSandboxFromSnapshotParams(labels={"something": "intro"})
sandbox = daytona.create(params)