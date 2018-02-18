""" at codeagon at hackerraank.com
"""

##still looks retarded..........
def add_to_top() :
    
def add_to_stack(letter) :
    stack.append(letter)
message = list(raw_input())
##print message
stack = ['' for i in message]
new_message = []

for letter in message[1:] :
    from_top()
    add_to_stack(letter)
    
"""

Problem Statement


Goku has written a secret message using some blocks. Each block contains a character. 
 Gohan likes to play with these blocks. He stacks these blocks on top of one another. At any point of time, Gohan can move a block from the front of the secret message to the top of the stack or he can remove the block from the top and add it to the end of a new message that he has created. Gohan creates this new message by adding the blocks that he removed from the top of the stack to the end of a new string in the order in which they were removed from the top of the stack. The final message has the same number of characters as the original message i.e. all the blocks must be removed from the stack. 

For example: 
 Goku has created the message "ab" using the blocks. 


Gohan can create two messages "ab" and "ba".

Goku is worried that his original message might be lost. He wants to know the number of ways in which Gohan could have recreated the original message and the number of distinct messages that Gohan could have created.


Input Format


The input consists of a string S denoting Goku's message.

Constraints 

1≤|S|≤10


Output Format


Output the number of ways in which Gohan could have recreated the original message and the number of distinct messages Gohan could have created.


Sample Input

ball



Sample Output

2 9



Explanation


Gohan can create the following 9 messages : {llab, lalb, labl, allb, albl, abll, blla, blal, ball}

He could have recreated the original message "ball" in 2 ways: 
1. Insert 'b', Remove 'b', Insert 'a', Remove 'a', Insert 'l', Insert 'l', Remove 'l', Remove 'l' 
2. Insert 'b', Remove 'b', Insert 'a', Remove 'a', Insert 'l', Remove 'l', Insert 'l', Remove 'l'


"""
