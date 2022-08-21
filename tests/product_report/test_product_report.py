from inventory_report.inventory.product import Product
from ..factories.product_factory import ProductFactory


def test_relatorio_produto():
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
    phrase = (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
    assert str(product) == phrase
