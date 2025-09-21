bowtie2 -p 4 -x ../genomes/sacCer3 -U ~/Data/BYxRM/fastq/A01_01.fq.gz > A01_01.sam 
samtools sort -o A01_01.bam A01_01.sam
samtools index A01_01.bam
samtools idxstats A01_01.bam.bai > A01_01.idxstats

Each track in IGV depicts the amount of coverage (read depth?) for the respective sample and indicates SNPs as a color change (red, blue, orange, green) to depict the base change in compareison to the reference. The text file lists each region in the genome and which sequences are inherited from either the BY or RM parental strain.

