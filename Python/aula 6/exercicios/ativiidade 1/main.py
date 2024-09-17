class Empregado:
        def __init__(self, nome, salario_base):
            self.nome = nome 
            self.salario_base = salario_base
            self.bonus_fixo = 3000
        def salario_base(self):
              ...
    


class Gerente(Empregado):
      def calculoSalario(self):
            return f"{self.salario_base + self.bonus_fixo}"
      
class Vendedor(Empregado):
      def calcularSalario(self,comissao,total_vendas):
            return f"{self.salario_base + comissao + total_vendas} "
      
      
matheus = Gerente("Matheus", 10000)
maquisuta = Vendedor("Maquisuta", 500)
maquisuta.calcularSalario(10,70)

print(f"Gerente tem o salario de {matheus.calculoSalario()}")
print(f"Vendedor tem o salario de {maquisuta.calcularSalario(total_vendas=500, comissao=70000)}")

        

