funcionarios = []

for i in range(2): 
    numeroFuncionario = int(input(f"Digite o número do funcionário {i + 1}: "))
    horasTrabalhadas = float(input(f"Digite o número de horas trabalhadas do funcionário {i + 1}: "))
    valorPorHora = float(input(f"Digite o valor recebido por hora do funcionário {i + 1}: "))
    salario = horasTrabalhadas * valorPorHora

    funcionario = {
        'Numero': numeroFuncionario,
        'Salario': salario
    }
    funcionarios.append(funcionario)


for funcionario in funcionarios:
    print(f"Funcionário Nº{funcionario['Numero']}: R${funcionario['Salario']:.2f}")
