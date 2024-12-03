from pathlib import Path

def read_a_file(filePath):
    path = Path(filePath)
    lines = []
    with open(path, "r") as file:
        lines = file.readlines()
    return lines