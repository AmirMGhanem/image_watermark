import os

from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware

from watermark import place_pins_on_image
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
import openai


api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

main_folder_path = f"/Users/amirbusiness/pCloud Drive/P- Main/Signaturo/Categories/"
watermark_folder_output = f"/Users/amirbusiness/pCloud Drive/P- Main/Signaturo/Categories"

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
app.mount("/images", StaticFiles(directory=main_folder_path), name="images")


@app.get("/")
def read_root():
    # delay 3 sec

    # time.sleep()
    response = image_analysis("https://media.istockphoto.com/id/1352120492/vector/woman-blowing-bubble-with-a-pink-bubble-gum-and-pop-speech-bubble-pop-art-comic-vector.jpg?s=612x612&w=0&k=20&c=DM5h6PMf6_In3yZsluOeOTUzYLxXgyrfm_efgljaUv8=")

    return{
            "result": "Welcome to the API, Result From Python. Now we need to go external API to analyze",
            "description": response
    }



@app.post("/imageWatermark")
def image_watermark(image_path: str):
    try:

        # image_path = http://localhost:8000/images/test/003.png


        category_folder = image_path.split("http://localhost:8000/images/")[1].split("/")[0]

        image_path= main_folder_path+image_path.split("http://localhost:8000/images/")[1]

        watermark_folder_output = f"/Users/amirbusiness/pCloud Drive/P- Main/Signaturo/Categories/{category_folder}/watermarked"
        # watermark the image
        place_pins_on_image(image_path, "pin.png", watermark_folder_output)
        return {
            "result": "Image Watermarked",
            "description": "The image has been watermarked successfully."
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/allImages/{subfolder}")
def all_images(subfolder: str):
    try:
        # edit subfolder
        app.subfolder = subfolder
        # Get all the image files in the main folder
        # folder=main_folder_path
        folder= main_folder_path + subfolder
        print(folder)
        image_files = [image for image in os.listdir(folder) if image.endswith(('png', 'jpg', 'jpeg', 'gif'))]
        print(image_files)
        # Build the list of image URLs
        image_urls = [f"http://localhost:8000/images/{subfolder}/{image}" for image in image_files]
        return {
            "result": "Success",
            "images": image_urls
        }
    except Exception as e:
        return {
            "result": "Error",
            "description": str(e)
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)