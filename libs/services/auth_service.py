from libs.services.basic_service import BasicService


class AuthService(BasicService):

    def __init__(self, base_url):
        BasicService.__init__(self, base_url)

    def login(self):

        return self.request(path='/auth/login')
