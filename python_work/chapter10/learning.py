from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

# print(contents)

for line in contents.splitlines():
    line = line.replace("Python", "Java")
    print(line)
