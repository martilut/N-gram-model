import numpy as np


class NgramModel:

    def __init__(self, n=2):
        self.n = n
        self.words = None
        self.prefix_dict = None

    @staticmethod
    def set_probability(prefix_dict):
        word_count = 0
        for word in prefix_dict.keys():
            word_count += prefix_dict[word]
        for word in prefix_dict.keys():
            prefix_dict[word] = prefix_dict[word] / word_count

    def fit(self, words):
        prefix_dict = dict()
        text_size = len(words)
        for i in range(text_size - self.n + 1):
            prefix = tuple(words[j] for j in range(i, i + self.n))
            if prefix_dict.get(prefix) is None:
                prefix_dict[prefix] = {}
            if i + self.n < text_size:
                next_word = words[i + self.n]
                if prefix_dict[prefix].get(next_word) is None:
                    prefix_dict[prefix][next_word] = 1
                else:
                    prefix_dict[prefix][next_word] += 1
        for prefix in prefix_dict.keys():
            self.set_probability(prefix_dict[prefix])
        self.words = words
        self.prefix_dict = prefix_dict

    def generate(self, text_size, seed=None, prefix=None):
        if self.words is None or self.prefix_dict is None:
            raise ValueError('Model is not trained')
        np.random.seed(seed)
        start_index = np.random.randint(0, len(self.words) - self.n + 1)
        if prefix is None:
            cur_prefix = tuple([self.words[i] for i in range(start_index, start_index + self.n)])
        else:
            cur_prefix = tuple(prefix)
        result = ' '.join(cur_prefix)
        for i in range(text_size):
            next_word = None
            if self.prefix_dict.get(cur_prefix) is not None:
                cur_words = [key for key in self.prefix_dict[cur_prefix].keys()]
                cur_probs = [self.prefix_dict[cur_prefix][key] for key in cur_words]
                next_word = np.random.choice(a=cur_words, p=cur_probs)
                result += f' {next_word}'
            else:
                for prefix in self.prefix_dict.keys():
                    if cur_prefix[-1] == prefix[-1]:
                        cur_words = [key for key in self.prefix_dict[prefix].keys()]
                        cur_probs = [self.prefix_dict[prefix][key] for key in cur_words]
                        next_word = np.random.choice(a=cur_words, p=cur_probs)
                        result += f' {next_word}'
                        break
            cur_prefix = [cur_prefix[i] for i in range(1, )]
            cur_prefix.append(next_word)
            cur_prefix = tuple(cur_prefix)
        return result
