import os
import urllib.request

os.makedirs("data", exist_ok=True)

base = "https://raw.githubusercontent.com/menicgiulia/NetMedPy/master/examples/VitaminD/data/input/"

files = {
    "ppi_network.pkl": base + "ppi/ppi_network.pkl",
    "vitd_targets_cpie.pkl": base + "drug_targets/vitd_targets_cpie.pkl",
    "disease_genes_merge.pkl": base + "disease_genes/disease_genes_merge.pkl"
}

for filename, url in files.items():
    urllib.request.urlretrieve(url, f"data/{filename}")
    print("Downloaded:", filename)

print("All datasets downloaded successfully!")
