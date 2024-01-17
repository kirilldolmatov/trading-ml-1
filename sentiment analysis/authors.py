import settings

path = settings.DEFAULT_FILE_PATH

def read_authors(file_path=path):
    try:
        with open(file_path, 'r') as file:
            strings_list = file.read().splitlines()
        return strings_list
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
