from fastapi import FastAPI
from pydantic import BaseModel
from scraper import scrape_website
from processor import generate_answer

app = FastAPI()

class Query(BaseModel):
    question: str
    url: str

@app.post("/chat")
def chat(query: Query):
    text = scrape_website(query.url)
    answer = generate_answer(text, query.question)
    return {"answer": answer}
