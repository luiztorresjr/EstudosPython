preco = float(input("ENTRE COM O PRECO: "))
percentual = float(input("ENTRE COM A PORCENTAGEM: "))
desconto=float(preco *(percentual/100))
print("VALOR DO DESCONTO %5.2f: " % desconto)
preco = (preco - desconto)
print("NOVO SALARIO %6.2f" %preco)
