from pydantic import BaseModel
from urllib.parse import urlencode, quote
import urllib.request
from .paths import PENDANT_CONFIG
import dbm
import sys
from typing import Any
from datetime import datetime
import re
import shutil
from rich.prompt import Confirm
from pathlib import Path

def ack(k, v):
    resp = Confirm.ask(f"Confirm {k} => {v}?")
    return resp


def must_exist(path):
    exists = Path(path).exists()
    if not exists:
        print(f"path {path} doesn't exist. Try again...")
    return exists


def write_file(path, text=""):
    with open(path, "w") as f:
        f.write(text)


def read_file(path):
    with open(path, "r") as f:
        text = f.read()
    return text


def update_file(path, func):
    text = read_file(path)
    new_text = func(text)
    write_file(path, text=new_text)


def move_file(src, dest):
    shutil.move_file(src, dest)



# v = Vault()
# v.write_file("test_note.md", "blabhalbhalhbalhlbhablahblhabhalbha")
