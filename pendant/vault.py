from .paths import VAULT_PATH
from pathlib import Path
import re
from pydantic import BaseModel
from .note import Note


class Vault:
    path: str = VAULT_PATH

    @property
    def notes(self):
        return list(map(lambda n: Note(path=str(n)), Path(self.path).rglob('*.md')))




