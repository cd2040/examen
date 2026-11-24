from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = None
    total_sin_descuento = None
    descuento = None
    total_pagar = None
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        
        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro
        
        if edad >= 18 and edad <= 30:
            porcentaje_descuento = 0.15
        elif edad > 30:
            porcentaje_descuento = 0.25
        else:
            porcentaje_descuento = 0.0
            
        descuento = total_sin_descuento * porcentaje_descuento
        total_pagar = total_sin_descuento - descuento

    return render_template(
        'ejercicio1.html',
        nombre=nombre,
        total_sin_descuento=total_sin_descuento,
        descuento=descuento,
        total_pagar=total_pagar
    )

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        
        if usuario == 'juan' and contrasena == 'admin':
            mensaje = 'Bienvenido Administrador juan'
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = 'Bienvenido Usuario pepe'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)