"""The contains_acronym function checks the text for the presence of 2 of more characters or digits surrounded by parentheses, with at least the first character in uppercase(if it’s a letter), returning True if the condition is met, or False otherwise. For example, “Instant messanging (IM) is a set of communication technologies used for text-based communication “should return True since (IM) satisfies the match conditions” Fill in the regular expression in this function """

import re
def check_tim(text):
  pattern = r"\([A-Z1-9][a-zA-Z1-9]*\)"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
