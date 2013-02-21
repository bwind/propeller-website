from propeller import RequestHandler, Response, Template


class HomeHandler(RequestHandler):
    def get(self, request):
        return Response(Template('home.html'))
