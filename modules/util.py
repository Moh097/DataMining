from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import re

import numpy as np 

ranked_bios_m=None
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

def get_ranked_results_m(tf_model_m, df_m, query_m):
    results_m = tf_model_m.rank_queries([query_m])
    result_m = results_m.get(query_m, {})
    ranked_bios_m = np.array(result_m.get("rankedIndexes", []))
    scores_m = np.array(result_m.get("score", []))
    return ranked_bios_m, scores_m

def calculate_dynamic_threshold_m(scores_m, df_m, ranked_bios_m):
    if len(scores_m) == 0:
        return np.array([]), np.array([]), 0.0
    
    max_desired_m = len(df_m) // 3
    if len(scores_m) > 1:
        diffs_m = scores_m[:-1] - scores_m[1:]
        elbow_idx_m = np.argmax(diffs_m) + 1
        threshold_m = scores_m[elbow_idx_m]
    else:
        threshold_m = scores_m[0]
    
    mask_m = scores_m >= threshold_m
    selected_bios_m = ranked_bios_m[mask_m][:max_desired_m]
    selected_scores_m = scores_m[mask_m][:max_desired_m]
    return selected_bios_m, selected_scores_m, threshold_m  

def write_ranked_results_m(path_m, df_m, selected_bios_m, selected_scores_m):
    with open(path_m, "w") as file_m:
        if len(selected_bios_m) > 0:
            for idx_m, score_m in zip(selected_bios_m, selected_scores_m):
                file_m.write(f"Bio: {df_m['Bio'][idx_m]}\n")
                file_m.write(f"Score: {score_m:.4f}\n")
            return True
        else:
            file_m.write("no related bios")
            return False
