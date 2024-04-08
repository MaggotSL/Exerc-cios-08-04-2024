class Numero:
    def __init__(self, valor):
        self.valor = valor

    def __lt__(self, outro):
        return self.valor < outro.valor

    def __str__(self):
        return f"{self.valor}"


def main():
    numeros = []
    for i in range(3):
        numero = int(input(f"Digite o {i + 1}º número: "))
        numeros.append(Numero(numero))

    numeros.sort(reverse=True)

    print("Os números em ordem decrescente são:", ", ".join(str(numero) for numero in numeros))


if __name__ == "__main__":
    main()
