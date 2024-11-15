import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
import openai


api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key


def image_analysis(image_path):
    try:
        response = openai.Image.create(
            prompt="An image of a dog",
            n=1,
            size="512x512",
        )
        return response
    except Exception as e:
        return str(e)

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    # delay 3 sec

    # time.sleep()
    response = image_analysis("https://media.istockphoto.com/id/1352120492/vector/woman-blowing-bubble-with-a-pink-bubble-gum-and-pop-speech-bubble-pop-art-comic-vector.jpg?s=612x612&w=0&k=20&c=DM5h6PMf6_In3yZsluOeOTUzYLxXgyrfm_efgljaUv8=")

    return{
            "result": "Welcome to the API, Result From Python. Now we need to go external API to analyze",
            "description": response
    }
