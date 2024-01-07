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
    # Print statement here does not make a pyramid. Numbers are sorted but only by the first digit (ex: 9 is greater than 10).
    print(lines_as_strings)
        # print statement here makes a pyramid but code starts over with each line.

# Example Usage
message_file = 'coding_qual_input.txt'
result = decode(message_file)
print(result)


# for line in text:
#         # # makes each line a list of two strings.
#         # manyLines = line.split()
#         # print(manyLines)

#         lines_as_strings.append(line.strip())
#         # lines_as_strings.sort()
#     print(lines_as_strings)