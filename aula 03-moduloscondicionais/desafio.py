idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Você ainda não pode votar.")
elif 16 <= idade < 18 or idade >= 70:
    print("O voto é opcional.")
else:
    print("O voto é obrigatório.")