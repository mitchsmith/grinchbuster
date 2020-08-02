import os, shlex, subprocess
from PIL import Image
from flask import render_template
from app import app

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIADIR = os.path.join(BASEDIR, 'app/static/media/')
MEDIAURL = "/static/media/"

@app.route('/')
def index():
    return "Running..."


@app.route('/monitor')
def monitor():
	sensitivity = 50
	threshold = 0
	listing = sorted(os.listdir(MEDIADIR), reverse = True)
	
	if len(listing) > 2:
		image_a = listing[1] 
		image_b = listing[2]
		# Extract the red channel data from a 20 x 20 pixel version of a and b images 
		sample_a = [d[0] for d in Image.open(os.path.join(MEDIADIR, image_a)).resize((20, 20)).getdata()]
		sample_b = [d[0] for d in Image.open(os.path.join(MEDIADIR, image_b)).resize((20, 20)).getdata()]

		deltas = [abs(sample_a[i] - sample_b[i]) for i in range(0, len(sample_a)) if abs(sample_a[i] - sample_b[i]) > sensitivity]

	if len(listing) > 10:
		trash = listing[10:]
		for filename in trash:
			os.remove(os.path.join(MEDIADIR, filename))

	return render_template('monitor.html', listing = listing[1:10], image_a = MEDIAURL + image_a, image_b = MEDIAURL + image_b, difference = len(deltas)) 

