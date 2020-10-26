import numpy as np
import scipy.sparse as sp
from typing import List


class CountVectorizer:
    def __init__(self, max_words=500):
        self.max_words = max_words
        self.feature_names = []

    def get_feature_names(self, corpus):
        for sentence in corpus:
            for word in sentence.split(' '):
                if word.lower() not in self.feature_names:
                    self.feature_names.append(word.lower())
        return self.feature_names

    def fit_transform(self, corpus):
        words = {}
        result = []
        _ = self.get_feature_names(corpus)

        for line in corpus:
            for word in self.feature_names:
                words[word] = 0

            for i in line.split(' '):
                words[i.lower()] += 1
            
            result.append(list(words.values()))
        return result


corpus = [
'Crock Pot Pasta Never boil pasta again',
'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = CountVectorizer()

print(vectorizer.get_feature_names(corpus))
print(vectorizer.fit_transform(corpus))

