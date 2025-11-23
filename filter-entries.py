import csv
import sys
from pathlib import Path


def drop_empty_rows(in_csv: Path, out_csv: Path) -> None:
    dialect = csv.excel()
    dialect.delimiter = ";"

    with in_csv.open(newline="", encoding="utf-8") as fin, out_csv.open(
        "w", newline="", encoding="utf-8"
    ) as fout:

        reader = csv.DictReader(fin, dialect=dialect)

        if reader.fieldnames is None:
            sys.exit("could not read header row from CSV file")

        writer = csv.DictWriter(fout, fieldnames=reader.fieldnames, dialect=dialect)
        writer.writeheader()

        kept = 0
        for row in reader:
            # keep only if every field has non-empty content
            if all(v.strip() for v in row.values()):
                writer.writerow(row)
                kept += 1

    print(f"Done. Kept {kept} complete rows -> {out_csv}")
    return


if len(sys.argv) != 3:
    print("Uso: python script.py input.csv output.csv")
    sys.exit(1)

drop_empty_rows(Path(sys.argv[1]), Path(sys.argv[2]))
