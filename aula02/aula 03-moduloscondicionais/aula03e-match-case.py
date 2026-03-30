escolha_usuario = 0

match escolha_usuario:
    case 0:
        status = "sair do progama"
    case 1:
        status = "entrar no progama"
    case _:
        status = "erro"

print(status)