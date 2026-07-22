# ft_vault_security.py

def secure_archive(
    filename: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:

    try:
        if action == "read":
            with open(filename, "r") as file:
                return (True, file.read())

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

    with open("archive.txt", "w") as file:
        file.write(
            "[FRAGMENT 001] Digital preservation protocols established 2087\n"
            "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
            "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
        )

    archive_content: tuple[bool, str] = secure_archive("archive.txt")
    print(archive_content)

    print("Using 'secure_archive' to write previous content to a new file:")

    content_to_write: str = archive_content[1]

    print(
        secure_archive(
            "new_archive.txt",
            "write",
            content_to_write
        )
    )
