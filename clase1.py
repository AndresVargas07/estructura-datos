x=int (input ("Escribir un número"))
y=int (input("Escribir un número"))
z=int (input("Escribir un número"))


if x<y and y>z:
  print("Este número es el menor",x, "El número mayor es",y)

elif y<x and x>z:
  print("Este número es el menor",y, "El número mayor es",x)

elif z<x and x>y:
  print("Este número es el menor",z, "El número mayor es",x)

else:
  print("Los números son iguales")
  

