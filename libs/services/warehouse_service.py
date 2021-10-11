from libs.services.basic_service import BasicService


class WarehouseService(BasicService):

    def __init__(self, base_url):

        BasicService.__init__(self, base_url)

    def get_product(self, product_id):

        return self.request(path=f'/warehouse/products/{product_id}')

    def get_products(self):

        return self.request(path='/warehouse/products')

    def search_products(self, params=None):

        return self.request(path='/warehouses/products/search', params=params)

    def get_product_computed(self, product_id):

        return self.request(path=f'/warehouse/products/computed/{product_id}')

    def get_products_computed(self):

        return self.request(path='/warehouse/products/computed')

    def search_products_computed(self, params=None):

        return self.request(path='/warehouse/products/computed/search', params=params)
