import csv
import sys
from pathlib import Path


def read_keep_list(path: Path) -> list[str]:
    with path.open(encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def filter_columns(in_csv, keep_txt, out_csv):
    keep_list = read_keep_list(keep_txt)
    if not keep_list:
        sys.exit("Error: no column names found in the text file.")

    print("Keep list: ", keep_list)

    dialect = csv.excel()
    dialect.delimiter = ";"

    with in_csv.open(newline="", encoding="latin-1") as fin, out_csv.open(
        "w", newline="", encoding="utf-8"
    ) as fout:

        reader = csv.DictReader(fin, dialect=dialect)
        # Preserve original header order, but only for kept columns

        if reader.fieldnames is None:
            sys.exit("could not read header row from CSV file")

        out_fieldnames = [name for name in reader.fieldnames if name in keep_list]

        if not out_fieldnames:
            sys.exit("Error: none of the requested columns exist in the CSV.")

        writer = csv.DictWriter(fout, fieldnames=out_fieldnames, dialect=dialect)
        writer.writeheader()

        for row in reader:
            writer.writerow({k: row[k] for k in out_fieldnames})

    print(f"Filtered CSV written to {out_csv}")


if len(sys.argv) != 4:
    print("Uso: python script.py input.csv columns.txt output.csv")
    sys.exit(1)

filter_columns(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
