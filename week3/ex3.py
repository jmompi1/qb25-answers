#!/usr/bin/env python3

#3.1
#I think samples 24, 27, 31, 62, and 63 derive from the wine strain, while the rest derive from the lab strain. 


sample_ids = ["A01_62", "A01_39", "A01_63", "A01_35", "A01_31",
              "A01_27", "A01_24", "A01_23", "A01_11", "A01_09"]

input_vcf = "biallelic.vcf"
output_file = "gt_long.txt"


with open(input_vcf) as vcf, open(output_file, "w") as out:
    # Write header
    out.write("Sample_ID\tChromosome\tPosition\tGenotype\n")
    
    # Initialize sample mapping
    sample_to_index = {}
    
    for line in vcf:
        line = line.strip()
        
        # Skip meta-information lines
        if line.startswith("##"):
            continue
        
        # Header line with sample names
        if line.startswith("#CHROM"):
            fields = line.split("\t")
            sample_names = fields[9:]  # VCF sample columns
            sample_to_index = {name: i for i, name in enumerate(sample_names)}
            continue
        
        # Variant line
        fields = line.split("\t")
        chrom = fields[0]
        pos = fields[1]
        format_keys = fields[8].split(":")
        
        # Skip lines if GT field is missing
        if "GT" not in format_keys:
            continue
        gt_index = format_keys.index("GT")  # index of GT in FORMAT
        
        # Loop over target samples
        for sample in sample_ids:
            if sample not in sample_to_index:
                genotype = "NA"
            else:
                col_index = sample_to_index[sample]
                sample_data = fields[9 + col_index]
                sample_fields = sample_data.split(":")
                gt_raw = sample_fields[gt_index]

                # Normalize genotype robustly
                alleles = gt_raw.replace("|","/").split("/")
                if "." in alleles:
                    genotype = "NA"
                elif all(a == "0" for a in alleles):
                    genotype = "0"
                else:
                    genotype = "1"
            
            # Write to output
            out.write(f"{sample}\t{chrom}\t{pos}\t{genotype}\n")