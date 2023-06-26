
import uvicorn
from uvicorn import Config, Server
import fastapi
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pydantic
from pydantic import BaseModel
import PIL
from PIL import Image
import io

from fastapi.responses import HTMLResponse, StreamingResponse
import cv2
import numpy as np


app = FastAPI(title='Deploying a ML Model with FastAP')


# Define class for image requests
class ImageRequest(BaseModel):
    file_name: str
    file_content: UploadFile




@app.get("/")  
async def main():
    """Create a basic home page to upload a file

    :return: HTML for homepage
    :rtype: HTMLResponse
    """

    content = """<body>
          <h3>Upload an image to get ....</h3>
          <form action="/predict" enctype="multipart/form-data" method="post">
              <input name="files" type="file" multiple>
              <input type="submit">
          </form>
      </body>
      """
    return HTMLResponse(content=content)






#1- async type:
# Define API endpoint for image classification
@app.post("/predict/")
async def predict(files: UploadFile = File(...)):  
        # # first, VALIDATE INPUT FILE
        filename = files.filename
        fileExtension = filename.split(".")[-1] in ("jpg", "jpeg", "png", "JPG", "JPEG", "PNG")
        if not fileExtension:
            raise HTTPException(status_code=415, detail="Unsupported file provided.")  
        image = await files.read()
        image = Image.open(io.BytesIO(image)).convert('RGB')
        
        image=np.array(image)# cv2 need np.array format
        
        cv2.circle(image,(50,50),20,(0,0,255), -1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print(image,flush=True)
#         _, png_img = cv2.imencode('.PNG', image)  #me: without saving
#         return StreamingResponse(io.BytesIO(png_img.tobytes()), media_type="image/png")        
        cv2.imwrite("cv_sil.jpg", image) #????cv2.imencode
        new_image=open("cv_sil.jpg",mode="rb")#read the image as a binary
        return StreamingResponse(new_image,media_type="image/jpeg") #send binay image to the site 
        


# Start the app in normal deployment
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

