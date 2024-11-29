from flask import Flask, request, send_file, render_template
from yt_dlp import YoutubeDL
import os

app = Flask(__name__)

# Ensure the downloads directory exists
os.makedirs('app/downloads', exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/youtube', methods=['GET', 'POST'])
def youtube_download():
    if request.method == 'POST':
        url = request.form.get('url')
        options = {
            'format': 'best',
            'outtmpl': 'app/downloads/%(title)s.%(ext)s',
        }
        try:
            with YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
            return send_file(filename, as_attachment=True)
        except Exception as e:
            return f"Error: {e}", 400
    return render_template('youtube.html')

@app.route('/tiktok', methods=['GET', 'POST'])
def tiktok_download():
    if request.method == 'POST':
        url = request.form.get('url')
        options = {
            'format': 'best',
            'outtmpl': 'app/downloads/%(title)s.%(ext)s',
        }
        try:
            with YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
            return send_file(filename, as_attachment=True)
        except Exception as e:
            return f"Error: {e}", 400
    return render_template('tiktok.html')
