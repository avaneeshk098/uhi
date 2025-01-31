import random
import uuid

from .models import User


def gen_unique_id(email: str, password: str) -> User:
    """
    Generates a New unique id and creates a new User Object with the username set to the unique id
    """
    _len = 16
    digits = "0123456789"
    code = "".join([random.choice(digits) for _ in range(_len)])
    while User.objects.filter(username=code):  # what does this return?
        code = "".join([random.choice(digits) for _ in range(_len)])

    user = User.objects.create_user(username=code,
                                    password=password,
                                    email=email)
    user.save()
    return user


def get_hcw_vid(email: str, password: str, division: str):
    """
    Generates a New unique id and creates a new User Object with the username set to the unique id
    """
    hcw_vid = uuid.uuid4()
    hcw_vid = str(hcw_vid)[:11]
    while User.objects.filter(username=hcw_vid):
        hcw_vid = uuid.uuid4()
        hcw_vid = str(hcw_vid)[:11]
    user = User.objects.create_user(username=hcw_vid,
                                    password=password,
                                    email=email,
                                    division=division)
    user.save()
    return user


def is_valid_file(file: str) -> bool:
    """
    checks if a file is valid, if not, it will return False
    """
    approved = ["docx", "pdf", "jpg", "jpeg", "png", "pptx", "ppt", "xlsx", "xls", "txt", "mp4", "avi", "mov", "mp3",
                "key"]
    file = str(file)

    if "." not in file:  # checks if it has an extension
        return False

    f_ext = file[file.rfind(".")+1:]
    if f_ext not in approved:  # checks if it has a valid extension
        return False

    return True


def filter_files(files: list, mode: str) -> list:
    """
    filters the file for myfiles view
    """
    if mode == "def":
        return files
    return [f for f in files if f.file_type == mode]


def sort_files(files: list, mode: str) -> list:
    """
    sorts the files for the myfiles view
    """
    if mode == "def":
        return files

    elif mode == "ft":

        exts = {f.file_type: [] for f in files}
        for file in files:
            exts[file.file_type].append(file)
        nfs = []
        for v in exts.values():
            nfs.extend(v)
        return nfs

    elif mode == "az":
        fs = [f for f in files]
        return sorted(fs, key=lambda x: str(x))


if __name__ == "__main__":
    print(str(uuid.uuid4())[:12])
