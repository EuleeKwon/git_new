def checkPalindrome(inputString):
    for i in range(len(inputString)):
        if inputString[i] == inputString[-(i+1)]:
            i = i+1
        else:
            return(0)
    return ("true")