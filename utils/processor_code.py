import re
import ast
from math import sqrt
from collections import Counter

def is_code_file(filename):
    return filename.lower().endswith(('.py', '.java', '.cpp', '.c'))

def is_text_file(filename):
    return filename.lower().endswith(('.txt', '.pdf', '.docx'))

def tokenize_code(code):
    code = re.sub(r'#.*', '', code)
    code = re.sub(r'""".*?"""', '', code, flags=re.DOTALL)
    code = re.sub(r"'''.*?'''", '', code, flags=re.DOTALL)
    tokens = re.findall(r'\b\w+\b', code)

    import keyword
    return [t if t in keyword.kwlist else 'ID' for t in tokens]

def get_ngrams(tokens, n=7):
    return [' '.join(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]

def jaccard_similarity(set1, set2):
    if not set1 or not set2:
        return 0.0
    return len(set1.intersection(set2)) / len(set1.union(set2))

def ast_node_freq(code):
    try:
        tree = ast.parse(code)
    except:
        return Counter()
    nodes = [type(node).__name__ for node in ast.walk(tree)]
    return Counter(nodes)

def cosine_sim(counter1, counter2):
    all_keys = set(counter1) | set(counter2)
    dot = sum(counter1[k] * counter2[k] for k in all_keys)
    mag1 = sqrt(sum(v*v for v in counter1.values()))
    mag2 = sqrt(sum(v*v for v in counter2.values()))
    if mag1 == 0 or mag2 == 0:
        return 0.0
    return dot / (mag1 * mag2)

def calculate_code_similarity(path1, path2):
    with open(path1, 'r', encoding='utf-8') as f:
        code1 = f.read()
    with open(path2, 'r', encoding='utf-8') as f:
        code2 = f.read()

    tokens1 = tokenize_code(code1)
    tokens2 = tokenize_code(code2)

    ngrams1 = set(get_ngrams(tokens1))
    ngrams2 = set(get_ngrams(tokens2))

    token_sim = jaccard_similarity(ngrams1, ngrams2)

    ast_freq1 = ast_node_freq(code1)
    ast_freq2 = ast_node_freq(code2)
    ast_sim = cosine_sim(ast_freq1, ast_freq2)

    final_sim = 0.7 * token_sim + 0.3 * ast_sim
    return round(final_sim * 100, 2)
