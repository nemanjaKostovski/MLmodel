import flask
import pickle
import pandas as pd

with open(f'model/alloys_nb_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder = 'templates')

@app.route('/', methods = ['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        max_strength = flask.request.form['Rm']
        yield_strength = flask.request.form['Rp']
        elongation = flask.request.form['A%']
        webster = flask.request.form['Wb']
        input_variables = pd.DataFrame([[max_strength, yield_strength, elongation, webster]],
                                       columns = ['Rm', 'Rp', 'A%', 'Wb'],
                                       dtype = float)
        prediction = model.predict(input_variables)[0]
        return flask.render_template('main.html',
                                     original_input = {'Rm':max_strength,
                                                     'Rp':yield_strength,
                                                     'A%':elongation,
                                                     'Wb':webster},
                                     result = prediction
                                     )
if __name__ == '__main__':
    app.run()