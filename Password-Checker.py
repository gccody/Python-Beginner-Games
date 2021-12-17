password = input("Password: ")
containsupper = False
containslower = False
containsletter = False
containsnumber = False
punc = False
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '-_;:,./\!@#$%^&*()'
score = 0

if len(password) >= 8:
    score += 5

for char in password:
    if char in letters.lower():
        containslower = True
        containsletter = True
    if char in letters:
        containsletter = True
        containsupper = True
    if char.isdigit():
        containsnumber = True
    if char in punctuation:
        punc = True
if containsletter and containsnumber:
    score += 10
if punc:
    score += 5
if containsupper and containslower:
    score += 10

print(f"Score: {score}")