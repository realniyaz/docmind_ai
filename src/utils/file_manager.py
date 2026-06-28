import os

UPLOAD_FOLDER = "data/pdfs"


def ensure_upload_dir():

    os.makedirs(
        UPLOAD_FOLDER,
        exist_ok=True
    )


def save_pdf(uploaded_file):

    ensure_upload_dir()

    filepath = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(filepath, "wb") as f:

        f.write(uploaded_file.getbuffer())

    return filepath


def delete_pdf(filename):

    path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    if os.path.exists(path):

        os.remove(path)

        return True

    return False