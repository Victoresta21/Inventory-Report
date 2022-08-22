from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def get_company_stock(stock):
        return {
            company["nome_da_empresa"]: [
                product
                for product in stock
                if product["nome_da_empresa"] == company["nome_da_empresa"]
            ]
            for company in stock
        }

    def create_company_report(stock):
        report = "Produtos estocados por empresa:\n"
        for company, products in stock.items():
            report += f"- {company}: {len(products)}\n"
        return report

    @classmethod
    def generate(self, list):
        company_stock = self.get_company_stock(list)
        company_report = self.create_company_report(company_stock)
        simple_report = super().generate(list)
        complete_report = simple_report + "\n" + company_report

        return complete_report
