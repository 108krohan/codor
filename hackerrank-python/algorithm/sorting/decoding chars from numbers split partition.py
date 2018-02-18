"""decoding characters at shubham kesarwani
"""
##    ''.join([o if not o in string.punctuation else ' ' for o in s]).split()
##
##    tokens = [x.strip() for x in data.split(',')]


elems = "19-15-13-5-20-9-13-5-19 16-5-15-16-12-5 4-15-14-20 23-1-9-20"
words = []

while len(elems) > 0:

    # Partition on first space.
    parts = elems.partition(" ")
    one_word = parts[0]
    numbers = one_word.split("-")
##    print numbers
    letters = [chr(int(c)+64) for c in numbers]
##    letters = [chr(c) for c in one_word if c != '-']
    decoded_word = "".join(letters)
    words.append(decoded_word)
    elems = parts[2]

for elem in words :
    print elem,
