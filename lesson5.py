"""Lesson 5: safe file handling and parsing exercises."""
import json
import re
from pathlib import Path

def write_lines(path, lines):
    with Path(path).open("w", encoding="utf-8") as stream:
        for line in lines:
            if not line: break
            stream.write(line + "\n")

def line_word_counts(path):
    with Path(path).open(encoding="utf-8") as stream:
        return [len(line.split()) for line in stream]

def salary_report(path):
    records = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        name, wage = line.rsplit(maxsplit=1)
        records.append((name,float(wage)))
    return {"below_20000":[name for name,wage in records if wage < 20000],
            "average":sum(wage for _,wage in records)/len(records) if records else 0}

NUMBERS = {"One":"Один","Two":"Два","Three":"Три","Four":"Четыре"}
def translate_numerals(text):
    return "\n".join(NUMBERS.get(line.split(maxsplit=1)[0], line.split(maxsplit=1)[0]) +
        (" " + line.split(maxsplit=1)[1] if len(line.split(maxsplit=1)) > 1 else "")
        for line in text.splitlines())

def sum_numbers_in_file(path):
    return sum(map(float, Path(path).read_text(encoding="utf-8").split()))

def subject_hours(lines):
    result = {}
    for line in lines:
        name, _, rest = line.partition(":")
        if not _: raise ValueError("Expected ':' in subject record")
        result[name.strip()] = sum(map(int,re.findall(r"\d+",rest)))
    return result

def company_profits(lines):
    profits = {}
    for line in lines:
        if not line.strip(): continue
        name, kind, revenue, costs = line.split()
        profits[name] = float(revenue)-float(costs)
    profitable = [p for p in profits.values() if p > 0]
    return [profits, {"average_profit":sum(profitable)/len(profitable) if profitable else 0}]

def save_profits_json(path, report):
    Path(path).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
