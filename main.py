def comb(num1,num2,num3,num4):  
    for num1 in range(4):
        for num2 in range(4):
            for num3 in range(4):
                for num4 in range(4):
                    if (num1!=num2 and num2!=num3 and num1!=num3 and num4!=num3 and num4!=num2):
                        print(num1, num2, num3)
                      
numb1 = int(input('Enter number: '))
numb2 = int(input('Enter number: '))
numb3 = int(input('Enter number: '))
numb4 = int(input('Enter number: '))
comb([numb1, numb2, numb3, numb4])
