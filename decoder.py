lines_as_strings = []

# Function to decode the message.
def decode(message_file):
    # Open the given file and reads each line. 
    with open(message_file, 'r') as text:
        # Loops through and reads each line of text.
        for line in text: 
            # Removes white space.
            lines_as_strings.append(line.strip())
    # 
    ordered = sorted((int(a), b) for a, b in map(str.split, lines_as_strings))
    width = 1 # Number of items on the same line as the pyramid.
    last_word = 0 # Index of the last item on the current line in the pyramid. 
    words = []
    while last_word < len(ordered):
        words.append(ordered[last_word][1])
        width += 1
        last_word += width
    return " ".join(words)

# Example Usage
message_file = 'coding_qual_input.txt'
result = decode(message_file)
print("The decoded Message is:", result)





