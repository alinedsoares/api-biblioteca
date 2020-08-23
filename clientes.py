import encargos


class Cliente:
    def __init__(self, id_cliente, id_livro_emprestado):
        self.id_cliente = id_cliente
        self.id_livro_emprestado = id_livro_emprestado


clientes = Cliente(0, 22)

if clientes.id_livro_emprestado is not None: #TODO: O RETORNO ESTÁ CONFLITANDO COM A ESTRUTURA CONDICIONAL
    encargos.encargos_emprestimo(10, 10, 22)
    print(clientes.id_livro_emprestado)
else:
    print('Cliente sem empréstimos')
