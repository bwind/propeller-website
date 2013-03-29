from propeller import Application, RequestHandler, Response


class HomeHandler(RequestHandler):
    def get(self, request):
        return Response('Hello world')

    def post(self, request):
        data = ''
        while True:
            d = request.files[0].file.read(1024)
            if not d:
                break
            data += d
        return Response(data, content_type='image/jpeg')

a = Application([
    (r'^/', HomeHandler)
], port=5000, debug=False)

if __name__ == '__main__':
    a.run()
