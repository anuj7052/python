amount = 2000

if amount%100==0:
    if amount>=500:
        notes = amount//500
        print("500 Rs notes are", notes)
        amount = amount%500
    if amount>=200:
        notes = amount//200
        print("200 Rs notes are", notes)
        amount = amount%200
    if amount >=100:
        notes = amount//100
        print("100 Rs notes are", notes)

else:
    print("Amount Should be Multiple of 100")
