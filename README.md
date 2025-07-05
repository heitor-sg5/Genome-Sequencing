# Genome Sequencing Algorithms

This repository contains implementations of key algorithms used in genome assembly and sequencing analysis. The focus is on graph-based approaches, particularly de Bruijn and Overlap graphs, which reconstruct sequences from k-mer reads, similar to data generated in real-world DNA sequencing experiments.

---

## 🧬 What is Genome Sequencing?

Genome sequencing is the process of determining the complete DNA sequence of an organism — identifying the exact order of nucleotides (A, C, G, T) across its entire genome. However, modern sequencing technologies don’t read whole genomes in one pass. Instead, they output millions of short DNA fragments called reads, which are small, overlapping subsequences of the original genome.

These reads may be single k-mers or paired k-mers (two k-length fragments separated by a known distance), and they are typically unordered and may include sequencing errors.

To reconstruct the full genome, we rely on computational algorithms that can assemble these short reads by identifying overlaps, patterns, and paths through graph-based models like de Bruijn graphs or overlap graphs.

---

## 📁 Files in This Repository

- `generate_kmer_read_pairs.py`: Generates a list of single and paired k-mer reads d bases apart given a genome.
- `overlap_graph_hamiltonian_path.py`: Finds the Hamiltonian path of an overlap graph to reconstruct the genome.
- `debrujin_eulerian_path.py`: Finds the Eulerian path of a de Brujin graph to reconstruct the genome.
- `paired_debrujin_eulerian_path.py`: Finds the Eulerian path of a paired de Brujin graph to reconstruct the genome.
- `maximal_non-branching_debrujin_eulerian_path.py`: Finds all maximal non-branching Eulerian paths in a de Brujin graph.
- `kmers_output.txt`: An example input file with a list of single k-mer reads.
- `read_pairs_output.txt`: An example input file with paired k-mer reads d bases apart.
    
---

## ⚙️ How to Use

### 1. Prepare Input

There are three types of inputs depending on the algorithm:

- Enter a DNA sequence as a string text, if using `generate_kmer_read_pairs.py`. 

- You can use experimental or simulated data, using `generate_kmer_read_pairs.py`, as a text file with a list of k-mer reads of DNA (as shown in `kmers_output.txt`) for `overlap_graph_hamiltonian_path.py`, `debrujin_eulerian_path.py` and `maximal_non-branching_debrujin_eulerian_path.py`.

- Similarly, use experimental or simulated data (from `generate_kmer_read_pairs.py`) as a text file, but with a list of paired k-mer reads which are d bases apart (e.g. `read_pairs_output.txt`) for `paired_debrujin_eulerian_path.py`.

### 2. Run the Algorithms

Each script reads from the input file and prints:

- Two text files with simulated **single and paired k-mer reads** in lexicographical order, if using `generate_kmer_read_pairs.py`
- The reconstructed **genome sequence**
- A list of **maximal non-branching paths**, if using `maximal_non-branching_debrujin_eulerian_path.py`

---

#### Generate Simulated Single/Paired k-mer Reads

  bash
```generate_kmer_read_pairs.py```

#### Find Hamiltonian Path for Overlap Graph

  bash
```overlap_graph_hamiltonian_path.py```

#### Find Eulerian Path for de Brujin Graph 

  bash
```debrujin_eulerian_path.py```

#### Find Eulerian Path for Paired de Brujin Graph 

  bash
```paired_debrujin_eulerian_path.py```

#### Find All Maximal Non-branching Paths 

  bash
```maximal_non-branching_debrujin_eulerian_path.py```

You can change the default parameters k (k-mer read length) and d (gap between pairs) directly in each script's function call at the bottom.

---

## 🧠 Algorithm Overviews

### Single/Paired k-mer Generation

- Generates lists of single k-mers or paired k-mers (with a specified gap d) from a given genome.
- Simulates the type of fragmented sequencing data produced in real-world labs.
- Used as input for assembly algorithms such as de Bruijn or overlap graphs.

### Overlap Graph Hamiltonian Path

- Constructs an overlap graph where nodes are reads and edges represent suffix-prefix matches.
- Searches for a Hamiltonian path — a path visiting every read exactly once — to reconstruct the genome.
- Accurate for small datasets but computationally intensive (NP-hard).

### de Brujin Graph Eulerian Path

- Breaks reads into overlapping k-mers and builds a de Bruijn graph where edges represent k-mers and nodes represent (k–1)-mers.
- Finds an Eulerian path — a path that visits every edge exactly once — to reconstruct the genome efficiently.
- Scales well for large datasets and is robust to redundancy in reads.

### Paired de Brujin Graph Eulerian Path

- Builds a graph from paired k-mers separated by a known distance d.
- Encodes both k-mer overlap and relative distance between paired reads.
- Finds an Eulerian path through the paired de Bruijn graph to reconstruct genome sequences with long-range linkage.

### Maximal Non-branching Paths

- Identifies all non-branching paths in a de Bruijn graph that are maximal (cannot be extended without creating a branch).
- Useful for identifying contigs — continuous sequences in fragmented genome assemblies.
- Especially effective in separating linear regions from repetitive or ambiguous ones.

---

## 🧪 Example Output

- Paired k-mer Reads:
  
    (ACG,CCT) (AGG,CGG) (CCT,AGG) (CGG,CTA) (GAC,GCC) (GCC,AAG) (GGA,GGC) (GGC,TAA) (TAG,ACG)

- Paired de Brujin Eulerian Path:
  
    Genome: TAGGACGGCCTAAGG

---

## 👤 Author

Heitor Gelain do Nascimento
Email: heitorgelain@outlook.com
GitHub: @heitor-sg5

---

## 📚 References

Bioinformatics Algorithms: An Active Learning Approach (Chapter 3) by
Phillip Compeau & Pavel Pevzner
https://bioinformaticsalgorithms.com
