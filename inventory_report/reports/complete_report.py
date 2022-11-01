import datetime
from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, lista):
        data_de_validade = list()
        data_de_fabricacao = list()
        qtd_product = list()

        for element in lista:

            if element["data_de_validade"] >= str(datetime.date.today()):
                data_de_validade.append(element["data_de_validade"])

            if str(datetime.date.today()) > element["data_de_fabricacao"]:
                data_de_fabricacao.append(element["data_de_fabricacao"])

            qtd_product.append(element["nome_da_empresa"])

        qtd = dict(Counter(qtd_product).most_common(1))
        key_qtd = list(qtd.keys())[0]
        qtd_total = dict(Counter(qtd_product))
        lista = ""
        for key, value in qtd_total.items():
            lista += f"- {key}: {value}\n"

        return (
            f"Data de fabricação mais antiga: {min(data_de_fabricacao)}\n"
            f"Data de validade mais próxima: {min(data_de_validade)}\n"
            f"Empresa com mais produtos: {key_qtd}\n"
            f"Produtos estocados por empresa:\n"
            f"{lista}"
        )
