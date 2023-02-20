from collections import Counter
from collections import defaultdict
from scipy.sparse import csr_matrix
import numpy as np
from sklearn.preprocessing import normalize

def scan_vocabulary(sents, tokenize, min_count=2):
    for sent in sents:
        for w in tokenize(sent):
            counter = Counter(w)

    for w,c in counter.items():
        if c >= min_count:
            counter = {w:c}

    for w, _ in sorted(counter.items(), key=lambda x:-x[1]): # _ 사용한 이유? 무시 or 마지막 값 -> 없어도 되나? 
        idx_to_vocab = w        
    
    for idx, vocab in enumerate(idx_to_vocab) :
        vocab_to_idx = {vocab:idx}
    
    return idx_to_vocab, vocab_to_idx


def cooccurrence(tokens, vocab_to_idx, window=2, min_cooccurrence=2):
    counter = defaultdict(int)
    for s, tokens_i in enumerate(tokens):
        for w in tokens_i :
            if w in vocab_to_idx :
                vocabs = vocab_to_idx[w]

    n = len(vocabs)
    for i, v in enumerate(vocabs):
        if window <= 0:
            b, e = 0, n
        else: 
            b = max(0, i - window)
            e = min(i + window, n)
        for j in range(b, e):
            if i == j:
                continue
            counter[(v, vocabs[j])] += 1
            counter[(vocabs[j], v)] += 1

    for k, v in counter.items() :
        if v >= min_cooccurrence:
            counter = {k:v}            
    n_vocabs = len(vocab_to_idx)

    return dict_to_mat(counter, n_vocabs, n_vocabs)


def dict_to_mat(d, n_rows, n_cols):
    rows, cols, data = [], [], []
    for (i, j), v in d.items():
        rows.append(i)
        cols.append(j)
        data.append(v)
    
    return csr_matrix((data, (rows, cols)), shape = (n_rows, n_cols))

def word_graph(sents, tokenize=None, min_count=2, window=2, min_cooccurrence=2):
    idx_to_vocab, vocab_to_idx = scan_vocabulary(sents, tokenize, min_count)
    for sent in sents:
        tokens = tokenize(sent)
    g = cooccurrence(tokens, vocab_to_idx, window, min_cooccurrence, verbose)

    return g, idx_to_vocab

def pagerank(x, df=0.85, max_iter=30):
    assert 0 < df < 1

    #initialize
    A = normalize(x, axis=0, norm='l1')
    R = np.ones(A.shape[0]).reshape(-1,1)
    bias = (1 - df) * np.ones(A.shape[0]).reshape(-1,1)

    #iteration
    for _ in range(max_iter):
        R = df * (A * R) + bias

    return R