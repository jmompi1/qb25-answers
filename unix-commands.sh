#!/bin/bash


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

#3. #code: cut -f7 GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt | tail -n +2 | sort | uniq -c | sort -nr | head -n 3
    #output: 3288 Whole Blood
            #1132 Muscle - Skeletal
            #867 Lung
    
    #code: grep -c "RNA" GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
    #output: 20017
    #20017 lines have RNA

    #code: grep -vc "RNA" GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt
    #output: 2935
    #2935 lines do not have RNA

