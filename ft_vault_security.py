# ft_vault_security.py

def secure_archive(filename, action="read", content=""):
    try:
        if action == "read":
            with open(filename, "r") as file:
                data = file.read()
            return (True, data)

        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")

        else:
            return (False, "Unknown action")

    except Exception as error:
        return (False, str(error))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("archive.txt"))

    print("Using 'secure_archive' to write previous content to a new file:")
    old_content = secure_archive("archive.txt")[1]
    print(secure_archive("new_archive.txt", "write", old_content))
