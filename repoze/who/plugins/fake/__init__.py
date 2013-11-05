
class AllAcceptingAuthenticationPlugin(object):
 
    def __init__(self, *args, **kwargs):
    pass
 
    # IAuthenticatorPlugin
    def authenticate(self, environ, identity):
        try:
            login = identity['login']
            password = identity['password']
            if login: return login
        except KeyError:
            pass
        return None
