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

## DeepSpeech
Read more about DeepSpeech here: https://deepspeech.readthedocs.io/en/v0.9.3/

## Librosa
Librosa is an audio-processing library created for musicians and music producers, which we are using to process non-speech audio.

## Current State of Project:
- At present, the project is largely in proof-of-concept phase.
- Flask was used to allow quick set-up of the various libraries.  Since Jinja2 templates are not very flexible, much of the front-end styling is done in extremely hacky ways, and probably should be discarded.
- File upload/download is fully set up using functions from python `os` and `glob` modules, but no data storage outside the session is currently possible.  
- Librosa is installed in the project, and routes have been added to `views.py`, but the functions are not completely developed and it is not integrated into the frontend UX.
- Deepspeech files are too large for a free GitHub account, so to run the project locally, you will need to install DeepSpeech locally and add it to your virtual environment for this project.
- Current data frames sent to frontend are 'dummy' data used for demo purposes, since the processing time for DeepSpeech is too long to use in a product demo.
- `librosafunctions.py` is a subset of all Librosa functions running simultaneously on a single audio file.  These are the functions that seemed most promising in terms of identifying unwanted "nonspeech" sounds.  Current output is visualizations using `matplotlib`. 
- To see all of the selected Librosa functions output in one place with some details on what each one does, and to be able to change the file they are run on easily, open `non-speech audio.ipynb` in Jupyter notebook.
- Note that the Zero-Crossing Rate function in Librosa plots along a different x-axis than the other functions.  Any filters built using these functions will need to compensate for this difference. Equations for making this adjustment are in `non-speech audio.ipynb`. 
