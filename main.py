from propeller.app import Application
from propeller.request_handler import StaticFileHandler
from handlers.home import HomeHandler
from handlers.downloads import DownloadsHandler
from handlers.docs import DocsHandler
from handlers.benchmarks import BenchmarksHandler
from handlers.mailinglist import MailingListHandler


urls = (
    (r'^/$', HomeHandler),
    (r'^/downloads$', DownloadsHandler),
    (r'^/docs$', DocsHandler),
    (r'^/benchmarks$', BenchmarksHandler),
    (r'^/mailinglist$', MailingListHandler),
    (r'^/static/(.*)$', StaticFileHandler, {'static_path': '/var/www/propellerframework.org/static'}),
)

settings = {'urls': urls}

a = Application(**settings)
a.run()
