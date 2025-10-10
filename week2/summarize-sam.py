#!/usr/bin/env python3
import sys

sam_file: TextIOWrapper[_WrappedBuffer] = open(file = sys.argv[1])
align_counts: dict[Any, Any] = {}
sorted_dict: dict[Any, Any] = {}
for line in sam_file:
    if line.startswith ("a"):
        continue
    fields: list[str] = line.strip().split(sep = "\t")
    RNAME: str = fields[2]
    if RNAME not in align_counts:
        align_counts[RNAME]= 1
    else:
        align_counts[RNAME]+=1
    for x in fields:
        if x.startswith ("NM:i"):
            data_split: list[str] = x.strip().split(sep=":")
            number = int(x=data_split[2])
            if number not in sorted_dict:
                sorted_dict[number] = 1
            else:
                sorted_dict[number] += 1

for line in sorted(sorted_dict.keys()):
    print(line, sorted_dict[line])

for line in align_counts.keys():
    print(line, align_counts[line])

