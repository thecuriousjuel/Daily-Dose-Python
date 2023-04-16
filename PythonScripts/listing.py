import os
import shutil

if not os.path.isdir('Images'):
    os.makedirs('Images')

for current, foldernames, filenames in os.walk('.'):
    print('Current : ', current)

    for foldername in foldernames:
        print('Foldername : ', foldername)

    for filename in filenames:
        print('Filename : ', filename)

        file_path = os.path.join(current, filename)
        # print('Pathname : ', file_path)

        if filename.endswith('jpg'):
            shutil.copy(file_path, 'Images')

    print('-'*50)