valor = 0
total = 0
soma = 0
loop = True

while loop == True:
  valor = int(input("digite um valor"))
  total = total + 1
  soma = soma + valor

  if valor == 999:
    loop = False
    print(soma - 999)
    print(total - 1)