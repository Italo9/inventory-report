import csv
import json

import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def auxiliary(cls, string_path):
        if string_path.endswith(".csv"):
            with open(string_path, encoding="utf-8") as file:
                result = csv.DictReader(file, delimiter=",", quotechar='"')
                result_products = []
                for row in result:
                    result_products.append(row)
            return result_products
        elif string_path.endswith(".json"):
            with open(string_path) as file:
                result_products = json.load(file)
            return result_products
        elif string_path.endswith(".xml"):
            with open(string_path, "r", encoding="utf-8") as file:
                result_products = xmltodict.parse(file.read())["dataset"][
                    "record"
                ]
            return result_products

    @staticmethod
    def import_data(string_path, string_type):
        result_products = Inventory.auxiliary(string_path)
        if string_type == "simples":
            return SimpleReport.generate(result_products)
        else:
            return CompleteReport.generate(result_products)
