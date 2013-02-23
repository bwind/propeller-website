from propeller import Application, RequestHandler, Response


class HomeHandler(RequestHandler):
    def get(self, request):
        for k, v in request.headers.items():
            print k, v
        return Response('Hello world')

a = Application([
    (r'^/', HomeHandler)
], port=5000, debug=True)

if __name__ == '__main__':
    a.run()
