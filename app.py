from flask import Flask, send_file, render_template, request, make_response
import os
import random

app = Flask(__name__)

def sair_here():
    desicion = random.choice([True,False])
    print(desicion)
    return desicion


@app.route('/api/image/<filename>')
def get_image(filename):
    image_path = os.path.join('assets', filename)
    if os.path.exists(image_path):
        return send_file(image_path, mimetype='image/png')
    else:
        return {"error": "Archivo no encontrado"}, 404




@app.route('/fer_room')
def fer_room():

    visitas = request.cookies.get('contador_fer_room', '0')
    
    # Incrementar el contador
    visitas = int(visitas) + 1

    images = [
        #cama_fer.png
        {
            'key': 'bed',
            'filename':'cama_fer.png',
            'x': 9,
            'y': 9,
          'scale_x': 3,
          'scale_y': 3.5
        },
        #computer_fer.png
        {
            'key': 'computer',
            'filename': 'computer_fer.png',
            'x': 9,
            'y': 2,
            'scale_x': 3,
            'scale_y': 4
        },
        #mueble_fer.png
        {
            'key': 'furniture',
            'filename':'mueble_fer.png',
            'x': 1,
            'y': 8,
          'scale_x': 2,
          'scale_y': 3
        },
        {
            'key': 'door',
            'filename':'door_2.png',
            'x': 0,
            'y': 3,
            'scale_x': 1,
            'scale_y': 3
        },
    ]
    if visitas >= 2 and request.cookies.get('atun', 'false') == 'false' :
        images.append({
            'key': 'atun',
            'filename':'tesoro.png',
            'x': 5,
            'y': 5,
            'scale_x': 0.5,
            'scale_y': 1
        },)

    if visitas >= 3 and request.cookies.get('pintura', 'false') == 'false' :
        images.append({
            'key': 'pintura',
            'filename':'tesoro.png',
            'x': 2,
            'y': 8,
            'scale_x': 0.5,
            'scale_y': 1
        },)

    response = make_response(render_template('fer_room.html', images=images, roomWidth=10, roomHeight=10, offSet= 50))
    response.set_cookie('contador_fer_room', str(visitas), max_age=60*60*24*365)  # 1 año
    return response

@app.route('/rest_room')
def rest_room():
    contador_visitas = request.cookies.get('contador_rest_room', '0')
    contador_visitas = int(contador_visitas) + 1
    images = [
        #mueble_sale.png
        {
            'key': 'furniture',
            'filename':'mueble_sala.png',
            'x': 5,
            'y': 5,
            'scale_x': 2,
            'scale_y': 3
        },
        #tv_sala.png
        {
            'key': 'tv',
            'filename':'tv_sala.png',
            'x': 5,
            'y': 0,
          'scale_x': 3,
          'scale_y': 5
        },
        #door.png
        {
            'key': 'door',
            'filename':'door_2.png',
            'x': 0,
            'y': 3,
            'scale_x': 1,
            'scale_y': 3
        },
        #door.png
        {
            'key': 'door_2',
            'filename':'door_2.png',
            'x': 10,
            'y': 3,
            'scale_x': 1,
            'scale_y': 3
        },
        {
            'key': 'door_3',
            'filename':'door.png',
            'x': 8,
            'y': 5,
            'scale_x': 1,
            'scale_y': 3
        },
    ]

    if contador_visitas >= 3 and request.cookies.get('emmy', 'false') == 'false' :
        images.append({
            'key': 'emmy',
            'filename':'emmy.png',
            'x': 5,
            'y': 2,
            'scale_x': 0.5,
            'scale_y': 1
        },)

    sair_is_here = sair_here() 
    response = make_response(render_template('rest_room.html', images=images, roomWidth=10, roomHeight=5, offSet= 100, sair_is_here=sair_is_here))
    response.set_cookie('contador_rest_room', str(contador_visitas), max_age=60*60*24*365)  # 1 año
    return response

@app.route('/chicken')
def chicken():
    contador_visitas = request.cookies.get('contador_chicken', '0')
    contador_visitas = int(contador_visitas) + 1
    images = [
        #bicicleta.png
        {
            'key': 'bicycle',
            'filename':'bicicleta.png',
            'x': 3,
            'y': 1,
          'scale_x': 2,
          'scale_y': 3
        },
        #mueble_chicken.png
        {
            'key': 'furniture',
            'filename':'mueble_chicken.png',
            'x': 3,
            'y': 10.5,
          'scale_x': 2.4,
          'scale_y': 6
        },
        #isla_cocina.png
        {
            'key': 'cooking',
            'filename':'isla_cocina.png',
            'x': 8,
            'y': 7,
            'scale_x': 4,
            'scale_y': 6
        },
        #lavado_cocina.png
        {
            'key': 'washing',
            'filename':'lavado_cocina.png',
            'x': 7.5,
            'y': 10.5,
          'scale_x': 3,
          'scale_y': 5
        },
        #estufa_chicken.png
        {
            'key': 'oven',
            'filename':'estufa_chicken.png',
            'x': 10,
            'y': 10,
           'scale_x': 2,
           'scale_y': 4
        },
        #door.png
        {
            'key': 'door',
            'filename':'door_2.png',
            'x': 10,
            'y': 4,
            'scale_x': 1,
            'scale_y': 3
        },
        
    ]
    response = make_response(render_template('chicken.html', images=images, roomWidth=10, roomHeight=10, sair_is_here=sair_here(), offSet= 100))
    response.set_cookie('contador_chicken', str(contador_visitas), max_age=60*60*24*365)  # 1 año
    
    return response

@app.route('/sair_room')
def index():
    contador_visitas = request.cookies.get('contador_sair', '0')
    contador_visitas = int(contador_visitas) + 1
    images = [
        #mesita_sair.png
        {
            'key': 'table',
            'filename': 'mesita_sair.png',
            'x': 1,
            'y': 3,
           'scale_x': 1,
           'scale_y': 2
        },
        {
            'key': 'bed',
            'filename': 'bed_icon.png',
            'x': 2.5,
            'y': 5,
            'scale_x': 2,
            'scale_y': 4
        },
        {
            'key': 'chair',
            'filename': 'sair_chair.png',
            'x': 8,
            'y': 4,
          'scale_x': 1,
          'scale_y': 3
        },
        {
            'key': 'desktop',
            'filename': 'escritorio_sair.png',
            'x': 10,
            'y': 4.5,
            'scale_x': 2,
            'scale_y': 3
        },
        #computer_sair.png
        {
            'key': 'computer',
            'filename': 'computer_sair.png',
            'x': 8.5,
            'y': 3,
           'scale_x': 1.2,
           'scale_y': 1.5
        },
        {
            'key': 'door',
            'filename':'door.png',
            'x': 8,
            'y': 0,
            'scale_x': 1,
            'scale_y': 3
        },
    ]
    response = make_response(render_template('sair_room.html', images=images, roomWidth=10, roomHeight=5, offSet= 100, sair_is_here=sair_here()))
    response.set_cookie('contador_sair', str(contador_visitas), max_age=60*60*24*365)  # 1 año
    return response


if __name__ == '__main__':
    app.run(debug=True)