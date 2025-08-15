cargo = input("Qual e o seu cargo na empresa de Desenvolvimento de sistemas:")
dia_semana = input("digite o dia da semna:")

if cargo == "gerente":
    print("Acesso permitido bem vindo!!")
    
elif cargo == "analista":
    if dia_semana == "segunda-feira" or dia_semana == "terça-feira" or dia_semana =="quarta-feira" or dia_semana == "quinta-feira" or dia_semana or "sexta-feira":
        print("acesso permitido analista ")
    else:
        print("acesso negado ")
        