



FROM python:3.8.5-slim

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt
RUN apt-get update
RUN pip install --upgrade pip


RUN apt update
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
#RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
#RUN apt install -y libgl1-mesa-glx


RUN pip install python-multipart
RUN pip install -r requirements.txt


COPY ./app /app


EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]






