from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TfIdf_moh:

    def __init__(self):

        self.vectorizer = TfidfVectorizer()

        self.matrix = None

        self.bios = None

    def vectorize(self, bios):

        self.bios = bios

        self.matrix = self.vectorizer.fit_transform(bios)

    def rank_queries(self, queries):
        results = {}

        if self.matrix is None:
            return "no queries to rank "

        
        for query in queries:

            queryVectorized = self.vectorizer.transform([query])

            similarities = cosine_similarity(queryVectorized, self.matrix)[0]


            rankedIndexes_list = []

            scores = []

            for index in range(len(similarities)):

                max_index = -1
                max_value = -1

                for i, value in enumerate(similarities):
                    if i not in rankedIndexes_list and value > max_value:
                        max_value = value
                        max_index = i

                if max_index != -1:
                    rankedIndexes_list.append(max_index)
                    scores.append(max_value)

            results[query] = {
                "rankedIndexes": rankedIndexes_list,
                "score": scores
            }

        return results
