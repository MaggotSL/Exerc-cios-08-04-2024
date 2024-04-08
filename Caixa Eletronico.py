def caixa_eletronico(valor_saque):
  """Simula o funcionamento de um caixa eletrônico.

  Args:
      valor_saque: Valor do saque desejado (int).

  Returns:
      Dicionário com a quantidade de notas de cada valor.
  """

  notas_disponiveis = {
      100: 0,
      50: 0,
      10: 0,
      5: 0,
      1: 0,
  }

  if not 10 <= valor_saque <= 600:
    raise ValueError("Valor do saque inválido. Informe um valor entre R$ 10 e R$ 600.")

  while valor_saque > 0:
    for valor_nota in sorted(notas_disponiveis.keys(), reverse=True):
      if valor_saque >= valor_nota:
        numero_notas = valor_saque // valor_nota
        valor_saque -= numero_notas * valor_nota
        notas_disponiveis[valor_nota] += numero_notas

  return notas_disponiveis

valor_saque = int(input("Digite o valor desejado para saque: "))
notas_saque = caixa_eletronico(valor_saque)

for valor_nota, numero_notas in notas_saque.items():
  if numero_notas > 0:
    print(f"{numero_notas} notas de R$ {valor_nota}")
