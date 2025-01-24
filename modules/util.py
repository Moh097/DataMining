from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import re

import numpy as np 

ranked_bios=None
def remove_stop_words(text):
    words = text.split()
    return " ".join(word for word in words if word.lower() not in ENGLISH_STOP_WORDS)

def has_words_english(query):
    return bool(re.search(r'[a-zA-Z]', query))

def get_languges(languages):
    parsed_languages = []
    if not languages:
        return []  
    return languages.split(";")

def get_ranked_results(tfodel, df, query):
    results = tfodel.rank_queries([query])
    result = results.get(query, {})
    ranked_bios = np.array(result.get("rankedIndexes", []))
    scores = np.array(result.get("score", []))
    return ranked_bios, scores

def calculate_dynamic_threshold(scores, df, ranked_bios):
    if len(scores) == 0:
        return np.array([]), np.array([]), 0.0
    
    max_desired = len(df) // 3
    if len(scores) > 1:
        diffs = scores[:-1] - scores[1:]
        elbow_idx = np.argmax(diffs) + 1
        threshold = scores[elbow_idx]
    else:
        threshold = scores[0]
    
    mask = scores >= threshold
    selected_bios = ranked_bios[mask][:max_desired]
    selected_scores = scores[mask][:max_desired]
    return selected_bios, selected_scores, threshold  

def write_ranked_results(path, df, selected_bios, selected_scores):
    with open(path, "w") as file:
        if len(selected_bios) > 0:
            for idx, score in zip(selected_bios, selected_scores):
                file.write(f"Bio: {df['Bio'][idx]}\n")
                file.write(f"Score: {score:.4f}\n")
            return True
        else:
            file.write("no related bios")
            return False
