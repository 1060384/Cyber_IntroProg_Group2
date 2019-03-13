import math
#Python Lab task
#Author: Stephane Lajoie
#Date: 13/03/2019

#define Variables
input1 = 0
input2 = 0
sumOfAll = 0
remainder = 0


input1 = int(input("Please input the 1st integer"))
input2 = int(input("Please input the 2nd integer"))


sumOfAll = input1 + input2
sumOfAll = input1 * input2
sumOfAll = sumOfAll + (input1 + input2)
sumOfAll = sumOfAll + (input1 - input2)
sumOfAll = sumOfAll + (input1 / input2)
print(sumOfAll)

#If the remainder > 0 then display r5emoander
remainder = float(sumOfAll % 1)
if remainder > 0:
  print("There is a remainder.")
else:
  print("There is no Remainder.")



