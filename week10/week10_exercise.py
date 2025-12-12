#!/usr/bin/env python3

import sys
from fasta import readFASTA


# Step 1.1: Read scoring matrix
def read_scoring_matrix(matrix_file):
    sigma = {}
    with open(matrix_file) as f:
        headers = f.readline().split()
        for line in f:
            parts = line.split()
            row_char = parts[0]
            scores = parts[1:]
            for col_char, score in zip(headers, scores):
                sigma[(row_char, col_char)] = int(score)
    return sigma


# Step 1.2: Initialize matrices
def initialize_matrices(seq1, seq2, gap_penalty):
    m = len(seq1)
    n = len(seq2)
    F = [[0]*(n+1) for _ in range(m+1)]
    traceback = [['']*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        F[i][0] = gap_penalty * i
        traceback[i][0] = 'U'  # Up
    for j in range(1, n+1):
        F[0][j] = gap_penalty * j
        traceback[0][j] = 'L'  # Left

    return F, traceback

# Step 1.3: Populate matrices
def populate_matrices(seq1, seq2, sigma, gap_penalty, F, traceback):
    m = len(seq1)
    n = len(seq2)
    for i in range(1, m+1):
        for j in range(1, n+1):
            diag_score = F[i-1][j-1] + sigma[(seq1[i-1], seq2[j-1])]
            up_score = F[i-1][j] + gap_penalty
            left_score = F[i][j-1] + gap_penalty

            max_score = max(diag_score, up_score, left_score)
            F[i][j] = max_score

            # Tie-breaking: Diagonal > Up > Left
            if max_score == diag_score:
                traceback[i][j] = 'D'
            elif max_score == up_score:
                traceback[i][j] = 'U'
            else:
                traceback[i][j] = 'L'
    return F, traceback

# Step 1.4: Traceback
def traceback_alignment(seq1, seq2, traceback):
    i = len(seq1)
    j = len(seq2)
    aligned_seq1 = []
    aligned_seq2 = []

    while i > 0 or j > 0:
        if i > 0 and j > 0 and traceback[i][j] == 'D':
            aligned_seq1.append(seq1[i-1])
            aligned_seq2.append(seq2[j-1])
            i -= 1
            j -= 1
        elif i > 0 and traceback[i][j] == 'U':
            aligned_seq1.append(seq1[i-1])
            aligned_seq2.append('-')
            i -= 1
        elif j > 0 and traceback[i][j] == 'L':
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j-1])
            j -= 1
        else:
            if i > 0:
                aligned_seq1.append(seq1[i-1])
                aligned_seq2.append('-')
                i -= 1
            elif j > 0:
                aligned_seq1.append('-')
                aligned_seq2.append(seq2[j-1])
                j -= 1

    aligned_seq1.reverse()
    aligned_seq2.reverse()
    return ''.join(aligned_seq1), ''.join(aligned_seq2)

# Step 1.5: Write alignment and stats
def write_alignment(output_file, seq1_id, seq2_id, aligned_seq1, aligned_seq2):
    with open(output_file, 'w') as f:
        f.write(f">{seq1_id}\n{aligned_seq1}\n")
        f.write(f">{seq2_id}\n{aligned_seq2}\n")

def compute_statistics(aligned_seq1, aligned_seq2, F, len_seq1, len_seq2):
    num_gaps_seq1 = aligned_seq1.count('-')
    num_gaps_seq2 = aligned_seq2.count('-')
    matches = sum(1 for a, b in zip(aligned_seq1, aligned_seq2) if a == b)
    length = len(aligned_seq1)
    percent_identity_seq1 = (matches / length) * 100
    percent_identity_seq2 = (matches / length) * 100
    alignment_score = F[len_seq1][len_seq2]
    return num_gaps_seq1, num_gaps_seq2, percent_identity_seq1, percent_identity_seq2, alignment_score

# Main function
if __name__ == "__main__":
    # Command-line arguments
    fasta_file = sys.argv[1]
    matrix_file = sys.argv[2]
    gap_penalty = int(sys.argv[3])
    output_file = sys.argv[4]

    # 1. Read sequences first
    input_sequences = readFASTA(open(fasta_file))
    seq1_id, seq1 = input_sequences[0]
    seq2_id, seq2 = input_sequences[1]

    # 2. Read scoring matrix
    sigma = read_scoring_matrix(matrix_file)

    # 3. Initialize matrices
    F, traceback_mat = initialize_matrices(seq1, seq2, gap_penalty)

    # 4. Populate matrices
    F, traceback_mat = populate_matrices(seq1, seq2, sigma, gap_penalty, F, traceback_mat)

    # 5. Traceback alignment
    aligned_seq1, aligned_seq2 = traceback_alignment(seq1, seq2, traceback_mat)

    # 6. Write alignment to file
    write_alignment(output_file, seq1_id, seq2_id, aligned_seq1, aligned_seq2)

    # 7. Compute and print statistics
    num_gaps_seq1, num_gaps_seq2, pid1, pid2, score = compute_statistics(
        aligned_seq1, aligned_seq2, F, len(seq1), len(seq2)
    )

    print("Number of gaps in seq1:", num_gaps_seq1)
    print("Number of gaps in seq2:", num_gaps_seq2)
    print("Percent identity seq1:", pid1)
    print("Percent identity seq2:", pid2)
    print("Alignment score:", score)