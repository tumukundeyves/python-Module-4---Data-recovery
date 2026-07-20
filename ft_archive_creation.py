import sys
import typing

print("=== Cyber Archives Recovery & Preservation ===")

if len(sys.argv) != 2:
    print("Usage: python3 ft_archive_creation.py <file>")
    sys.exit(1)

filename: str = sys.argv[1]

try:
    print(f"Accessing file '{filename}'")

    file: typing.IO = open(filename, "r")
    content: str = file.read()

    print("---")
    print(content, end="")
    print("\n---")

    file.close()
    print(f"File '{filename}' closed.")

    print("Transform data:")
    print("---")

    new_content: str = ""
    current_line: str = ""

    for char in content:
        if char == "\n":
            new_content += current_line + "#\n"
            current_line = ""
        else:
            current_line += char

    if current_line != "":
        new_content += current_line + "#"

    print(new_content, end="")
    print("\n---")

    new_filename: str = input("Enter new file name (or empty): ")

    if new_filename == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_filename}'")

        new_file: typing.IO = open(new_filename, "w")
        new_file.write(new_content)
        new_file.close()

        print(f"Data saved in file '{new_filename}'.")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except PermissionError:
    print(f"Error: Permission denied for '{filename}'.")
except OSError:
    print("Error while accessing the file.")
