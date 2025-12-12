#!/usr/bin/env python3
#used chatgpt for help

import numpy as np
from scipy.stats import poisson, norm


# Parameters
genome_size = 1_000_000  # 1 Mbp
read_length = 100        # 100 bp reads
coverage = 3             # 3x coverage

# Step 1: Calculate number of reads needed
num_reads = int((genome_size * coverage) / read_length)
print(f"Simulating {num_reads} reads for {coverage}x coverage...")

# Step 2: Initialize coverage array
genome_coverage = np.zeros(genome_size, dtype=int)

# Step 3: Simulate reads and update coverage
for _ in range(num_reads):
    start_pos = np.random.randint(0, genome_size - read_length + 1)
    end_pos = start_pos + read_length
    genome_coverage[start_pos:end_pos] += 1

# Step 4: Save coverage to file
np.savetxt("genome_coverage.txt", genome_coverage, fmt='%d')
print("Coverage saved to genome_coverage.txt")

# Step 5: Compute Poisson and Normal estimates
max_coverage = genome_coverage.max()
xs = np.arange(0, max_coverage + 1)

# Poisson PMF
poisson_estimates = poisson.pmf(xs, mu=coverage)

# Normal PDF (density between points)
normal_estimates = norm.pdf(xs, loc=coverage, scale=np.sqrt(coverage))

#Save distributions
np.savetxt("poisson_estimates.txt", np.column_stack((xs, poisson_estimates)))
np.savetxt("normal_estimates.txt", np.column_stack((xs, normal_estimates)))

print("Poisson and normal estimates saved.")