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

### Overview of Clustering
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

---

## 2. TF-IDF Module

**File**: `modules/tfidf_moh.py`

### Overview of TF-IDF
- Converts text (e.g., user bios) into TF-IDF vectors.
- Computes **cosine similarity** between each query and the bios corpus to rank documents.

---

## 3. Graph Module

**File**: `modules/graph.py`

### Overview of Graph Representation
- Uses **NetworkX** for graph/digraph creation.
- Visualizes relationships between students, programming languages, and certifications.

---

## Assignment Context

This code is part of a **Data Mining** course assignment at **AlHussein Technical University (HTU)**.  
The primary objectives include:

1. **Data Preprocessing & Feature Engineering**  
2. **Dimensionality Reduction** (PCA, LDA)  
3. **Clustering & Evaluation** (KMeans, DBSCAN, KMedoids, Agglomerative)  
4. **Text Analysis** using TF-IDF  
5. **Graph Representation & Visualization** with NetworkX

---

## Repository Structure

```
.
├─ modules/
│  ├─ clustering.py       
│  ├─ tfidf_moh.py          
│  ├─ graph.py          
│  └─ util.py           
├─ README.md            
└─ main.ipynb
```

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUserName/YourRepoName.git
   cd YourRepoName
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Required packages:
   - `scikit-learn`
   - `pandas`
   - `seaborn`
   - `matplotlib`
   - `networkx`
   - `sklearn-extra`

---

**AlHussein Technical University (HTU) – Data Mining Course Assignment**  
**Created by**: **Mohammad Almasri**

