def adjacentElementsProduct(inputArray):
    newpro = min(inputArray)
    if len(inputArray) == 2:
        newpro = inputArray[0]*inputArray[1]
    else:
        for i in range(len(inputArray)-1):
            product= inputArray[i] * inputArray[i+1]
            if newpro < product:
                newpro = product
                i = i+1
            else:
                i = i+1
    return(newpro)


return max([ia[i] * ia[i+1] for i in range(len(ia)-1)])