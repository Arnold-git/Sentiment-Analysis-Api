# Sentiment Analysis API :rocket:

The purpose of this README.md file is to explain the steps required to setup this project in your local environment for testing.

### How do I get set up? :pushpin:

### Requirements 
* Python

## Setting up with Python ### 

**Clone Repo**
```
git clone https://github.com/Arnold-git/Sentiment-Analysis-Api
```

**Change current working directory**
```
cd Sentiment-Analysis-Api
```

**Create a Virtual environment**
```
python -m venv .venv
```
**Activate virutual Environment**
```
#windows
source .venv/Scripts/activate
#linux
source .venv/bin/activate
```

**Install dependencies**
```
pip install -r app/requirements.txt
```

**Start Server**

```
uvicorn app.main:app --reload
```

## Demo

![Demo](app/asset/demo.gif)

I wrote an article on how to deploy this API with Google Cloud Run. [Check it out here](https://arnoldighiwiyisi.hashnode.dev/build-and-deploy-a-sentiment-analysis-api-with-fastapi-docker-and-google-cloud-run)