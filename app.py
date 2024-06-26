from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo entrenado
model = joblib.load('diamonds_rfmodel.pkl')
scaler = joblib.load('standard_scaler.pkl')

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos enviados en el request
        carat = float(request.form['carat'])
        color = float(request.form['color'])
        clarity = float(request.form['clarity'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        
        # Escalar los datos de entrada
        scaled_data = scaler.transform([[carat, color, clarity, x, y]])
        
        # Crear un DataFrame con los datos escalados
        data_df = pd.DataFrame(scaled_data, columns=['Carat', 'Color', 'Clarity', 'x', 'y'])
        
        # Imprimir el DataFrame para verificar los datos
        print("Datos recibidos (escalados):")
        print(data_df)
        
        # Realizar la predicción
        prediction = model.predict(data_df)[0]
        
        # Devolver la predicción como respuesta JSON
        return jsonify({'prediction': prediction})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
