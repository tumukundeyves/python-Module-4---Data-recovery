import sys

from typing import IO

if len(sys.argv) != 2:
    print("Usage: python ex0/ft_ancient_text.py <file_path>")
    sys.exit(1)

filename = sys.argv[1]

print("=== Cyber Archives Recovery ===")
print(f"Accessing file '{filename}'")

try:
    file: IO = open(filename, 'r')
    print("---")
    print(file.read(), end="")
    print("\n---")
    file.close()
    print(f"file '{filename}' closed")
except OSError as err:
    print(f"Error openig file '{filename}' : {err}")
