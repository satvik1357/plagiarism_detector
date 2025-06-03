import re
import fitz
import docx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load BERT model once
model = SentenceTransformer('all-MiniLM-L6-v2')


def clean_text(text):
    text = text.lower()
    # Optional: remove common stopwords here if you want more filtering
    text = re.sub(r'[^a-z\s]', '', text)
    return text


def extract_text(path):
    if path.endswith('.txt'):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    elif path.endswith('.pdf'):
        doc = fitz.open(path)
        return ''.join([page.get_text() for page in doc])
    elif path.endswith('.docx'):
        doc = docx.Document(path)
        return '\n'.join([para.text for para in doc.paragraphs])
    return ''


def calculate_bert_similarity(text1, text2):
    embeddings = model.encode([text1, text2])
    sim = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(sim * 100, 2)


def calculate_ngram_hash_similarity(text1, text2, k=4):
    tokens1 = clean_text(text1).split()
    tokens2 = clean_text(text2).split()

    if len(tokens1) < k or len(tokens2) < k:
        return 0.0

    def get_ngrams(tokens):
        return {' '.join(tokens[i:i + k]) for i in range(len(tokens) - k + 1)}

    ngrams1 = get_ngrams(tokens1)
    ngrams2 = get_ngrams(tokens2)

    if not ngrams1 or not ngrams2:
        return 0.0

    intersection = ngrams1 & ngrams2
    union = ngrams1 | ngrams2

    return (len(intersection) / len(union)) * 100


def calculate_text_similarity(text1, text2):
    bert_score = calculate_bert_similarity(text1, text2)
    hash_score = calculate_ngram_hash_similarity(text1, text2, k=4)

    final_score = 0.65 * bert_score + 0.35 * hash_score
    final_score = min(100, final_score)

    # Penalize short texts similarity to reduce false positives
    if len(text1.split()) < 10 or len(text2.split()) < 10:
        final_score *= 0.7

    return round(final_score, 2)
