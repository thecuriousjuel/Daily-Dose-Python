import os

number_of_folders = 5
number_of_files_per_folder = 10
extension = 'txt'

base_directory = 'base_directory'

for folder in range(1, number_of_folders+1):
    folder_name = f'folder_{folder}'
    folder_path = os.path.join(base_directory, folder_name)
    os.makedirs(folder_path)

    for file in range(1, number_of_files_per_folder+1):
        filename = f'filename_{file}.{extension}'
        file_path = os.path.join(folder_path, filename)

        with open(file_path, mode='w') as file_writer:
            file_writer.write(f'This is {filename}')

