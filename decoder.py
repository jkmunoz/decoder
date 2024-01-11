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

    current_pair_index = 0

    # This is an outer loop to handle the # of ROWS.
    for i in range(0, len(sorted_lines)):
        # This is an inner loop to handle the # of COLUMNS.
        for j in range(0, i + 1):
            current_pair = sorted_lines[current_pair_index].split()
            print(f"{current_pair[0]} {current_pair[1]}", end=' ')
            current_pair_index += 1
        print()


    # print(sorted_lines)
# Example Usage
message_file = 'coding_qual_input.txt'
decode(message_file)


