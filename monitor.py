import os, time, datetime, shlex, subprocess
from PIL import Image

BASEDIR = os.path.dirname(os.path.abspath(__file__))
MEDIADIR = os.path.join(BASEDIR, 'app/static/media/')
MEDIAURL = "/static/media/"

used_images = ['','']

def initialize_stream():
	# Check network connection
	try:
		process = subprocess.run('ping -c 3 192.168.234.1', shell=True, check=True, stdout=subprocess.PIPE)
		# exp = re.compile('.*?(\d+)\% packet loss.*$')
		# exp.match(process.stdout.decode('utf-8').split('\n')[-3:][0])[1] == 100:

	except subprocess.CalledProcessError:
		# Attempt to retstart the wifi network  and return
		return 1

	# Check rtsp image stream and kill it if it exists

	# Remove residual images

	# Run png capture command	

	pass


def monitor():
	sensitivity = 60
	threshold = 4
	listing = sorted(os.listdir(MEDIADIR), reverse = True)
	
	if len(listing) > 2:
		image_a = listing[1] 
		image_b = listing[2]

		#if image_a == used_images[0] and image_b = used_images[1]
		# Extract the red channel data from a 20 x 20 pixel version of a and b images 
		sample_a = [d[0] for d in Image.open(os.path.join(MEDIADIR, image_a)).resize((20, 20)).getdata()]
		sample_b = [d[0] for d in Image.open(os.path.join(MEDIADIR, image_b)).resize((20, 20)).getdata()]

		deltas = [abs(sample_a[i] - sample_b[i]) for i in range(0, len(sample_a)) if abs(sample_a[i] - sample_b[i]) > sensitivity]

	if len(listing) > 10:
		trash = listing[10:]
		for filename in trash:
			os.remove(os.path.join(MEDIADIR, filename))

	# return render_template('monitor.html', listing = listing[1:10], image_a = MEDIAURL + image_a, image_b = MEDIAURL + image_b, difference = len(deltas)) 

	return len(deltas) 

if __name__ == '__main__':
	# clearcmd = "rm " + os.path.join(MEDIADIR, '*.png')
	# subprocess.run(clearcmd)
	time.sleep(10)
	print("Monitoring ...\n")
	while True:
		time.sleep(1)
		diff = monitor()
		if diff > 0:
			print("Motion detected! {}".format(diff) )
			subprocess.run(os.path.join(BASEDIR,'record.sh'))
