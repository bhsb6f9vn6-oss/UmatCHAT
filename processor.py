from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def generate_answer(scraped_text, user_question):
    sentences = scraped_text.split(".")
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(sentences + [user_question])
    similarity = cosine_similarity(vectors[-1], vectors[:-1])

    best_match = similarity.argmax()
    return sentences[best_match]
