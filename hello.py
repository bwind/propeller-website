from datetime import timedelta
from propeller import Application, RequestHandler, Response


class HomeHandler(RequestHandler):
    def get(self, request):
        r = Response('test')
        print request.cookies
        return r

a = Application([
    (r'^/$', HomeHandler),
], debug=True)

if __name__ == '__main__':
    a.run()
