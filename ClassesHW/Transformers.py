from CountVectorizer import CountVectorizer
import numpy as np
from functools import reduce
from operator import add


class TfidfTransformer:
    """
    Transforms numeric matrix into tf-idf matrix.
    do_round is whether we round numbers or not.
    """

    def __init__(self, do_round=True):
        self.do_round = do_round

    def tf_transform(self, count_matrix):
        if self.do_round:
            return [
                *map(
                    lambda x: [*map(lambda y: round(y / reduce(add, x), 3), x)], cmatrix
                )
            ]
        else:
            return [*map(lambda x: [*map(lambda y: y / reduce(add, x), x)], cmatrix)]

    def idf_transform(self, count_matrix):
        n = len(count_matrix)
        idf_matrix = []
        for i in range(len(count_matrix[0])):
            count = 0
            for j in range(n):
                if count_matrix[j][i] > 0:
                    count += 1
            if self.do_round:
                idf_i = round(np.log((n + 1) / (count + 1)) + 1, 3)
            else:
                idf_i = np.log((n + 1) / (count + 1)) + 1
            idf_matrix.append(idf_i)
        return idf_matrix

    def fit_transform(self, count_matrix):
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        if self.do_round:
            return [[round(j * idf[i], 3) for i, j in enumerate(row)] for row in tf]
        else:
            return [[j * idf[i] for i, j in enumerate(row)] for row in tf]


class TfidfVectorizer(TfidfTransformer, CountVectorizer):
    """
    Transforms corpus of texts into TfIdf matrix
    do_round is the same as in TfIdf
    """

    def __init__(self, do_round=True):
        CountVectorizer.__init__(self)
        TfidfTransformer.__init__(self, do_round)

    def get_feature_names(self, corpus):
        return super().get_feature_names(corpus)

    def fit_transform(self, texts):
        matrix = CountVectorizer.fit_transform(self, texts)
        final_matrix = TfidfTransformer.fit_transform(self, matrix)
        return final_matrix


if __name__ == "__main__":
    cmatrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    ]
    transformer = TfidfTransformer()
    print(transformer.fit_transform(cmatrix))

    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]

    vectorizer = TfidfVectorizer()
    print(vectorizer.get_feature_names(corpus))
    print(vectorizer.fit_transform(corpus))
