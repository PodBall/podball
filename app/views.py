from flask import render_template, request, make_response
from werkzeug.utils import secure_filename

from app import app
import os
import json
import pandas as pd
import speech_client
import librosa_functions

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/choices')
def choices():
    return render_template("choices.html")

<<<<<<< HEAD
@app.route('/deepspeech')
def deepspeech():
    #analysis = os.system("python clientV2.py --audio audio/SimpleTest3.wav --json")
    analysis = speech_client.main()
    json_data = analysis
    json_formatted = json.loads(json_data)
    word, start_time, duration = [],[],[]
    transcripts = json_formatted['transcripts']
    transcripts[1]['words']
    for result in transcripts[1]['words']:
        word.append(result['word'])
        start_time.append(result['start_time'])
        duration.append(result['duration'])
    
    df = pd.DataFrame({'word': word, 'start_time' : start_time, 'duration': duration})
    #jsonresponse = "Response from deep speech."
    df.to_csv('downloads/podball-analysis.csv')
    return render_template("deepspeech.html", dsresponse = df)

@app.route('/nonspeech')
def nonspeech():
//TODO: Create functions
    return render_template("nonspeech.html", libresponse=df)

@app.route('/upload')
def upload():
    return render_template("upload.html")
=======
@app.route('/start_upload')
def start_upload():
    return render_template("start_upload.html")
>>>>>>> master

@app.route('/uploader', methods =["GET", "POST"])
def upload_file():
    UPLOAD_FOLDER = 'uploads'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method == "GET":
        return render_template("upload.html")
    if request.method == "POST":
        f = request.files["file"]
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "file uploaded successfully"

@app.route('/searchwords')
def searchwords():
    return render_template("searchwords.html")

@app.route('/downloadNS', methods = ['GET'])
def download_NS_file():
    with open("downloads/podball-NS-analysis.csv") as fp:
        csv = fp.read()
    resp = make_response(csv)
    resp.headers["Content-Disposition"] = "attachment; filename=podball-NS-analysis.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@app.route('/analyze')
def analyze():
    analysis = speech_client.main()
    json_data = analysis
    json_formatted = json.loads(json_data)
    word, start_time, duration = [],[],[]
    transcripts = json_formatted['transcripts']
    transcripts[1]['words']
    for result in transcripts[1]['words']:
        word.append(result['word'])
        start_time.append(result['start_time'])
        duration.append(result['duration'])
    
    df = pd.DataFrame({'word': word, 'start_time' : start_time, 'duration': duration})
    #jsonresponse = "Response from deep speech."
    df.to_csv('downloads/podball-analysis.csv')
    return render_template("results.html", dsresponse = df)


@app.route('/download', methods = ['GET'])
def download_file():
    with open("downloads/podball-analysis.csv") as fp:
        csv = fp.read()
    resp = make_response(csv)
    resp.headers["Content-Disposition"] = "attachment; filename=podball-analysis.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

        
@app.route('/addwords', methods = ['POST'])
def addwords():
    searchwords = request.form.get("searchword")
    analysis_df = pd.read_csv("downloads/podball-analysis.csv", index_col=0)
    #searchwords = "name"
    filtered = analysis_df['word'] == searchwords
    filtered_df = analysis_df[filtered]
    return render_template("addwords.html", search=searchwords, result=filtered_df)

# @app.route('/search')
# def search():
#     return render_template("search.html")

@app.route('/results')
def results():
    #searchwords = request.form.get("searchword")
    analysis_df = pd.read_csv("downloads/podball-analysis.csv", index_col=0)
    #searchwords = "name"
    #filtered = analysis_df['word'] == searchwords
    filtered_df = analysis_df
    return render_template("results.html", result=filtered_df)
