from pathlib import Path

ROOT_DIR = Path(__file__).parent
example = ROOT_DIR / 'example.txt'

with open(example) as example:
    contents = example.read()
    print(contents)




