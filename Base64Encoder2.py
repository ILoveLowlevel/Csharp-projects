import math
import base64
from colorama import Fore, Back, Style

## STEP 1

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

print("''Hello world'' in binary is ")
print(toBinary("Hello world"))
Base64encode = input("Yo guys what was happening :")
Hello = toBinary(Base64encode)
LongBinaryList = len(toBinary(Base64encode)) ## len(toBinary(Base64encode))
RLBL = LongBinaryList * 8
Remain = RLBL % 6
add_number = (8 - Remain)
BinarySix = ""
x = 0


for i in Hello:
    BinarySix = BinarySix + str(i)
    x = x + 1

print(x,"-",LongBinaryList,"-",Remain,"-",add_number,"-",RLBL)
print("BinarySix:",BinarySix)
print(len(BinarySix))
LBinarySix = len(BinarySix)
## Adding Extra Binaries

if Remain == 0:
    pass
else:
    for i in range(add_number):
        BinarySix = BinarySix + "0"
print("BinarySixnew:",BinarySix)
print(len(BinarySix))
## STEP 2

BinarySixList = []
BinaryTransporter = ""
for i in range(len(BinarySix)):
    BinaryTransporter = BinaryTransporter + str(BinarySix[i])
    if (i % 6) == 0:
        BinarySixList.append(BinaryTransporter)
        BinaryTransporter = ""
    else:
        pass

## Some Fixing
BinarySixList[1] = BinarySixList[0] + BinarySixList[1]
del BinarySixList[0]
print(BinarySixList)

## STEP 3 adding 2 binaries each 6 binary groups

LongBinarySixList = len(BinarySixList)

for i in range(LongBinarySixList):
    if i == 0:
        BinarySixList[i] =  "0" + BinarySixList[i]
    else:
        BinarySixList[i] = "00" + BinarySixList[i]


print("Final:",BinarySixList)

## Binary To Decimal Converter

def binaryToDecimal(n):
    return int(n,2)

DecimalList = []

for i in range(LongBinarySixList):
    DecimalList.append(binaryToDecimal(BinarySixList[i]))
print("Decimal",DecimalList)

Base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/======================================================================================================="
Encoded = ["",""]
Encode = ""

LongDecimalList = len(DecimalList)


for i in range(LongDecimalList):
    Encode = Encode + Base64[int(DecimalList[i])]
print(Fore.RED+'Base64::')
print(Encode)

stop = input("--------END of UNIVERSE :D--------")