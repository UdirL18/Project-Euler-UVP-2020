#==================================================================
#Largest prime factor
#==================================================================  
#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
###################################################################
def najvecji_prafaktor(n):
    i = 2
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
    return n

#600851475143|8857
#    87625999|1471
#       59569|839
#          71|71
#           1

