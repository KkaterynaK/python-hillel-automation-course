import csv
import json
import logging
import os
from pathlib import Path
import xml.etree.ElementTree as ET

second_name = "Kuchma"


IDEAS_DIR = None
for parent in [Path(__file__).resolve().parent, *Path(__file__).resolve().parents]:
    if (parent / "ideas_for_test").is_dir():
        IDEAS_DIR = parent / "ideas_for_test"
        break

CSV_DIR = IDEAS_DIR / "work_with_csv"
JSON_DIR = IDEAS_DIR / "work_with_json"
XML_DIR = IDEAS_DIR / "work_with_xml"


# ==========================================
# Завдання 1: порівняти два CSV і прибрати дублікати
# ==========================================

file1 = CSV_DIR / "r-m-c.csv"
file2 = CSV_DIR / "random-michaels.csv"


def read_csv(path):
    with open(path, encoding="utf-8", errors="ignore", newline="") as f:
        delimiter = ";" if ";" in f.readline() else ","
        f.seek(0)
        rows = list(csv.reader(f, delimiter=delimiter))
    return rows


rows1 = read_csv(file1)
rows2 = read_csv(file2)

header = rows1[0]
all_rows = rows1[1:] + rows2[1:]

result = []
seen = set()
for row in all_rows:
    contact_id = row[0]
    if contact_id not in seen:
        seen.add(contact_id)
        result.append(row)

output_csv = CSV_DIR / f"result_{second_name}.csv"
with open(output_csv, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(result)

print("Завдання 1:")
print("  Всього рядків:", len(all_rows))
print("  Після видалення дублікатів:", len(result))
print("  Дублікатів прибрано:", len(all_rows) - len(result))
print("  Результат записано у:", output_csv.name)


# ==========================================
# Завдання 2: провалідувати всі json, помилки в лог-файл (рівень ERROR)
# ==========================================

log_file = JSON_DIR / f"json__{second_name}.log"

json_logger = logging.getLogger("json_logger")
json_logger.setLevel(logging.ERROR)
json_logger.propagate = False
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
json_logger.addHandler(file_handler)

print("\nЗавдання 2:")
for name in os.listdir(JSON_DIR):
    if name.endswith(".json"):
        with open(JSON_DIR / name, encoding="utf-8") as f:
            try:
                json.load(f)
                print(f"  {name} - валідний")
            except json.JSONDecodeError as e:
                print(f"  {name} - НЕвалідний")
                json_logger.error(f"{name}: {e}")
print("  Помилки записано у:", log_file.name)


# ==========================================
# Завдання 3: пошук по group/number, вивід timingExbytes/incoming (рівень INFO у консоль)
# ==========================================

xml_logger = logging.getLogger("xml_logger")
xml_logger.setLevel(logging.INFO)
xml_logger.propagate = False
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
xml_logger.addHandler(console_handler)

tree = ET.parse(XML_DIR / "groups.xml")
root = tree.getroot()


def find_incoming(number):
    for group in root.findall("group"):
        if group.find("number").text == str(number):
            timing = group.find("timingExbytes")
            if timing is not None and timing.find("incoming") is not None:
                value = timing.find("incoming").text
                xml_logger.info(f"group {number}: incoming = {value}")
                return value
            xml_logger.info(f"group {number}: немає timingExbytes/incoming")
            return None
    xml_logger.info(f"group {number} не знайдено")
    return None


print("\nЗавдання 3:")
find_incoming(0)
find_incoming(2)
find_incoming(1)
find_incoming(5)
find_incoming(99)
