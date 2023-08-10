import os

class FolderFileScanner:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def get_file_paths(self):
        file_paths = []
        for root, _, files in os.walk(self.folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
        return file_paths

# Usage:
folder_path = '/path/to/your/folder'
scanner = FolderFileScanner(folder_path)
all_files = scanner.get_file_paths()

# Print the list of all file paths in the folder
print(all_files)
