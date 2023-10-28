# Read content from a file
"""If you pass the read method an integer argument,
 it will read up to that number of characters, 
 output all of them, and keep the 'window' at that
 position ready to read on."""
f = open('msg.txt', 'r')
file_word = f.read(8) # Read only 8 characters
file_data = f.read()
f.close()

print(file_word)
print(file_data)

# To open a file n times
files = []
for i in range(10):
    files.append(open('msg.txt', 'r'))
    print(i)

# To write into a file
f = open('msg_1.txt', 'w')  # Overwrites the content
# f = open('msg.txt', 'a')  # Adds the content
f.write('Hello World!')
f.close()

# To auto close a file after work
with open('msg.txt', 'r') as f:
    # file_data = f.readline()   # Reads the next line of a file
    file_data = f.read()

print(file_data)

# To create a list of lines in the file.
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)

# Function that takes only first names from a list
def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename, 'r') as f:
        for line in f:
            cast_list.append(line.split(',', 2)[0])
    return cast_list
cast_list = create_cast_list('flying_circus_cast.txt')
print(cast_list)

