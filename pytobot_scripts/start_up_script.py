import os


def create_local_folders():
    pictures_folder = os.path.join(os.path.expanduser("~"), "Pictures")
    pictures_folder_path = os.path.join(pictures_folder, "pytobot")
    if not os.path.exists(pictures_folder_path):
        os.makedirs(pictures_folder_path)
        print(f"Created '{pictures_folder_path}' directory")
    else:
        print(f"'{pictures_folder_path}' directory already exists")


if __name__ == "__main__":
    create_local_folders()
