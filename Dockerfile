FROM python:3.11

WORKDIR /sentimentApi

# 
COPY ./app/requirements.txt /sentimentApi/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /sentimentApi/requirements.txt

# 
COPY . .

EXPOSE 3200

CMD ["gunicorn", "app.main:app"]

