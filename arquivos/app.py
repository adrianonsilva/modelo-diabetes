from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import pickle
import sklearn as sk
#from sklearn.preprocessing import Imputer
from sklearn.naive_bayes import GaussianNB
#from sklearn import metrics
import numpy as np

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "Hello World! <strong>I am learning Flask</strong>", 200

@app.route('/pagina',methods = ['POST', 'GET'])
def root():
	if request.method == 'POST':
		pregnancies = request.form['pregnancies']
		glucose = request.form['glucose']
		bloodpressure = request.form['bloodpressure']
		skinthickness = request.form['skinthickness']
		insulin = request.form['insulin']
		bmi = request.form['bmi']
		diabfunction = request.form['diabfunction']
		age = request.form['age']

		pregnancies = float(pregnancies)
		glucose = float(glucose)
		bloodpressure = float(bloodpressure)
		skinthickness = float(skinthickness)
		insulin = float(insulin)
		bmi = float(bmi)
		diabfunction = float(diabfunction)
		age = float(age)

		filename = 'static/model/modelo_diabetes_v1.sav'
		loaded_model = pickle.load(open(filename, 'rb'))
		retorno = loaded_model.predict([[pregnancies, glucose,bloodpressure,skinthickness,insulin,bmi,diabfunction,age]])
		resultado = ''

		if retorno[0] == 1:
			resultado = 'Desenvolveu diabetes.'
		else:
			resultado = 'Não desenvolveu diabetes.'

		return render_template('pagina1.html', pregnancies = pregnancies,glucose = glucose,bloodpressure = bloodpressure,skinthickness = skinthickness,insulin = insulin,bmi = bmi,diabfunction = diabfunction,age = age, Outcome=resultado)
	else:
		return render_template('pagina1.html')

#app.run()
if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0',port=5000)
