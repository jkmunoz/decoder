lines_as_strings = []
message = []

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

    current_pair_index = 0

    # This is an outer loop to handle the # of ROWS.
    for i in range(0, len(sorted_lines)):
        # This is an inner loop to handle the # of COLUMNS.
        for j in range(0, i + 1):
            if current_pair_index >= len(sorted_lines):
                # break out of the inner loop so the index is always within range.
                break
            current_pair = sorted_lines[current_pair_index].split()
            # last_string = current_pair[-1]
            # message.append(last_string)
            print(current_pair, end=' ')
            current_pair_index += 1
        print()
    # return message

# Example Usage
message_file = 'coding_qual_input.txt'
result = decode(message_file)
print(result)


