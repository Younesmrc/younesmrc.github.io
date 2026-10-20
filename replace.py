
from pathlib import Path

root = Path(__file__).resolve().parent

total = 0

for file in root.rglob("*.html"):
    content = file.read_text(encoding="utf-8")

    count = content.count("—")

    if count:
        file.write_text(
            content.replace("—", "-"),
            encoding="utf-8"
        )

        total += count
        print(f"[OK] {file.relative_to(root)} : {count} remplacements")

print(f"\nTerminé ! {total} tirets remplacés.")
