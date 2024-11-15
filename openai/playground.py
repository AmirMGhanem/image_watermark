import os

import openai

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key


def image_analysis(image_path):
    try:
        response = openai.Image.create(
            prompt="An image of a dog",
            image=image_path,
            n=1,
            size="512x512",
        )
        return response
    except Exception as e:
        return str(e)
