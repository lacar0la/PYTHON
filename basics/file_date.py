import os
import datetime

#function to create a new file in the currento working directory, checks the date that
#the file was modified and returns just the date portion of the timestamp in the format 
#yyyy-mm-dd

def file_date(filename):
  # Create the file in the current directory
  with open(filename, 'w+') as file:
    timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  time = datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(time.strftime("%Y-%m-%d")))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
