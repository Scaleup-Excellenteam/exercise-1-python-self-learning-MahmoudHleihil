import os

def list_deep_files(directory: str):
    """
    Returns a list of all files in the given directory that start with "deep"
    """
    return [file for file in os.listdir(directory) if file.startswith("deep") and os.path.isfile(os.path.join(directory, file))]


if __name__ == '__main__':
    # Example usage
    print(list_deep_files("./images"))
