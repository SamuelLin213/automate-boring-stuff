import os

# joining file path
os.path.join('folder1', 'folder2', 'file.png') # connects w/ appropriate slash

# get current working directory
os.getcwd()

# change current working directory
os.chdir('c:\\')

# get absolute path of file
os.path.abspath('file.png')

# check if path is absolute
os.path.isabs('c:\\file.png')

# get relative path between two locations
os.path.relpath('targetPath', 'originPath')

# get directories of path
os.path.dirname('path')

# get basename(last folder/file) of path
os.path.basename('path')

# check if path exists on filesystem
os.path.exists('path')

# check filetype
os.path.isfile('path')
os.path.isdir('path')

# size of file
os.path.getsize('path')

# get files/folders of path
os.path.listdir('path')

# create new folder
os.path.makedirs('path') # creates new directory
