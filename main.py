from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import replicate
from dotenv import load_dotenv

# Finding variables
load_dotenv()

# FastAPI app
app = FastAPI()


class generateRequest(BaseModel):
    category: str
    humanImage: str
    garmentImage: str


@app.get("/home")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}


@app.post("/generate")
async def generate_image(
    request: generateRequest,
):

    input = {
        "category": request.category,
        "garment_des": "",
        "garm_img": request.garmentImage,
        "human_img": request.humanImage,
    }
    try:
        # Send POST request (replace with actual request method if needed)
        output = replicate.run(
            "cuuupid/idm-vton:906425dbca90663ff5427624839572cc56ea7d380343d13e2a4c4b09d3f0c30f",
            input=input,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating image: {e}")

    # Handle response (replace with logic to process actual response data)
    return {"img": output}
