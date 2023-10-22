from os import name as os_name
from subprocess import run
from pyperclip import copy as clip_copy


def copy(text):
    if os_name == "posix":
        try:
            run(f'echo "{text}" | xclip -selection clipboard', shell=True)  # work with term copy in linux
        except:
            clip_copy("text")
    else:
        clip_copy("text")
