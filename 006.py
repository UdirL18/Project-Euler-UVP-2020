#==========================================================================================
#Sum square difference
#========================================================================================== 
#Problem 6
#The sum of the squares of the first ten natural numbers is, 385
#The square of the sum of the first ten natural numbers is, 55**2 == 3025
#Hence the difference between the sum of the squares of the first ten natural numbers
#and the square of the sum is 3025 - 385 = 2640
#
#Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.
###########################################################################################
def vsota_kvadratov(n): #v našem primeru je n = 100
    vsota = 0 
    for i in range(1, n + 1):
        vsota += i ** 2
    return vsota

def vsota_na_kvadrat(n):
    vsota = 0
    for i in range(1, n + 1):
        vsota += i
    return vsota ** 2

print(vsota_na_kvadrat(100) - vsota_kvadratov(100)) #25164150
