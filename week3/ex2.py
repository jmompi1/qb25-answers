#!/usr/bin/env python3

#for line in open("biallelic.vcf") :
#    if line.startswith('#'):
#       continue
#    fields = line.rstrip('\n').split('\t')

#    chrom = fields[0]
#    pos = fields[1]
#    ref = fields[3]
#    alt = fields[4]
#   qual = fields[5]
#    info = fields[7]
#   print (f"{chrom}:{pos} {ref}>{alt} QUAL={qual}")


#input_vcf = "biallelic.vcf"
#with open("biallelic.vcf") as vcf, open(output_file, "w") as out:
    #out.write("Variant_ID\tAllele_Frequency\n")

    #for line in open("biallelic.vcf"):
      #  if line.startswith("#"):
       #     continue 
       # fields = line.strip().split('\t')
       # info_field = fields[7]  

      
       # info_dict = dict(item.split('=') for item in info_field.split(';') if '=' in item)

        
       # af = info_dict.get("AF", "NA") 
        #print(f"{fields[0]}:{fields[1]}\t{af}\n")
    


input_vcf = "biallelic.vcf"
output_file = "AF.tsv"

with open(input_vcf) as vcf, open(output_file, "w") as out:
    out.write("variant_id\tAllele_Frequency\n")  # header with tab separator
    for line in vcf:
        if line.startswith("#"):
            continue
        fields = line.strip().split('\t')
        chrom = fields[0]
        pos = fields[1]
        info_field = fields[7]

        # Parse INFO field
        info_dict = dict(item.split('=') for item in info_field.split(';') if '=' in item)
        af = info_dict.get("AF", "NA")

        # Write as tab-separated values
        variant_id = f"{chrom}:{pos}"
        out.write(f"{variant_id}\t{af}\n")