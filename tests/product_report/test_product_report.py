from inventory_report.inventory.product import Product


def test_relatorio_produto():
    result = Product(
        id=1,
        nome_do_produto="cadeira",
        nome_da_empresa="Target Corporation",
        data_de_fabricacao="2021-02-18",
        data_de_validade="2025-09-17",
        numero_de_serie="CR25",
        instrucoes_de_armazenamento="empilhadas",
    )

    assert (
        str(result) == f"O produto {result.nome_do_produto}"
        f" fabricado em {result.data_de_fabricacao}"
        f" por {result.nome_da_empresa} com validade"
        f" até {result.data_de_validade}"
        f" precisa ser armazenado {result.instrucoes_de_armazenamento}."
    )
