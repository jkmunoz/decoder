# Function to decode the message.
def decode(message_file):
    content = open(message_file, 'r')
    for line in content:
        print(line)

# Example Usage
message_file = 'coding_qual_input.txt'
print(decode(message_file))