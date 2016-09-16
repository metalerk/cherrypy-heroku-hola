import random
import string
import cherrypy

class StringGenerator:
    
    @cherrypy.expose
    def index(self):
        return """<html>
        <head></head>
        <body>
          <form method="get" action="generate">
            <input type="text" value="8" name="length" />
            <button type="submit">Give it now!</button>
          </form>
        </body>
        </html>"""

    @cherrypy.expose
    def generate(self, length=8):
        try:
            return ''.join(random.sample(string.hexdigits, int(length)))
        except:
            return '[-] Numero Negativo o caracter inválido'

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
