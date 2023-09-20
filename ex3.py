numeroFuncionario = int(input("Digite o número do funcionário: "))
horasTrabalhadas = float(input("Digite o número de horas trabalhadas: "))
valorPorHora = float(input("Digite o valor recebido por hora: "))
salario = horasTrabalhadas * valorPorHora

print(f"O funcionário Nº{numeroFuncionario} tem um salário de R${salario:.2f}")
