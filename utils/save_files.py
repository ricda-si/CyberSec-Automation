from pathlib import Path

def save_file(file, data, type):
    path = Path(__name__).resolve().parent / f"data/{type}"
    filename = path / file
    print(path)
    print(filename)
    print(data)
    print(file)

    with open(filename, 'w') as f:
        f.write(data)
