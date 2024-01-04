content = []
# Function to decode the message.
def decode(message_file):
    # Open the given file and reads each line. 
    text = open(message_file, 'r')
    for line in text:
        content.append(line)
        print(content)

# Example Usage
message_file = 'coding_qual_input.txt'
print(decode(message_file))