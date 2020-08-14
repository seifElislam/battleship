import json
import traceback
from http import HTTPStatus

from flask import Flask, jsonify, request

from battleship.game import Game

app = Flask(__name__)

game = Game.get_instance((10, 10))


@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    try:
        game = Game.get_instance((10, 10))
        ships = json.loads(request.data)['ships']
        for ship in ships:
            game.add_ship(**ship)
        return jsonify({"result": "ok"}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": e.__str__()}), HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['PUT'])
def shot():
    try:
        data = json.loads(request.data)
        x = data['x']
        y = data['y']
        response = game.handle_shot(x, y)
        return jsonify({"result": response}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": e.__str__()}), HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    global game
    del game
    return jsonify({"result": "deleted"}), HTTPStatus.OK
