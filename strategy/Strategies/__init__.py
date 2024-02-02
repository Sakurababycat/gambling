from pathlib import Path

folder = Path(__file__).resolve().parent
prefix = folder.relative_to(folder.parents[1]).as_posix().replace("/", ".")
py_files = folder.glob("*Strategy.py")
for py_file in py_files:
    module_name = prefix + "." + py_file.stem
    __import__(module_name)
