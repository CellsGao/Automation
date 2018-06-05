#P79 4.10.1 Practice

spam=[]
length=int(input('input the length'))
for i in range(length):
    spam.append(input('input somthing'))

print(spam)

theSentence=''
for i in range(length):
    if i==0:
        theSentence+=spam[i]
    elif i==length-1:
        theSentence+=', and '
        theSentence+=spam[i]
    else:
        theSentence+=', '+spam[i]

print(theSentence)

