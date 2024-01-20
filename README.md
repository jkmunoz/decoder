The function decode(message_file) reads text from a message file, arranges the number-word pairs in numerical order in the shape of a triangle, and return a string of the last words on each row. 

The text looks something like this...
3 love
6 computers
2 dogs
4 cats
1 I 
5 you

Which means the triangle would be...
1 I
2 dogs 3 love
4 cats 5 you 6 computers

And the string should print...
"I love computers"
