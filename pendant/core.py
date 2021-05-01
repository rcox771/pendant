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


def ack(k, v):
    options = ["y", "n", "c"]

    while True:
        resp = input(f"Confirm, {k} => {v} (options: [y/n/c])?: ")
        if resp not in options:
            print(f" sorry, {key} must be one of {options}. Please try again...")
        else:
            break

    if resp == "y":
        return True
    if resp == "n":
        return False
    if resp == "c":
        print("cancelled.")
        sys.exit(0)
    return


def must_exist(path):
    exists = Path(path).exists()
    if not exists:
        print(f"path {path} doesn't exist. Try again...")
    return exists


def gather_configurable(key, options=[]):
    # todo: make a list of conditional callbacks
    value = None
    s = f"Enter value for {key}: "
    if options:
        s = s.replace(f"{key}: ", f"{key} (options: {options}): ")
    v = None
    while True:
        v = input(s)
        if options:
            if v not in options:
                print(f" sorry, {key} must be one of {options}. Please try again...")

        if ack(key, v) == True:
            break

    return v


class PendantConfig(BaseModel):
    path: str = PENDANT_CONFIG

    def get(self, key) -> Any:
        with dbm.open(self.path, "c") as db:
            value = db.get(key)
        if value == None:
            value = gather_configurable(key)
            self.set(key, value)
        return value

    def set(self, key, value):
        with dbm.open(self.path, "c") as db:
            db[key] = value
        print(f"set {key} => {value}")
        return True

    def update(self, **kwargs):
        with dbm.open(self.path, "c") as db:
            for k, v in kwargs.items():
                db[k] = v
                print(f"set {k} => {v}")
        return data


class Vault(BaseModel):
    path: str = PendantConfig().get("vault")


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
# v.open("test_note.md", "blabhalbhalhbalhlbhablahblhabhalbha")
