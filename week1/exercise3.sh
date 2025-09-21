#!/bin/bash
#3
mv ~/Downloads/nhlf.bed .
mv ~/Downloads/nhek.bed .

#Subset regions classified as 1_Active and 12_Repressed in to separate files
grep 1_Active nhek.bed > nhek-active.bed
grep 1_Active nhlf.bed > nhlf-active.bed
grep 12_Repressed nhek.bed > nhek-repressed.bed
grep 12_Repressed nhlf.bed > nhlf-repressed.bed

#Construct a bedtools command to test where there is any overlap between 1_Active and 12_Repressed in a given condition (aka mutually exclusive)
bedtools intersect -u -a nhek-active.bed -b nhek-repressed.bed | wc -l

#Construct two bedtools intersect [OPTIONS] -a nhek-active.bed -b nhlf-active.bed commands, one to find regions that are active in NHEK and NHLF, and one to find regions that are active in NHEK but not active in NHLF

bedtools intersect -u -a nhek-active.bed -b nhlf-active.bed | wc -l
#There are 11608 regions of overlap.

bedtools intersect -v -a nhek-active.bed -b nhlf-active.bed | wc -l 
#There are 2405 regions active in NHEK and not NHLF

bedtools intersect -v -a nhlf-active.bed -b nhek-active.bed | wc -l 
#There are 3033 regions active in NHLF and not NHEK

#Do these two numbers add up to the original number of lines in nhek-active.bed?
#Yes


#Construct three bedtools intersect commands to see the effect of using the arguments -f 1, -F 1, and -f 1 -F 1 when comparing -a nhek-active.bed -b nhlf-active.bed
bedtools intersect -f 1 -a nhek-active.bed -b nhlf-active.bed | head -n 1
#chr1	25558413	25559413	1_Active_Promoter	0	.	25558413	25559413

bedtools intersect -F 1 -a nhek-active.bed -b nhlf-active.bed | head -n 1
#chr1	19923013	19924213	1_Active_Promoter	0	.	19922613	19924613

bedtools intersect -f 1 -F 1 -a nhek-active.bed -b nhlf-active.bed | head -n 1
#chr1	1051137	1051537	1_Active_Promoter	0	.	1051137	1051537

#Construct three bedtools intersect commands to identify the following types of regions. Use UCSC Genome Browser to save one PDF image for each of the three types of regions. Describe the chromatin state across all nine conditions.

#Active in NHEK, Active in NHLF
bedtools intersect -a nhek-active.bed -b nhlf-active.bed | head -n 1
#chr1	19923013	19924213	1_Active_Promoter	0	.	19922613	19924613
#consistently and strongly active throughout

#Active in NHEK, Repressed in NHLF
bedtools intersect -a nhek-active.bed -b nhlf-repressed.bed | head -n 1
#chr1	1981140	1981540	1_Active_Promoter	0	.	1981140	1981540
#there is a combination of strongly active and repressed/poised 

#Repressed in NHEK, Repressed in NHLF
bedtools intersect -a nhek-repressed.bed -b nhlf-repressed.bed | head -n 1
#chr1	11537413	11538213	12_Repressed	0	.	11534013	11538613
# seem inactive/repressed throughout

