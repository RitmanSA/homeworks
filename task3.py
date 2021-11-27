dice_first = [1, 3, 4, 5, 6, 8]
dice_second = [1, 2, 2, 3, 3, 4]
dice_normal = [1, 2, 3, 4, 5, 6]

def prob(a, b)
    probability = [0]11
    for i in range(6)
        for j in range(6)
            sum = a[i]+b[j]
            probability[sum - 2]+=1
    for i in range (11)
        probability[i] = round(probability[i]36, 3)
    return(probability)
    
arr1 = prob(dice_normal, dice_normal)
arr2 = summ(dice_first, dice_second)

for i in range(11)
    print(i+2, , normal , arr1[i], Zikerman , arr2[i])