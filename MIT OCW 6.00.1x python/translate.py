"""Translation of words from one language to another"""
def translateWord ( word, dictionary ) :
    if word in dictionary :
        return dictionary[word]
    else :
        return word

def translate(sentence) :
    translation = ''
    word = ''

    for c in sentence :
        if c != ' ' :
            word = word + c
        else :
            translation = translation + ' ' + translateWord(word,EtoF)
            word = ''
    return translation[1:] + ' ' + translateWord(word,EtoF)

EtoF = { 'amigo':'friend', 'te' : 'you','amo':'love' }
print translate("te amo amigo Rohan :)")

##
##def keySearch(L, k) :
##    for elem in L :
##       if elem == k :
##           return L[elem]
##    return None
##
##print keySearch(EtoF, 'amo')
