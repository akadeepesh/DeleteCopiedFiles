import os


def delete_files_with_copy(start_path):
    for dirpath, dirnames, filenames in os.walk(start_path):
        for filename in filenames:
            if "Copy" in filename:
                file_path = os.path.join(dirpath, filename)
                os.remove(file_path)
                print(f"Deleted {file_path}")


delete_files_with_copy("C:/Users/(enter)/(your)/(path)")
