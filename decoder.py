lines_as_strings = []

# Function to decode the message.
def decode(message_file):
    # Open the given file and reads each line. 
    text = open(message_file, 'r')
    # Loops though and reads each line of text.
    for line in text:
        # # makes each line a list of two strings.
        # manyLines = line.split()
        # print(manyLines)

        lines_as_strings.append(line.strip())
        lines_as_strings.sort()
    return lines_as_strings


# Example Usage
message_file = 'coding_qual_input.txt'
result = decode(message_file)
print(result)