import flask
from flask import render_template
import keras
import tensorflow as tf
from tensorflow import keras
import numpy as np

app = flask.Flask(__name__, template_folder ='templates')

def get_prediction(parametrs,loaded_model):
    y_pred = loaded_model.predict(parametrs)

    return f"Соотношение матрица-наполнитель {y_pred}"

@app.route('/', methods=['post', 'get'])
def main():
    loaded_model = keras.models.load_model("C:/Users/mi/Desktop/ML_project/model/")
    message = ''

    if flask.request.method == 'POST':
        parametrs = flask.request.form.get('p1')
        parametrs_parametrs =parametrs.split(" ")
        parametrs = [float(param) for param in parametrs_parametrs]
        parametrs=np.array([parametrs])
        
        message = get_prediction(parametrs,loaded_model)
    return render_template ('main.html', result = message)
if __name__ == '__main__':
    app.run(debug=True)
