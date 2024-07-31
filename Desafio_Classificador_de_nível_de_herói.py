nome = input("Qual o nome do seu herói?\n")
xp = int(input("Qual a quantidade de experiência (XP) do seu herói?\n"))

if xp < 1000:
    print(f"O Herói de nome {nome} está no nível de Ferro")
elif 1001 <= xp <= 2000:
    print(f"O Herói de nome {nome} está no nível de Bronze")
elif 2001 <= xp <= 5000:
    print(f"O Herói de nome {nome} está no nível de Prata")
elif 5001 <= xp <= 7000:
    print(f"O Herói de nome {nome} está no nível de Ouro")
elif 7001 <= xp <= 8000:
    print(f"O Herói de nome {nome} está no nível de Platina")
elif 8001 <= xp <= 9000:
    print(f"O Herói de nome {nome} está no nível de Ascendente")
elif 9001 <= xp <= 10000:
    print(f"O Herói de nome {nome} está no nível de Bronze")
elif xp >= 10001:
    print(f"O Herói de nome {nome} está no nível de Imortal")
