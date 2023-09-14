import os
#function that creates a new directory inside the current working direcotry, then creates a new empty file inside the new directory
#and returns the list of the files in that directory.
def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, 'w+') as file:
    file.close()
    pass
  os.chdir("..")

  # Return the list of files in the new directory
  return (os.listdir(directory))

print(new_directory("PythonPrograms", "script.py"))
