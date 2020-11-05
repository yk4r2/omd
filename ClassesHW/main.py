from typing import List


class CountVectorizer:
    def __init__(self):
        self._feature_names = []

    def get_feature_names(self, corpus: List[List[str]]) -> List[str]:
        """Fills in all the words matrix for encoding."""
        for sentence in corpus:
            for word in sentence.split(" "):
                if word.lower() not in self._feature_names:
                    self._feature_names.append(word.lower())
        return self._feature_names

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """Makes some kinda one-hot encoding for every word in sentence."""
        words = {}
        result = []
        _ = self.get_feature_names(corpus)

        for line in corpus:
            for word in self._feature_names:
                words[word] = 0

            for i in line.split(" "):
                words[i.lower()] += 1

            result.append(list(words.values()))
        return result


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = CountVectorizer()

    print(vectorizer.get_feature_names(corpus))
    print(vectorizer.fit_transform(corpus))
