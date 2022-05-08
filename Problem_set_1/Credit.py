# Details of cards company
# American Express: [Startswith = (34,37) and length = 15]
# Master Card: [StartsWith= (51,52,53,54,55) and length = 16]
# Visa Card: [StartsWith= 4 and length = (13 and 16)]


def checksum(cardnumber):
    sum=cardsum=leftsum= 0
    for i in range(len(cardnumber)-1,-1,-1):
        if i % 2 == 0:
            sum = int(cardnumber[i])*2
            if len(str(sum)) > 1:
                while(sum !=0):
                    r = sum % 10
                    sum //= 10
                    cardsum += r
            else: 
                cardsum += sum
        else:
            leftsum += int(cardnumber[i])

    print("Total cardsum",cardsum) 
    print("Total leftsum",leftsum) 
    if((cardsum+leftsum)%10 == 0):
        return True
    else:
        return False

input = input("Enter the Card Number: \n")
if ((input[0:1]=='4') and (len(input) in [13,16]) and checksum(input)):
    print("Visa")
elif((input[0:2] in ['34','37']) and (len(input) == 15) and checksum(input) ):
    print("American Express")
elif((input[0:2] in ['51','52','53','54','55']) and (len(input) == 16) and checksum(input)):
    print("MasterCard")
else:
    print("Invalid Card")
