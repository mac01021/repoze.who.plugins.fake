repoze.who.plugins.fake
=======================

Fake authenticators that may be useful for testing your web application



To use, add the following entries to your who.ini file

    [plugin:fakeauth]
    use = repoze.who.plugins.fake:*{plugin-class-of-your-choosing}*

    [authenticators]
    plugins = fakeauth


Currently available plugin classes include

-   AllAcceptingAuthenticationPlugin - allows you to log in as any
    username without worrying about the password.  Use with the basicauth
    challenger

-   ScriptNameAuthenticationPlugin - Never challenges the user.  Uses the
    SCRIPT_NAME from the application environment as the login name.


