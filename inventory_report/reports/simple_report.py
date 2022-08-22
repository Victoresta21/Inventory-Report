from datetime import datetime
import statistics


class SimpleReport:
    def generate(data):
        fact_date = sorted(data, key=lambda d: d["data_de_fabricacao"])[0][
            "data_de_fabricacao"
        ]
        val_date = sorted(data, key=lambda d: d["data_de_validade"])
        date_now = datetime.today().strftime("%Y-%m-%d")
        max_product = statistics.mode(item["nome_da_empresa"] for item in data)
        next_date_val = val_date[0]["data_de_validade"]

        for item in val_date:
            if item["data_de_validade"] < date_now:
                val_date.remove(item)
        return (
            f"Data de fabricação mais antiga: {fact_date}\n"
            f"Data de validade mais próxima: {next_date_val}\n"
            f"Empresa com mais produtos: {max_product}"
        )
