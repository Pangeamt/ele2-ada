def get_extension(path):
    extension = path.split(".")[-1]
    return extension


if __name__ == "__main__":
    full_path = "/this/is/a/path/example.txt"
    extension = get_extension(full_path)
    print(extension)
