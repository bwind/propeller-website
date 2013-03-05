from handlers.home import HomeHandler
from handlers.downloads import DownloadsHandler
from handlers.benchmarks import BenchmarksHandler
from handlers.mailinglist import MailingListHandler
from propeller.app import Application
from propeller.request_handler import StaticFileHandler

import os
import settings
import sys


urls = (
    (r'^/$', HomeHandler),
    (r'^/downloads$', DownloadsHandler),
    (r'^/benchmarks$', BenchmarksHandler),
    (r'^/mailinglist$', MailingListHandler),
    (r'^/static/(.*)$', StaticFileHandler, {'static_path': os.path.join(sys.path[0], 'static')}),
)

settings = {'urls': urls, 'debug': settings.DEBUG}

a = Application(**settings)
a.run()
