'''
Print final message
'''

def text(sen):
    "Prints final msg for .txt file"

    print(f'''Score:\t\t{int(round(sen.score, 1) * 10)}
Magnitude:\t{round(sen.magnitude, 1)}\n
 - score range is from -10 to 10
 - magnitude range is from 0 to infinity''')

def excel(file):
    "Prints final msg for .xls/.xlsx file"

    print(f'''\nDONE! RESULTS IN:\t{file}\n
 - score range is from -10 to 10
 - magnitude range is from 0 to infinity''')
