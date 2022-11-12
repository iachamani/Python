def squareroot(a,precision):
    y = a
    while(True):
      root = 1/2*(y+a/y)
      if abs(root-y) <= precision:
        break
      y = root
    return root
   
x = float((input("Type a number : ")))
#precision example 0.00000001 or 0.0001
l = float(input("what is the precision you want :"))
result = squareroot(x,l)
print(result)

#calculating square root with Newton's Method
