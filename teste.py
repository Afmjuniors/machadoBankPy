from models.cliente import Cliente
from models.conta import Conta

alexandre: Cliente = Cliente('Alexandre Machado', 'alexandre@email', '123.456.789-10', '12/12/1985')

# print(alexandre)

contaa: Conta = Conta(alexandre)
print(contaa)
