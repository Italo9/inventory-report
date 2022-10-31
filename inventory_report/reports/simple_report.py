from collections import Counter
import datetime


class SimpleReport:
    @classmethod
    def generate(lista):
        data_de_validade = []
        data_de_fabricacao = []
        qtd_product = []
        for element in lista:
            if (
                datetime.date.fromisoformat(element["data_de_validade"])
                >= datetime.date.now()
            ):
                data_de_validade.append(element["data_de_validade"])
            if datetime.date.now() > datetime.date.fromisoformat(
                element["data_de_fabricacao"]
            ):
                data_de_fabricacao.append(element["data_de_fabricacao"])
            qtd_product.append(element["nome_da_empresa"])
        qtd = dict(Counter(qtd_product).most_common(1))
        key_qtd = list(qtd.keys())[0]
        return (
            f"Data de fabricação mais antiga: {min(data_de_fabricacao)}\n"
            f"Data de validade mais próxima: {min(data_de_validade)}\n"
            f"Empresa com mais produtos: {key_qtd}"
        )
