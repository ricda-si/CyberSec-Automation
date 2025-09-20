from pathlib import Path

def save_file(file, data):
    path = Path(__name__).resolve().parent / "data"
    filename = path / f"{file}"
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    else:
        if filename.exists():
            print("dont exist")
            with open(filename, 'a') as file:
                file.write(data)
        else:
            print("exist")
            with open(filename, 'w') as file:
                file.write(data)
