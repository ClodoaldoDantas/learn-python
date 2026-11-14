import os


def read_text_file(filename):
    folder = os.path.dirname(__file__)
    path = os.path.join(folder, filename)

    with open(path, "r", encoding="utf-8") as text_file:
        result = text_file.read()
        return result


content = read_text_file("message.txt")
print(content)
