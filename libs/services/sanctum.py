from libs.services.basic_service import BasicService


class Sanctum(BasicService):

    def __init__(self, base_url):
        BasicService.__init__(self, base_url)

    def get_csrf_cookie(self):

        return self.request(path='/sanctum/csrf-cookie')
