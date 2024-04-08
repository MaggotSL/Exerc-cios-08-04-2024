def maior(a, b, c):
  """Retorna o maior número entre a, b e c."""
  if a >= b and a >= c:
    return a
  elif b >= a and b >= c:
    return b
  else:
    return c

def menor(a, b, c):
  """Retorna o menor número entre a, b e c."""
  if a <= b and a <= c:
    return a
  elif b <= a and b <= c:
    return b
  else:
    return c

# Leitura dos números do usuário
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

# Encontrar o maior e o menor número
maior_numero = maior(a, b, c)
menor_numero = menor(a, b, c)

# Imprimir os resultados
print(f"O maior número é {maior_numero}.")
print(f"O menor número é {menor_numero}.")
