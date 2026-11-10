# Network-Based Drug Repurposing Using NetMedPy

## 1. Research Question

Are Vitamin D target proteins located close to inflammation-associated proteins in a human protein-protein interaction (PPI) network?

This project applies network-based drug repurposing methods to investigate the proximity between Vitamin D targets and disease-associated proteins.

An additional comparison examines Vitamin D target proximity across 13 disease gene sets.

## 2. Data Source

The datasets were obtained from the official NetMedPy GitHub repository:

https://github.com/menicgiulia/NetMedPy

The following datasets from its VitaminD example resources were used:

| Dataset | Description |
|---|---|
| `ppi_network.pkl` | Human protein-protein interaction network |
| `vitd_targets_cpie.pkl` | Vitamin D target proteins |
| `disease_genes_merge.pkl` | Disease-associated gene sets |

### Dataset Statistics

- PPI network proteins: 18,642
- PPI interactions: 354,650
- Vitamin D targets present in network: 15
- Disease gene sets: 13
- Inflammation genes present in network: 608

## 3. Methodology

The project uses network proximity analysis based on average minimum shortest-path distance.

The observed proximity between Vitamin D targets and inflammation genes is compared with degree-matched random protein sets.

The analysis calculates:
- Observed proximity
- Randomised mean proximity
- Z-score
- Empirical p-value

The project also compares observed proximity across all 13 disease gene sets.

## 4. How to Run the Code

### Requirements

Python 3 and the packages listed in `requirements.txt`.

### Step 1: Clone the repository

```bash
git clone https://github.com/saisaradaR/Network-Based-Drug-Repurposing.git
cd Network-Based-Drug-Repurposing
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Download the datasets

```bash
python download_data.py
```

This downloads the required datasets into the `data` folder.

### Step 4: Run the notebook

Open `Network_Based_Drug_Repurposing.ipynb` using Google Colab or Jupyter Notebook.

Run the cells in order to reproduce the analysis and generate the results.

## 5. Results

### Vitamin D and Inflammation

| Measurement | Result |
|---|---:|
| Observed proximity | 0.4000 |
| Degree-matched random mean | 1.3440 |
| Z-score | -7.9226 |
| Empirical p-value | 0.0099 |
| Random iterations | 100 |

The observed proximity is lower than the degree-matched random mean, suggesting that Vitamin D targets are closer to inflammation-associated proteins than expected under this random comparison.

### Comparison Across Diseases

Inflammation showed the lowest observed proximity (0.4000) among the 13 disease gene sets, followed by Asthma (0.5333) and CAD (0.6000).

This comparison is based on observed proximity values; statistical significance was not separately tested for every disease.

## 6. Limitations

- PPI networks may not contain all biological interactions.
- Network proximity does not prove drug effectiveness.
- The analysis uses 100 random iterations.
- Further experimental and clinical validation is required.

## 7. Repository Files

- `Network_Based_Drug_Repurposing.ipynb` – Analysis notebook.
- `README.md` – Project documentation.
- `requirements.txt` – Python dependencies.
- `download_data.py` – Dataset download script.
- `proximity_results.csv` – Main statistical results.
- `proximity_results.png` – Proximity distribution graph.
- `all_disease_comparison.csv` – Disease comparison results.
- `all_disease_comparison.png` – Disease comparison graph.

## 8. Reference

Guney, E., Menche, J., Vidal, M., & Barabási, A.-L. (2016). Network-based in silico drug efficacy screening. *Nature Communications*, 7, 10331.

https://doi.org/10.1038/ncomms10331
