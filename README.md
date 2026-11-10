
# Network-Based Drug Repurposing

## Research Question
Are Vitamin D drug targets located close to inflammation-associated
proteins in a human protein-protein interaction network?

## Dataset
NetMedPy VitaminD example dataset:
https://github.com/menicgiulia/NetMedPy

- PPI proteins: 18642
- PPI interactions: 354650
- Vitamin D targets: 15
- Inflammation genes: 608

## Method
Network-based proximity analysis using average minimum
shortest-path distance.

Statistical significance was evaluated using NetMedPy's
degree-matched null-model sampling with 100 iterations.

## Modification Beyond the Tutorial
We selected Inflammation from the available disease gene sets
and investigated its proximity to Vitamin D drug targets.
This changes the biological comparison from the tutorial example.

## Results and Interpretation

- Observed proximity: 0.4000
- Degree-matched random mean: 1.3440
- Z-score: -7.9226
- Empirical p-value: 0.0099
- Random iterations: 100

The observed proximity is lower than the degree-matched random
mean. The negative z-score indicates that Vitamin D targets are
closer to inflammation-associated proteins than expected under
the degree-matched random comparison.

This suggests a network-level association, not proof that
Vitamin D is an effective treatment for inflammation.

## Limitations
- Protein interaction networks are incomplete.
- Network proximity does not establish clinical effectiveness.
- The analysis uses 100 random iterations.
- The disease gene set may contain heterogeneous biological roles.

## How to Run
1. Install dependencies using requirements.txt.
2. Run python download_data.py to download datasets.
3. Open the analysis notebook in Google Colab or Jupyter.
4. Run the notebook cells in order.

## Files
- requirements.txt: Python dependencies
- download_data.py: Dataset download script
- proximity_results.csv: Statistical results
- proximity_results.png: Results graph
