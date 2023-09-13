FROM python:3.9

WORKDIR /sentimentApi

# 
COPY ./app/requirements.txt /sentimentApi/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /sentimentApi/requirements.txt

# 
COPY ./app /sentimentApi/app

# 
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 app.main:app

