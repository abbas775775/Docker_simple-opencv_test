


FROM python:3.10.12

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY ./app /app


EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]






