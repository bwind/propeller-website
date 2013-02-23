from settings import *
from propeller import RequestHandler, Response, NotFoundResponse, Template

import markdown2
import os


class DocsHandler(RequestHandler):
    def get(self, request, page=None):
        if not page:
            page = 'index'
        fname = os.path.join(DOCS_PATH, page + '.txt')
        if not fname.startswith(DOCS_PATH) or not os.path.exists(fname):
            return NotFoundResponse(request.url)
        content = markdown2.markdown(open(fname).read())
        return Response(Template('docs.html', {'content': content}))
