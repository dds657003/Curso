
def letras_na_frase(frase, letra):
    contagem = 0
    for x in frase:
        if x == letra:
            contagem = contagem + 1
    return contagem

frase = input("entre com a frase: ").lower()
letra = input("qual letra deseja verificar: ").lower()

contagem = letras_na_frase(frase, letra)
print(f"esta frase tem {contagem} {letra}")



