import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.cluster import KMeans, DBSCAN
from sklearn_extra.cluster import KMedoids
from sklearn.metrics import adjusted_mutual_info_score, adjusted_rand_score
from modules.util import get_languges
import seaborn as sns

class Clustering:
    def __init__(self, df):
        self.true_labels = df['Cluster'].values
        self.df = df.drop(columns=['Name', 'Bio', 'Cluster'])
        self.features = None
        self.results = {}

    def preprocess_data(self):
        categorical_features_m = self.df.copy()
        
        categorical_features_m['Project Count'] = StandardScaler().fit_transform(categorical_features_m[['Project Count']])
        
        categorical_cols = ['Certifications', 'Extracurricular Activities', 'Career Interest']
        categorical_features_m = pd.get_dummies(categorical_features_m, columns=categorical_cols)
        
        langs = get_languges(categorical_features_m['Programming Languages'].str)
        categorical_features_m = pd.concat([categorical_features_m, langs], axis=1)
        categorical_features_m = categorical_features_m.drop(['Programming Languages'], axis=1)
        
        self.features = categorical_features_m.values
        return self.features

    def reduce_dimensions(self, method='PCA'):
        if method == 'PCA':
            reducer = PCA(n_components=2)
            return reducer.fit_transform(self.features)
        elif method == 'LDA':
            n_classes = len(np.unique(self.true_labels))
            valid_components = min(n_classes - 1, 2)
            if valid_components < 1:
                raise ValueError("LDA requires at least 2 different clusters")
            reducer = LDA(n_components=valid_components)
            return reducer.fit_transform(self.features, self.true_labels)
        else:
            raise ValueError("Invalid reduction method")

    def apply_clustering(self, data, method):
        if method == 'kmeans':
            model = KMeans(n_clusters=3)
        elif method == 'dbscan':
            model = DBSCAN()
        elif method == 'kmedoids':
            model = KMedoids(n_clusters=3)
        else:
            raise ValueError("Invalid clustering method")
        return model.fit_predict(data)

    def evaluate_clusters(self, labels):
        return {
            'AMI': adjusted_mutual_info_score(self.true_labels, labels),
            'ARI': adjusted_rand_score(self.true_labels, labels)
        }

    def run_analysis(self):
        self.preprocess_data()
        
        methods = ['kmeans', 'dbscan', 'kmedoids']
        reductions = ['PCA', 'LDA']
        
        for method in methods:
            self.results[method] = {}
            for reduction in reductions:
                try:
                    reduced_data = self.reduce_dimensions(reduction)
                    labels = self.apply_clustering(reduced_data, method)
                    self.results[method][reduction] = self.evaluate_clusters(labels)
                except Exception as e:
                    print(f"Error with {method}-{reduction}: {str(e)}")
                    self.results[method][reduction] = None
        
        return self.results

    def visualize_comparison(self):
        metrics = ['AMI', 'ARI']
        methods = list(self.results.keys())
        reductions = ['PCA', 'LDA']
        
        fig, axs = plt.subplots(1, len(metrics), figsize=(15, 6))
        
        for metric_idx, metric in enumerate(metrics):
            # Prepare data for plotting
            data = {
                method: [
                    self.results[method][reduction][metric] 
                    for reduction in reductions
                ] 
                for method in methods
            }
            
            # Plot settings
            x = np.arange(len(methods))
            width = 0.35
            
            # Create bars for each reduction method
            for i, reduction in enumerate(reductions):
                offset = width * i
                values = [self.results[method][reduction][metric] for method in methods]
                axs[metric_idx].bar(x + offset, values, width, label=reduction)
            
            # Formatting
            axs[metric_idx].set_title(metric)
            axs[metric_idx].set_xticks(x + width/2)
            axs[metric_idx].set_xticklabels(methods)
            axs[metric_idx].set_ylim(0, 1)
            axs[metric_idx].legend()
        
        plt.tight_layout()
        plt.show()

