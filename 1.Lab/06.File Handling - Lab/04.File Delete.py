import os

file_path = "text.txt"

if os.path.exists(file_path):
    os.remove(file_path)

