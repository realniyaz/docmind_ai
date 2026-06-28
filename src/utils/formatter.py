from pathlib import Path


def filename(path):

    return Path(path).name


def filesize(size):

    kb = size / 1024

    if kb < 1024:

        return f"{kb:.1f} KB"

    mb = kb / 1024

    return f"{mb:.2f} MB"


def page(page):

    return f"Page {page+1}"