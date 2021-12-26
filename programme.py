# gcd-python-of-two-polynomials
#a programme that calculate gcd of two polynomials using gmpy2 module in python
#importation de package gmpy2
import gmpy2
#function to count the first zeros of a list
def count_zeros(list):
    i=0
    count=0
    for i in range(len(list)):
        if list[i] == 0 :
            count+=1
        else:
            break
    return count
#function to remove the first zeros in a list
def remove_first_zeros(count,list):
    for i in range(len(list)-count):
        list[i]=list[i+count]
    list=list[:-count]
    return list
#function to multiply the quotient we find using gmp2.div
def mul_sub(q,poly1,poly2):
    for i in range(len(poly2)):
        poly1[i]-=q*poly2[i]
    return poly1

#function to assign list2 to list1
def remp(list1,list2):
    i=0
    for i in range(len(list2)):
        list1.append(list2[i]) 
#function to divide poly1 with poly2 and return the quotient of tuples and the rest
def division(poly1,poly2):
    if len(poly1)<len(poly2):
        return division(poly2,poly1)
    list=[]
    while len(poly1) >= len(poly2):
        q=float(gmpy2.div(poly1[0],poly2[0])) #q is quotient of poly1 [0] and poly2 [0]
        list.append(q)
        poly1 = mul_sub(q,poly1,poly2)
        c = count_zeros(poly1)
        poly1 = remove_first_zeros(c,poly1)
    r=[]
    remp(r,poly1)
    return poly2,r
#main programme :
poly1=[]
poly2=[]
deg1=int(input("donner la degre de 1er polynome"))
i=0
while i <= deg1:
    print("donner a"+str(deg1-i))
    a=int(input())
    poly1.append(a)
    i+=1
deg2=int(input("donner la degre de la 2eme polynome"))
i=0
while i <= deg2:
    print("donner a"+str(deg2-i))
    a=int(input())
    poly2.append(a)
    i+=1
a,b=division(poly1,poly2)
while len(b) != 0:
    a,b=division(a,b)
pgcd = [i * 1/a[0] for i in a]
print("le pgcd est :")
if len(pgcd)==1 :
 print (pgcd[0])
else:
    for i in range(len(pgcd)-1):
        if pgcd[i] !=0:
          print("("+str(pgcd[i])+")x^"+str(len(pgcd)-1-i)+"+", end="")
        else:
            continue
    print("("+str(pgcd[len(pgcd)-1])+")")
#code by NADIR EL HAJJAJI MCSC
