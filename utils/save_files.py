from pathlib import Path

def save_file(file, data):
    path = Path(__name__).resolve().parent.parent / "data"
    filename = path / f"/{file}"
    if not path.exists():
        print("Folder not found!")
        path.mkdir(parents=True, exist_ok=True)
    else:
        print("Data folder found!")
        if filename.exists():
            print("File Found!")
            with open(filename, 'a') as file:
                file.write(data)
        else:
            print("File not found!")
            with open(filename, 'w') as file:
                file.write(data)


