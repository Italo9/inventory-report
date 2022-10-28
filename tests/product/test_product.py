from inventory_report.inventory.product import Product


def test_cria_produto():
    result = Product(
        1,
        "t",
        "t",
        "t",
        "t",
        "t",
        "t",
    )

    assert result.id == 1
    assert result.nome_do_produto == "t"
    assert result.nome_da_empresa == "t"
    assert result.data_de_fabricacao == "t"
    assert result.data_de_validade == "t"
    assert result.numero_de_serie == "t"
    assert result.instrucoes_de_armazenamento == "t"
