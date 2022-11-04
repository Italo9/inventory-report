import csv

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(string_path, string_type):
        with open(string_path, encoding="utf-8") as file:
            result = csv.DictReader(file, delimiter=",", quotechar='"')
            result_products = []
            for row in result:
                result_products.append(row)
            print(result_products)
        if string_type == "simples":
            return SimpleReport.generate(result_products)
        if string_type == "completo":
            return CompleteReport.generate(result_products)
