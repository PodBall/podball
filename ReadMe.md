# PodBall MVP

This app is built in Flask, a Python micro-framework.

## Running locally

### Prerequisites
1. Ensure that you have Python 3.6 installed.  Python 3.8 is not compatible with Mozilla's DeepSpeech.
2. If you have not previously installed the virtual environment for Python, 
    ```pip install virtualenv```
### Prodcedure
1. Clone the repository from https://github.com/PodBall/podball
2. Navigate into the project directory.
3. Activate your virtual environment:
    ```virtualenv venv```
    ```source bin/activate```
4. Install requirements by running 
    ```pip install -r requirements.txt```
5. Run the application locally
    ```export FLASK_APP = run.py```
    ```flask run```
### Pull Requests
1. Create a dev branch:
  ```git checkout -b yourDevBranch```
2. After testing your code locally, commit and push to your branch
3. Make a pull request:
    ```git checkout master```
    ```git merge yourDevBranch```
4. The project development team will review merge conflicts on GitHub before accepting the pull request

## Deploying


## DeepSpeech
Read more about DeepSpeech here: https://deepspeech.readthedocs.io/en/v0.9.3/