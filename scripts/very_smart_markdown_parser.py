def get_title(text: str) -> str:
    for line in text.split("\n"):
        if line.startswith("# "):
            return line[2:]
    return ""


def replace_title(text: str, new_title: str) -> str:
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("# "):
            lines[i] = f"# {new_title}"
            break
    return "\n".join(lines)


def get_description(text: str) -> str:
    description_line = False
    for line in text.split("\n"):
        if line == "":
            continue

        if description_line:
            return line

        if line.startswith("# "):
            description_line = True

    return ""


def replace_description(text: str, new_description: str) -> str:
    lines = text.split("\n")
    description_line = False
    for i, line in enumerate(lines):
        if line == "":
            continue

        if description_line:
            lines[i] = new_description
            break

        if line.startswith("# "):
            description_line = True

    return "\n".join(lines)
