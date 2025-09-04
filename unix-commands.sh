#1.
#code: wc ce11_genes.bed
#output: 53935 323610 2200094
#There are 53935 lines

#code: cut -f 1 ce11_genes.bed | sort | uniq -c
 #There are the following number of features per each chromosome:
#5460 chrI
#6299 chrII
#4849 chrIII
#21418 chrIV
#12 chrM
#9057 chrV
#6840 chrX

#cut -f 6 ce11_genes.bed | sort | uniq -c
#output: 26626 -
        #27309 +
#there are 26626 features in the negative strands and 27309 features in the positive strands






