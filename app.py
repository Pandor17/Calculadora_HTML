from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

# Ruta principal para manejar el cálculo
@app.route('/calcular', methods=['POST'])
def calcular():
    datos = request.get_json()
    numero1 = float(datos['numero1'])
    numero2 = float(datos['numero2'])
    operacion = datos['operacion']
    
    resultado = None
    
    # Realiza la operación
    if operacion == '+':
        resultado = numero1 + numero2
    elif operacion == '-':
        resultado = numero1 - numero2
    elif operacion == '*':
        resultado = numero1 * numero2
    elif operacion == '/':
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            return jsonify({"error": "No se puede dividir por cero"}), 400
    
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)