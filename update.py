from os import listdir

directory = "gigachads"
files = [f'"{i}"' for i in listdir(directory)]

filenames = ",\n    ".join(files)
gigalist = f"""$a
  "gigachads": [
    {filenames}
  ]
$b""".replace("$a", "{").replace("$b", "}")

with open("gigalist.json", "w") as f:
    f.write(gigalist)
