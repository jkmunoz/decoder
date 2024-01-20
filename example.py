# txt_file = ['3 love', '6 computers', '2 dogs', '4 cats', '1 I', '5 you']
# def decode():
#     sorted_file = sorted(txt_file)

#     row = 0
#     last_words_string = ''

#     for i in range(len(sorted_file)):
#         for j in range (0, i + 1):
#             if row >= len(sorted_file):
#                 break
#             pairs = sorted_file[row].split()
#             last_word = pairs[-1]
#             row += 1
#             print(pairs, end=' ')
#         last_words_string += last_word + ' '
#         print()
#     # Why is this printing all of the words?
#     print(last_words_string)

# decode()


#     txt_file = ['3 love', '6 computers', '2 dogs', '4 cats', '1 I', '5 you']
#     sorted_file = sorted(map(str.split, txt_file), key=lambda t: int(t[0]))
#     print(*(
#         sorted_file[(n + 1) * (n + 2) // 2 - 1][1]
#         for n in range(int((8 * len(sorted_file) + 1) ** .5 - 1) // 2)
#     ))

# decode()


def decode(txt_file):
    ordered = sorted((int(a), b) for a, b in map(str.split, txt_file))
    width = 1  # number of items on the same line in the triangle
    last = 0 # index of the last item on the current line in the triangle
    words = []
    while last < len(ordered):
        words.append(ordered[last][1])
        width += 1
        last += width
    return  " ".join(words)

# Example run
txt_file = ['3 love', '6 computers', '2 dogs', '4 cats', '1 I', '5 you']
print(decode(txt_file))