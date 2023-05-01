import os
from datetime import datetime, timedelta

number_of_folders = 5
number_of_files_per_folder = 10
extension = 'txt'

base_directory = 'File Inventory'
if not os.path.isdir(base_directory):
    os.makedirs(base_directory)

today = datetime.now()

for folder in range(1, number_of_folders+1):
    folder_name = f'folder_{folder}'
    folder_path = os.path.join(base_directory, folder_name)
    os.makedirs(folder_path)

    for file in range(1, number_of_files_per_folder+1):
        if file % 3 != 0:
            american_date = today.strftime('%m-%d-%Y')
            filename = f'filename_{american_date}.{extension}'
        else:
            filename = f'filename_{file}.{extension}'

        file_path = os.path.join(folder_path, filename)

        with open(file_path, mode='w') as file_writer:
            file_writer.write(f'This is {filename}')

        today += timedelta(days=1)

