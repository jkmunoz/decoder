lines_as_strings = []

# Function to decode the message.
def decode(message_file):
    # Open the given file and reads each line. 
    with open(message_file, 'r') as text:
    # Loops though and reads each line of text.
        for line in text: 
            # Removes white space.
            lines_as_strings.append(line.strip())
    # Sorts lines by the first three characters
    sorted_lines = sorted(lines_as_strings, key=lambda x: int(x.split()[0]))
    return sorted_lines
        
# Example Usage
message_file = 'coding_qual_input.txt'
result = decode(message_file)
print(result)