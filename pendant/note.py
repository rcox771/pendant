from pydantic import BaseModel
from pathlib import Path

class Note(BaseModel):
    path: str

    @property
    def contents(self):
        with open(self.path, 'r') as f:
            txt = f.read()
        return txt

    @contents.setter
    def contents(self, txt):
        print('setting contents')
        with open(self.path, 'w') as f:
            f.write(txt)

    @property
    def name(self):
        return Path(self.path).name.rstrip('.md').rstrip('.MD')

