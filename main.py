from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import Dict

import requests as ree
from keybert import KeyBERT

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

kw_model = KeyBERT(model='paraphrase-multilingual-MiniLM-L12-v2')


@app.get("/", name="Health check route")
async def root() -> Dict:
    return {"status": "healthy"}

@app.get("/get_gen_keywords", name="This route is to extract keywords from generated text that is created from a prompt")
async def get_gen_keywords(text_prompt: str) -> Dict:
    """
    Takes a text; generates a large text body using text generation api and does keyword extraction
    on this text body.

    :param text_prompt:str text to generate keywords for
    :return:Dict containing keywords in a list in the form of {"result":{"keywords":keywords}}
    """

    prompt_len = len(text_prompt)

    #TODO: update endpoint url
    res = ree.get(f"https://abb-textgen-api-i6euhypvwa-ew.a.run.app/generate?prompt={text_prompt}&?temperature=2")
    res = res.json()

    content = " ".join([r[prompt_len:] for r in res])

    keywords = kw_model.extract_keywords(content, keyphrase_ngram_range=(1, 1))
    return {"result":{"keywords":keywords}}

@app.get("/get_text_keywords", name="This route is made to extract keywords from a document")
async def get_text_keywords(doc_text: str) -> Dict:
    """
    Takes a text generates a large text body using text generation api and does keyword extraction
    on this text body.

    :param text_prompt:str text to generate keywords for
    :return:Dict containing keywords in a list in the form of {"result":{"keywords":keywords}}
    """
    keywords = kw_model.extract_keywords(doc_text, keyphrase_ngram_range=(1, 1))
    return {"result":{"keywords":keywords}}



