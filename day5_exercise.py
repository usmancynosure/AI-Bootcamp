# Exercise 1 -->Create the Text Cleaner 
# '''
# # Text Cleaner\
import re
'''
def text_cleaner(text):
    pattern=r"[^a-zA-Z0-9\s]"
    result=re.sub(pattern,"",text)
    final_result=result.strip()
    return final_result.lower()


user =input("Enter the text: ")

print(text_cleaner(user))
'''
# Exercise 2 -->Create the Email Validator
'''
def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, text)
    return emails

# Example Input
text = "Contact us at support@example.com or sales123@shop.co for inquiries."

print(extract_emails(text))

'''

# Ex3 -->validate the password

'''
def validate_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return bool(re.match(pattern, password))

# Example Inputs
passwords = ["Pass@123", "weakpass", "Strong1!", "Hello123"]
for pwd in passwords:
    print(f"{pwd}: {validate_password(pwd)}")
'''

# Ex4 -->find the palindrome after cleaning the text
import re

def clean_text(text):
    """Removes all non-alphanumeric characters and converts text to lowercase."""
    cleaned_text = re.sub(r"[^a-zA-Z0-9]", "", text)  # Keep only letters & digits
    return cleaned_text.lower()

def is_palindrome(text):
    """Checks if the given text is a palindrome."""
    cleaned_text = clean_text(text)
    return cleaned_text == cleaned_text[::-1]  # Reverse comparison

# User input
text = input("Enter a text: ")

# Check palindrome
if is_palindrome(text):
    print("The given text is a palindrome!")
else:
    print("The given text is NOT a palindrome.")
