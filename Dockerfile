


FROM python:3.8-alpine  

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt

RUN apt install -y libgl1-mesa-glx
RUN pip install python-multipart
RUN pip install -r requirements.txt


COPY ./app /app


EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]






