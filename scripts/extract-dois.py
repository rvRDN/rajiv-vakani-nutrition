import json, re, sys
path = sys.argv[1]
dois = set()
for line in open(path, encoding="utf-8"):
    for m in re.findall(r"10\.\d{4,9}/[^\s\"'<>)\]]+", line):
        dois.add(m.rstrip(".,;"))
for d in sorted(dois):
    print(d)
print("--- count", len(dois))
