from pathlib import Path


HOME = str(Path().home())
PENDANT_PATH = str(Path(HOME) / ".pendant")
PENDANT_CONFIG = str(Path(PENDANT_PATH) / "config.db")

Path(PENDANT_CONFIG).mkdir(parents=True, exist_ok=True)

VAULT_PATH = f"{HOME}/vault"
