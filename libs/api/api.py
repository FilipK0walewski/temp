from flask import Flask
from flask_restful import reqparse, Resource, Api
from libs.services import *
from .api_helpers import *


app = Flask('michal_api')
api = Api(app)
allegro_service = AllegroService('http://192.168.1.242/api')
auth_service = AuthService('http://192.168.1.129/api')
sanctum = Sanctum('http://192.168.1.242')


@app.route('/sanctum/csrf-cookie')
def get_csrf_cookie():

    return sanctum.get_csrf_cookie()


@app.route('/login')
def login():

    return auth_service.login()


@app.route('/allegro/offers/<string:offer_id>')
def get_offer(offer_id):
    response = allegro_service.get_offer(offer_id)
    return response


@app.route('/allegro/offers')
def search_offers():

    return allegro_service.search_offers(params={
        'phrase': get('phrase'),
        'account_id': get('account_id'),
        'page': get('page'),
        'per_page': get('per_page')
    })


@app.route('/allegro/offers/errors/<string:error_id>')
def get_error(error_id):

    return allegro_service.get_error(error_id)


@app.route('/allegro/offers/errors/search')
def search_errors():

    return allegro_service.search_errors(params={
        'phrase': get('phrase'),
        'account_id': get('account_id'),
        'required_manual_review': get('required_manual_review'),
        'page': get('page'),
        'per_page': get('per_page')
    })


@app.route('/allegro/commands/<string:command_id>')
def get_command(command_id):

    return allegro_service.get_command(command_id)


@app.route('/allegro/commands/search')
def search_commands():

    return allegro_service.search_commands(params={
        'phrase': get('phrase'),
        'account_id': get('account_id'),
        'processed': get('processed'),
        'page': get('page'),
        'per_page': get('per_page')
    })


@app.route('/allegro/delivery/shipping-rates/search')
def search_shipping_rate():

    return allegro_service.request(params={
        'phrase': get('phrase'),
        'account_id': get('account_id'),
    })


@app.route('/allegro/config/shipping-rates/search')
def search_shipping_rates_config():

    return allegro_service.search_shipping_rates_config(params={
        'id': get('id'),
        'phrase': get('phrase')
    })
