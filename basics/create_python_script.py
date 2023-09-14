#function that creates a new document in the current working directory, adds the line of comments to it
#declared by the "comments" variable and returns the size of the new file
import os

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open (filename,'w+') as file:
    file.write(comments)
    file.close()
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))
