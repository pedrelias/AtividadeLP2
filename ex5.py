class Funcionario:
    def __init__(self, numero, horasTrabalhadas, valorPorHora):
        self.numero = numero
        self.horasTrabalhadas = horasTrabalhadas
        self.valorPorHora = valorPorHora

    def calcularSalario(self):
        return self.horasTrabalhadas * self.valorPorHora


def lerDadosFuncionario():
    numeroFuncionario = int(input("Digite o número do funcionário: "))
    horasTrabalhadas = float(input("Digite o número de horas trabalhadas: "))
    valorPorHora = float(input("Digite o valor recebido por hora: "))
    return Funcionario(numeroFuncionario, horasTrabalhadas, valorPorHora)


funcionario = lerDadosFuncionario()


salario = funcionario.calcularSalario()

print(f"Funcionário Nº{funcionario.numero}: R${salario:.2f}")
