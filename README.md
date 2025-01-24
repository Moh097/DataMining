```markdown
# Data Mining Assignment at AlHussein Technical University (HTU)

This repository contains code for a **Data Mining** assignment at **AlHussein Technical University (HTU)**.  
It demonstrates various concepts in data mining, including:

- **Data Preprocessing & Clustering**  
- **Dimensionality Reduction** (PCA, LDA)  
- **Text Analysis with TF-IDF**  
- **Graph Representation** using NetworkX

---

## 1. Clustering Module

**File**: `modules/clustering.py`

### Overview
- **Preprocessing**:  
  - Scales numeric features (e.g., project counts).  
  - Encodes categorical features (certifications, extracurricular activities, career interests).  
  - Extracts programming languages per student.

- **Dimensionality Reduction**:  
  - **PCA** – reduces features to 2 principal components.  
  - **LDA** – projects features into 1 or 2 dimensions if there are enough classes.

- **Clustering**:  
  - **KMeans**  
  - **DBSCAN**  
  - **KMedoids**  
  - **Agglomerative Clustering**

- **Evaluation**:  
  - **AMI** (Adjusted Mutual Information)  
  - **ARI** (Adjusted Rand Index)  
  - **Silhouette Score**

- **Visualization**:  
  - Compares clustering results across PCA and LDA using bar plots.

### Usage Example

```python
from modules.clustering import Clustering
import pandas as pd

# df should contain columns ["Name", "Bio", "Cluster", "Project Count", ...]
analyzer = Clustering(df)
results = analyzer.run_analysis()
analyzer.visualize_comparison()
```

---

## 2. TF-IDF Module

**File**: `modules/tfidf_moh.py`

### Overview
- Converts text (e.g., user bios) into TF-IDF vectors.
- Computes **cosine similarity** between each query and the bios corpus to rank documents.

### Usage Example

```python
from modules.tfidf_moh import TfIdf_moh

tfidf_analyzer = TfIdf_moh()
tfidf_analyzer.vectorize(["Alice is a Data Scientist", "Bob is a Software Engineer"])

queries = ["Data", "Software"]
ranked_results = tfidf_analyzer.rank_queries(queries)
print(ranked_results)
```

---

## 3. Graph Module

Below is an example `Graph`-like class that uses **NetworkX** for creating and visualizing normal or directed graphs. This variant has `_m` appended to variables/methods, as requested.

**File**: `modules/graph_m.py` (example name)

```python
import networkx as nx
import matplotlib.pyplot as plt

class Graph_m:

    def __init__(self, kind_m="Normal"):
        if kind_m == "Normal":
            self.graph_m = nx.Graph()
        elif kind_m == "Directed":
            self.graph_m = nx.DiGraph()
        self.central_m = None
        self.labels_m = {}

    def create_graph_m(self, student_m, languages_related_m, all_languages_m):
        self.central_m = student_m
        self.graph_m.add_node(student_m)
        for language_m in all_languages_m:
            self.graph_m.add_node(language_m)

        for language_m in languages_related_m:
            self.graph_m.add_edge(student_m, language_m)

    def create_graph_projects_m(self, cert_m, cert_student_projects_m):
        self.graph_m.add_node(cert_m)

        if cert_m in cert_student_projects_m:
            related_students_m = cert_student_projects_m[cert_m]

            for student_m, project_count_weights_m in related_students_m.items():
                self.graph_m.add_edge(cert_m, student_m, weight=project_count_weights_m)

    def draw_graph_m(self, title_m="graph visualization"):
        if not self.graph_m:
            print("no graph to visualize")
            return

        plt.figure(figsize=(8, 6))
        pos_m = nx.spring_layout(self.graph_m)

        nx.draw(
            self.graph_m, pos_m, with_labels=True,
            node_size=3000, font_size=10,
            node_color="skyblue", edge_color="gray"
        )

        try:
            edge_labels_m = nx.get_edge_attributes(self.graph_m, 'weight')
            if edge_labels_m:
                nx.draw_networkx_edge_labels(
                    self.graph_m, pos_m,
                    edge_labels=edge_labels_m,
                    font_color="red"
                )
        except KeyError:
            pass

        plt.title(title_m)
        plt.show()

    def clear_graph_m(self):
        self.graph_m.clear()
        self.central_m = None
```

### Usage Example

```python
from modules.graph_m import Graph_m
from modules.util import get_languges

student_m = "laila mansour"
student_data_m = df[df["Name"] == student_m]
student_langs_m = get_languges(student_data_m["Programming Languages"].iloc[0])

graph_m = Graph_m(kind_m="Normal")
graph_m.create_graph_m(student_m, student_langs_m, all_languages_m)
graph_m.draw_graph_m(title_m="Student Language Graph")

cert_m = input("Please enter the certificate: ").lower().strip()

if cert_m in all_certificates_m:
    di_graph_m = Graph_m(kind_m="Directed")
    di_graph_m.create_graph_projects_m(cert_m, cert_student_projects_m)
    di_graph_m.draw_graph_m(title_m="Directed Graph for Certification Projects")
else:
    print("The certification does not exist")
```

---

## Assignment Context

This code is part of a **Data Mining** course assignment at **AlHussein Technical University (HTU)**.  
The primary objectives include:

1. **Data Preprocessing & Feature Engineering**  
2. **Dimensionality Reduction** (PCA, LDA)  
3. **Clustering & Evaluation** (KMeans, DBSCAN, KMedoids, Agglomerative)  
4. **Text Analysis** using TF-IDF  
5. **Graph Representation & Visualization** with NetworkX

Students learn how to handle both numeric and text data, apply different mining techniques, and visualize results to gain insights into the data.

---

## Repository Structure

```
.
├─ modules/
│  ├─ clustering.py         # 'Clustering' class
│  ├─ tfidf_moh.py          # 'TfIdf_moh' class
│  ├─ graph_m.py            # 'Graph_m' class (example name)
│  └─ util.py               # Utility functions (e.g., get_languges)
├─ README.md                # This file
└─ ...
```

---

## Installation

1. **Clone** the repository:

   ```bash
   git clone https://github.com/YourUserName/YourRepoName.git
   cd YourRepoName
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
   (Ensure you have `scikit-learn`, `pandas`, `seaborn`, `matplotlib`, `networkx`, and `sklearn-extra` installed.)


**AlHussein Technical University (HTU) – Data Mining Course Assignment**  
Created by: **Mohammad Almasri**
```
