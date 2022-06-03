from flask import Flask,jsonify,request
from sklearn.datasets import load_iris
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return 'Creando la primera pagina'

@app.route('/predecir')
def predecir():
    # json=request.get_json()
    # medidas=json['Medidas']
    # clf = joblib.load('modelo_entrenado.pkl')
    # prediccion = clf.predict(medidas)
    # return 'Las medidas que diste corresponde a la clase {0}'.format(prediccion)
    return 'Las medidas que diste corresponde a la clase'

if __name__ == '__main__':
    app.run()