from pathlib import Path

def save_file(file, data):
    path = Path(__name__).resolve().parent.parent / "data"
    filename = path / f"/{file}"
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    else:
        if filename.exists():
            with open(filename, 'a') as file:
                file.write(data)
        else:
            with open(filename, 'w') as file:
                file.write(data)
                print("File Saved!!")



