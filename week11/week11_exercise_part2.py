#!/usr/bin/env python3
#used chatgpt for help

#Step 2.1
#Next, you’re going to generate your own de Bruijn graph using a provided set of reads. Copy the list of reads below into your code:

reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT',
         'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

k = 3
edges = set()

# Build edges: store as tuples (kmer1, kmer2)
for read in reads:
    for i in range(len(read) - k):
        kmer1 = read[i : i+k]
        kmer2 = read[i+1 : i+1+k]
        edges.add((kmer1, kmer2))

# Write edges to text file
with open("debruijn_edges.txt", "w") as out:
    for a, b in sorted(edges):
        out.write(f"{a} -> {b}\n")

# Write Graphviz DOT file
with open("debruijn_graph.dot", "w") as dot:
    dot.write("digraph debruijn {\n")
    for a, b in sorted(edges):
        dot.write(f'    "{a}" -> "{b}";\n')
    dot.write("}\n")

print("Created: debruijn_edges.txt and debruijn_graph.dot")
