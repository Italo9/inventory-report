from inventory_report.inventory.product import Product


def test_cria_produto():
    result = Product(
        1,
        "cadeira",
        "Target Corporation",
        "2021-02-18",
        "2025-09-17",
        "CR25",
        "empilhadas",
    )

    assert result.id == 1
    assert result.nome_do_produto == "cadeira"
    assert result.nome_da_empresa == "Target Corporation"
    assert result.data_de_fabricacao == "2021-02-18"
    assert result.data_de_validade == "2025-09-17"
    assert result.numero_de_serie == "CR25"
    assert result.instrucoes_de_armazenamento == "empilhadas"
