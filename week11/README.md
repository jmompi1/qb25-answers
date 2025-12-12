In your README.md for this assignment, answer the following question (show your work):
How many 100bp reads are needed to sequence a 1Mbp genome to 3x coverage?
#There would be 30,000 100bp reads required. 



Step 1.4
Using your results from Step 1.3, answer the following questions in your README.md:

In your simulation, how much of the genome has not been sequenced (has 0x coverage)?
How well does this match Poisson expectations? How well does the normal distribution fit the data?
#A little less than 20% of the genome has not een sequenced. The distriution matches more of a Poisson than normal. For the normal distribution, there is a singlular peak at 3x coverage, while the actual data, the most common level of coverage was both 2x and 3x, which was more representated in the Poisson curve.

1.5
In your README.md, answer the following questions:
In your simulation, how much of the genome has not been sequenced (has 0x coverage)?
How well does this match Poisson expectations? How well does the normal distribution fit the data?
#Still, less than 20% of the genome has 0x coverage. The data don't ft the normal or Poisson distributions, where the coverage is generally expected to be higher (higher frequency of higher coverage). 

1.6
In your README.md, answer the following questions:
In your simulation, how much of the genome has not been sequenced (has 0x coverage)?
How well does this match Poisson expectations? How well does the normal distribution fit the data?
#The normal and poisson distributions show zero read coverage as across the board, since they're both straight horizontal lines at zero. 

Step 2.5
Assume that the maximum number of occurrences of any 3-mer in the actual genome is five. Using your graph from Step 2.4, write one possible genome sequence that would produce these reads. Record your answer in your README.md.
#TTCATTCTTATTGATTT

Step 2.6
In a few sentences, what would it take to accurately reconstruct the sequence of the genome? Record your answer in your README.md.
#One would need longer kmers, to get a higher amount of coverage. They should be long enough so that reads containing the same sequences can be mapped to the appropriate locations in the genome. 
