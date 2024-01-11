lines_as_strings = []

# Function to decode the message.
def decode(message_file):
    # Open the given file and reads each line. 
    text = open(message_file, 'r')
    # Loops though and reads each line of text.
    for line in text:   
        lines_as_strings.append(line.strip())
        sorted_lines = sorted(lines_as_strings, key=lambda x: x[:3])
    # Print statement here does not make a pyramid. Numbers are sorted but only by the first digit (ex: 9 is greater than 10).
    # print(sorted_lines)
        # print statement here makes a pyramid but code starts over with each line.
        # print(sorted_lines)
    return sorted_lines
        
# Example Usage
message_file = 'coding_qual_input.txt'
result = decode(message_file)
print(result)