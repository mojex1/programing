def vowel():
    word    = str(input('kalame mored nazar ra vared konid'))
    vowel   = ['a','A','e','E','o','O','i','I','u','U']
    found   = []
    for letter in word:
        if letter in vowel:
            if letter not in found:
                found.append(letter)
    for vowel in found:
        print(vowel)
vowel()
tekrar = str(input('bra adame Y,y type konid'))
while tekrar != "Y" or tekrar != 'y' :
    print(vowel())