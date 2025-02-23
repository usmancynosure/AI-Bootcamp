
import re
# Regular Expressions
# 1. regular expressions---sequence of characters that forms a search pattern
# 2. regular expressions---used to search, replace, and match text
# 3. regular expressions---used to validate the input
# 4. regular expressions---used to extract the information from the text
# Example are the email validation, phone number validation, etc
# 5. regular expressions---used to search the specific pattern in the text
# using the re module from the regex operations

text= "usmanwaris@gmail is my email address and my phone number is 0321-1234567 " #text
pattern=r"\d+" #pattern
result=re.findall(pattern,text) #searching the pattern in the text
print(" ".join(result))

updated_text=re.sub(r"\d","X",text) #replacing the pattern with the specified value
print(updated_text)