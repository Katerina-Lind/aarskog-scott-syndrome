from pathlib import Path
import csv
import re
import sys

BUCKET = "katerina-lind-storage"

input_file = Path("metadata/fastq_files.txt")
output_file = Path("metadata/samplesheet.sarek.csv")

pattern = re.compile(
    r"raw/(?P<sample>M\d+)/"
    r"(?P=sample)_(?P<lane>L\d+)_(?P<read>R[12])_(?P<chunk>\d+)\.(?:fastq|fq)\.gz$"
)

pairs = {}

with input_file.open() as f:
    for line in f:
        key = line.strip()

        if not key:
            continue

        match = pattern.search(key)

        if not match:
            print(f"WARNING: could not parse: {key}")
            continue

        sample = match.group("sample")
        lane = match.group("lane")
        read = match.group("read")
        chunk = match.group("chunk")

        pair_key = (sample, lane, chunk)

        pairs.setdefault(pair_key, {})
        pairs[pair_key][read] = f"s3://{BUCKET}/{key}"

errors = []

for pair_key, reads in pairs.items():
    if "R1" not in reads or "R2" not in reads:
        errors.append((pair_key, reads))

if errors:
    print("\nERROR: unpaired FASTQ files found:\n")

    for pair_key, reads in errors:
        print(pair_key, reads)

    sys.exit(1)

with output_file.open("w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "patient",
        "sample",
        "lane",
        "fastq_1",
        "fastq_2"
    ])

    for (sample, lane, chunk), reads in sorted(pairs.items()):
        writer.writerow([
            sample,
            sample,
            f"{lane}_{chunk}",
            reads["R1"],
            reads["R2"]
        ])

print(f"Wrote {len(pairs)} FASTQ pairs to {output_file}")