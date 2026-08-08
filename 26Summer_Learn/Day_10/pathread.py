from pathlib import Path

path = Path('pi.txt')
content = path.read_text().rstrip()
print(content)

path1 = Path('../Day_09/pi.txt')
contents = path1.read_text().rstrip()
print(contents)

#splitlines
lines = content.splitlines()
print(lines)
print(type(lines))
print(len(lines))
for line in lines:
    line = line.lstrip()
    line = line.replace('3', '5')
    print(line)