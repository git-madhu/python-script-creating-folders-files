import os

folders = ['Folder1', 'Folder2']
file_contents = [
    'Testing python script using Azure Pipelines',
    'Testing python script with Azure DevOps Pipelines'
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    file_name = os.path.join(folder, 'file1.txt')
    with open(file_name, 'w') as file:
        file.write(file_contents[folders.index(folder)])
    print(f'Created {file_name}')
