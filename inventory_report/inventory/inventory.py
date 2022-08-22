import csv
import json
from xml.etree import ElementTree as ET

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def read_csv(path):
        with open(path) as file:
            dict_list = list(csv.DictReader(file))
        return dict_list

    def read_json(path):
        with open(path) as file:
            dict_list = json.loads(file.read())

        return dict_list

    def read_xml(path):
        tree = ET.parse(path)
        root = list(tree.getroot())
        dict_list = []
        info_dict = {}
        for index in range(len(root)):
            for info in root[index]:
                info_dict[info.tag] = info.text
            dict_list.append(info_dict)
            info_dict = {}
        return dict_list

    def read_file(path):
        if "csv" in path:
            return Inventory.read_csv(path)
        elif "json" in path:
            return Inventory.read_json(path)
        elif "xml" in path:
            return Inventory.read_xml(path)

    @classmethod
    def import_data(cls, path, type_report):
        if type_report == "simples":
            return SimpleReport.generate(Inventory.read_file(path))
        if type_report == "completo":
            return CompleteReport.generate(Inventory.read_file(path))
