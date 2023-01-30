# Sentiment Analysis API :rocket:

The purpose of this README.md file is to explain the steps required to setup this project in your local environment for testing.

### How do I get set up? :pushpin:

### Requirements 
* Python
* Docker

## Setting up with Python ### 

* Clone Repo
```
git clone https://github.com/Arnold-git/Sentiment-Analysis-Api
```

* Change current working directory
```
cd Sentiment-Analysis-Api
```

* Create a Virtual environment
```
python -m venv .venv
```
* Activate virutual Environment
```
source .venv/bin/activate
```

* Install dependencies
```
pip install -r requirements.txt
```

* Start Server

```
uvicorn app.main:app --reload
```

## Demo

[](app/asset/demo.gif)