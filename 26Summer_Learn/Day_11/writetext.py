from pathlib import Path

path1 = Path("program1.txt")
path1.write_text("i love programming")

contents2 = "zxcfvbnm,./\n"
contents2 += "asdfghjkl;'"
print(contents2)
path2 = Path("program2.txt")
path2.write_text(contents2)