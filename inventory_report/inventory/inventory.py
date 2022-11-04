import csv
import json

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(string_path, string_type):
        if string_path.endswith(".csv"):
            with open(string_path, encoding="utf-8") as file:
                result = csv.DictReader(file, delimiter=",", quotechar='"')
                result_products = []
                for row in result:
                    result_products.append(row)
        elif string_path.endswith(".json"):
            with open(string_path) as file:
                result_products = json.load(file)
        if string_type == "simples":
            return SimpleReport.generate(result_products)
        else:
            return CompleteReport.generate(result_products)
