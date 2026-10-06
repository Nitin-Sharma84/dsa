import random as r

numFaces=[1,2,3,4,5,6,7,8,9,'King','Queen','Ace','Jack']
syms=['Spade','Diamond','Club','Heart']
cards=[]
for sym in syms:
    for numFace in numFaces:
        cards.append(f'{numFace} of {sym}')

r.shuffle(cards)

for card in cards:
    print(card)
