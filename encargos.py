from datetime import date

# para livros com status 'EMPRESTADO'

data_atual = date.today()
data_atual_brasil = data_atual.strftime(
    '%d/%m/%Y')  # TODO: TRATAR AS DATAS PARA QUE POSSAM SER LIDAS ADEQUADAMENTE E PARA QUE AS DIFERENÇAS SEJA CALCULDAS


def encargos_emprestimo(tarifa, data_retirada, data_devolucao_efetiva):
    data_devolucao = data_retirada + 3  # TODO: APÓS TRATAMENTO DAS DATAS, TRATAR O PERÍODO DO EMPRÉSTIMO
    dias_atraso = abs(data_devolucao_efetiva - data_devolucao)

    if data_devolucao_efetiva > data_devolucao:
        if dias_atraso == 0:
            multa = 0
            juros = 0
            total = tarifa + multa + juros
            print('A tarifa é de R${:.2f}.'.format(tarifa))
        elif dias_atraso <= 3:
            multa = (tarifa * 0.03)
            juros = (dias_atraso * (tarifa * 0.02))
            total = tarifa + multa + juros
        elif 3 < dias_atraso <= 5:
            multa = (tarifa * 0.05)
            juros = (dias_atraso * (tarifa * 0.04))
            total = tarifa + multa + juros
        elif 5 < dias_atraso:
            multa = (tarifa * 0.07)
            juros = (dias_atraso * (tarifa * 0.06))
            total = tarifa + multa + juros
        print('A data atual é {} e seu empréstimo possui data de devolução {}...'.format(data_atual_brasil, data_devolucao))
        print('A tarifa de R${:.2f} será acrescida de multa de R${:.2f} e juros de R${:.2f}, resultando no total de R${:.2f}.'.format(tarifa, multa, juros, total))
    else:
        print('Seu empréstimo deve ser devolvido na data indicada na retidada para cobrança normal da tarifa de R${:.2f}.'.format(tarifa))

encargos_emprestimo(10, 10, 13)
