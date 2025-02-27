# File Handling
'''Opening Files
        ->Use the build-in open() function to open a file
        ->The open() function returns a file object, which has a read() method for reading the content of the file
        ->The open() function takes two arguments: filename and mode
        ->There are four different methods (modes) for opening a file:
            ->"r" - Read - Default value. Opens a file for reading, error if the file does not exist
            ->"a" - Append - Opens a file for appending, creates the file if it does not exist
            ->"w" - Write - Opens a file for writing, creates the file if it does not exist
            ->"x" - Create - Creates the specified file, returns an error if the file exists
'''
'''
Reading File 
    .read()--->read entire File 
    .readline()--->read only one line at a time 
    .readlines()---->read all the lines 

'''

'''
Writing the files
    .write() | .writelines()-->multiple list of items 
'''


# Example to Read the file 
'''
f = open("sample.txt", "r")
print(f.read())

'''
'''
# example to write in the file 
with open("sample.txt","w") as file:
    file.write("complete the bachelor")
    file.writelines("[usman,waris], [104,105]")
    '''
# with the help of 'with' file are automatically closed 
    
'''
f = open("sample.txt", "r")
print(f.read())

'''
# exmaple of exceptional handling 
'''
try:
    with open("samples.txt","r") as file:
        content=file.read()
except FileNotFoundError:
    print("File Not Found")
'''


# Append the content 
'''
try:
    with open("sample.txt","a") as file:
        file.write("I am from Pakistan")
except FileNotFoundError:
    print("File Not Found")
'''    
# Exercise -->count the words in a file 

'''
def line_and_word_count(file_name):
    try:
        with open(file_name, "r") as file:
            lines=file.readlines()
            count_lines=len(lines)
            count_words=sum(len(line.split()) for line in lines)
            
            print(f"line count is {count_lines}")
            print(f"word count is {count_words}")
    except FileNotFoundError:
        print("File not found ")

line_and_word_count("sample.txt")

'''

# Exercise two -->write the list of items in a file
Student=[["Usman","Waris","Ali","Ahmed"],["104","105","106","107"]]
def write_list(file_name,lists):
    with open(file_name,"a") as file:
        for list in lists:
            for item in list:
                file.write(item)
                file.write("\n")

def display(file_name):
    with open(file_name,"r") as file:
        print(file.read())

def copy_file(file_name1,file_name2):
    with open(file_name1,"r") as file1:
        with open(file_name2,"a") as file2:
            file2.write(file1.read())

def occurence(file_name):
    with open(file_name,"r") as file:
        content=file.read()
        print(content)
        print(content.count("Usman"))
def log_message(file_name,message):
    with open(file_name,"a") as file:
        file.write(message)
        file.write("\n")
                
                
write_list("student.txt",Student)
display("student.txt")
copy_file("student.txt","student1.txt")

        
                


