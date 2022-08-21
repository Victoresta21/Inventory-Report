from inventory_report.inventory.product import Product
from ..factories.product_factory import ProductFactory


def test_cria_produto():
    fake_product = ProductFactory()
    product = Product(
        fake_product.id,
        fake_product.nome_do_produto,
        fake_product.nome_da_empresa,
        fake_product.data_de_fabricacao,
        fake_product.data_de_validade,
        fake_product.numero_de_serie,
        fake_product.instrucoes_de_armazenamento,
    )

    assert product.id == fake_product.id
    assert product.nome_do_produto == fake_product.nome_do_produto
    assert product.nome_da_empresa == fake_product.nome_da_empresa
    assert product.data_de_fabricacao == fake_product.data_de_fabricacao
    assert product.data_de_validade == fake_product.data_de_validade
    assert product.numero_de_serie == fake_product.numero_de_serie
    assert (
        product.instrucoes_de_armazenamento
        == fake_product.instrucoes_de_armazenamento
    )
