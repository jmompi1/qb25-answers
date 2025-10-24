#!/usr/bin/env python3

#3.1
#I think samples 24, 27, 31, 62, and 63 derive from the wine strain, while the rest derive from the lab strain. 


# sample IDs
sample_ids = ["A01_62", "A01_39", "A01_63", "A01_35", "A01_31",
              "A01_27", "A01_24", "A01_23", "A01_11", "A01_09"]

# open the VCF file
input_vcf = "biallelic.vcf"
output_file = "gt_long.txt"
with open(input_vcf) as vcf, open(output_file, "w") as out:
    sample_ids = ["A01_62", "A01_39", "A01_63", "A01_35", "A01_31",
              "A01_27", "A01_24", "A01_23", "A01_11", "A01_09"]
    for line in vcf:
        if line.startswith("#"):
            continue
        elif line.startswith("#CHROM"):
            # Extract sample names from header
            fields = line.strip().split('\t')
            sample_names = fields[9:]
            out.write("Sample_ID\tChromosome\tPosition\tGenotype\n")
            continue
    
    # split the line into fields by tab, then
        chrom = fields[0]
        pos = fields[1]
        format_keys = fields[8].split(':')
        sample_values = fields[9:]


# Find GT index
        gt_index = format_keys.index("GT")

        for sample in sample_ids:
            sample_fields = sample_data.split(':')
            if len(sample_fields) <= gt_index:
                genotype = "NA"
            else:
                gt_raw = sample_fields[gt_index]
                # Normalize genotype to 0 or 1
                if gt_raw in ["0/0", "0|0"]:
                    genotype = "0"
                elif gt_raw in ["1/1", "1|1", "0/1", "1/0", "0|1", "1|0"]:
                    genotype = "1"
                else:
                    genotype = "NA"
            out.write(f"{sample}\t{chrom}\t{pos}\t{genotype}\n")
