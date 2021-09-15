numbers=[3,6,9,3,2,7]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if(numbers[i]==numbers[j]):
            print(numbers[i],"is a duplicate")
            break