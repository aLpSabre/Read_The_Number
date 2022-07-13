
my_dict={"0":"","1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine",}
two_digits={"0":"","1":"Ten","2":"Twenty","3":"Thirty","4":"Fourty","5":"Fifty","6":"Sixty","7":"Seventy","8":"Eighty","9":"Ninety"}
two_digits_startsWith_one={"10":"Ten","11":"Eleven","12":"Twelve","13":"Thirteen","14":"Fourteen","15":"Fifteen","16":"Sixteen","17":"Seventeen","18":"Eighteen","19":"Nineteen"}
three_digits="Hundered"
four_digits="Thousand"

while True:
  number=input("Pls Enter a number! : ")
  if (number[0]=="0" and len(number)==1):  # To get the definition of 0
    print("Zero")
    break
  elif number.isdigit() and len(number)<5 :  # To only get digits 
    break
  else :
    print("Pls enter a valid number! : ")

length=len(number) #  to get the length of the number, so we can itarate with it

for i in reversed(range(0,length+1)):  # to get the index of the element in a number

  if(i==4 ):  # index
    if(number[-i]!="0"):  # we use always the negative index to get the number at same position always
          print(my_dict[number[-i]]+" "+four_digits,end=" ")
    elif number[-i]!="0": 
      print(four_digits,end=" ")
          
  elif(i==3) :
    if(number[-i]!="0"):
      print(my_dict[number[-i]]+" "+three_digits,end=" ")
    elif  number[-i]!="0":
      print(three_digits,end=" ")

  elif(i==2 and number[-i]=="1"):
      print(two_digits_startsWith_one[number[-2:]])
      break

  elif (i==2 and  number[-i]!="0" ):
      print(two_digits[number[-i]],end=" ")

  elif(i==1):
    print(my_dict[number[-i]],end=" ")
    
