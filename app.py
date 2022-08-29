from flask import Flask, render_template
from functions import utils as u

FILE = 'data/candidates.json'  # JSON file
app = Flask(__name__)  # Flask instance


@app.route('/', methods=['GET'])
def index():
	"""Main entry point"""
	return render_template('index.html', title='Candidates', data=data)


@app.route('/candidate/<int:pk>', methods=['GET'])
def candidate(pk):
	"""Page with candidate information"""
	candidate_ = u.get_by_pk(pk, data)
	if candidate_ is not None:
		return render_template('candidate.html', title=candidate_['name'],
								candidate_=candidate_)
	else:
		return render_template('error_404.html')


@app.route('/skills/<skill_name>', methods=['GET'])
def skills(skill_name):
	"""Page with skill information"""
	candidate_list = u.get_by_skill(skill_name, data)
	if candidate_list:
		return render_template('skills.html', candidate_list=candidate_list,
								title='Skills ' + skill_name)
	else:
		return render_template('error_404.html')


@app.errorhandler(404)
def error_404(error):
	"""Page 404 error"""
	return render_template('error_404.html', title='Oops!'), 404


data = u.load_json(FILE)

if __name__ == '__main__':
	app.run(debug=True)
