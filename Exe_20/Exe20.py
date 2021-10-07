from sys import argv

script, input_file = argv

def print_all(f):   # Function to print entire file
    print(f.read())

def rewind(f):  # Set pointer to zero eth position
    f.seek(0)

def print_a_line (line_count,f): # Function to print the present line
    print(line_count,f.readline(), end='')

current_file = open(input_file)
print("Let's print the entire file.")
print_all(current_file)

print("Let's rewind, like a tape.")
rewind(current_file)

print("Let's print three lines\n")
current_line = 1
print_a_line(current_line,current_file)
current_line += 1
print_a_line(current_line,current_file)
current_line = current_line + 1
print_a_line(current_line,current_file)

