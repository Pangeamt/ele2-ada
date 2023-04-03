def get_filename(path):
    filename = path.split("/")[-1].split(".")[0]
    return filename


if __name__ == "__main__":
    full_path = "/this/is/a/path/example.txt"
    filename = get_filename(full_path)
    print(filename)
