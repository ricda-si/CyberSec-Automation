from pathlib import Path

def save_file(file, data, type):
    path = Path(__name__).resolve().parent / f"data/{type}"
    filename = path / file

    with open(filename, 'w') as f:
        f.write(data)
