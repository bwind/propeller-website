from propeller import RequestHandler, Response, Template, __version__


class DownloadsHandler(RequestHandler):
    def get(self, request):
        return Response(Template('downloads.html', {'version': __version__}))
