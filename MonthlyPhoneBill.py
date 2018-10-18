print("Please input your monthly contract fee: ",end = "£")
contractFee = float(input())
if contractFee > 0:
    print("Please input any extra charges on your bill: ",end = "£")
    additionalFee = float(input())
else:
    print("Please enter a contract fee above 0.")
    input()
    exit
resultFee = contractFee + additionalFee
print("Your total bill is: ",end = str.resultFee)
input()
