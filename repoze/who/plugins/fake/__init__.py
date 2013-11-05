
class AllAcceptingAuthenticationPlugin(object):
    """ When challenged, the client can specify whatever
    user name she likes, and this authenticator will
    believe her.
    """

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



class ScriptNameAuthenticationPlugin(object):
    """ Never challenges the client.  Authenticates
    as the name of the script that the client has
    requested.
    """
 
    #IAuthenticatorPlugin
    def authenticate(self, environ, identity):
        return identity['login']
 
    #IIdentifierPlugin
    def identify(self, environ):
        return {'login': environ['SCRIPT_NAME'][1:],
                'password': None}
 
    #IIdentifierPlugin
    def remember(self, environ, identity):
        pass
 
    #IIdentifierPlugin
    def forget(self, environ, identity):
        pass


