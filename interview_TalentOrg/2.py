from collections import Counter

def ArrayChallenge(strArr):

    # store tmp values for judge
    parent = []
    children = []

    for i in strArr:
        children.append(int(i[1]))
        parent.append(int(i[3]))

    for k,v in Counter(parent).items():
        if v > 2:
            return False


    for k,v in Counter(child).items():
        if v > 1:
            return False
    return True

# keep this function call here 
print(ArrayChallenge(input()))