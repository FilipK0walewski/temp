from libs.services.basic_service import BasicService


class AllegroService(BasicService):

    def __init__(self, base_url):

        BasicService.__init__(self, base_url)

    def get_offer(self, offer_id):

        return self.request(path=f'/allegro/offers/{offer_id}')

    def search_offers(self, params=None):

        return self.request(path='/allegro/offers/search', params=params)

    def get_error(self, error_id):

        return self.request(path=f'/allegro/offers/errors/{error_id}')

    def search_errors(self, params=None):

        return self.request(path='/allegro/offers/errors/search', params=params)

    def get_command(self, command_id):

        return self.request(path=f'/allegro/commands/{command_id}')

    def search_commands(self, params=None):

        return self.request(path='/allegro/commands/search', params=params)

    def get_shipping_rate(self, shipping_rate_id):

        return self.request(path=f'/allegro/delivery/shipping-rates/{shipping_rate_id}')

    def search_shipping_rate(self, params=None):

        return self.request(path='/allegro/delivery/shipping-rates/search', params=params)

    def search_shipping_rates_config(self, params=None):

        return self.request(path='/allegro/config/offers-shipping-rates/search', params=params)

    def create_shipping_rate_config(self, shipping_rate_id, typer, value):

        data = {
            'shipping_rate_id': shipping_rate_id,
            'type': typer,
            'value': value
        }
        return self.request(method='POST', path='/allegro/config/offers-shipping-rates', data=data)

    