FROM python:3.9

WORKDIR /sentimentApi

# 
COPY ./app/requirements.txt /sentimentApi/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /sentimentApi/requirements.txt

# 
COPY ./app /sentimentApi/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]