import os
import logging
import sys

from flask import Flask, redirect, request, session
from flask.logging import create_logger
from pyga.requests import Tracker, Page, Session, Visitor
from urllib.parse import urlparse

app = Flask(__name__)
logger = create_logger(app)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    logger.handlers = gunicorn_logger.handlers
    logger.setLevel(gunicorn_logger.level)


redirect_type = int(os.environ.get('REDIRECT_TYPE', '302'))
redirect_target = os.environ.get(
    'REDIRECT_TARGET', 'https://www.pioneera.com/')
google_analytics = os.environ.get('GA', None)
listening_port = int(os.environ.get('PORT', 8080))

logger.info('Adding redirection handling to target %s with code %d',
            redirect_target, redirect_type)

if google_analytics:
    logger.info('Logging to Google Analytics as %s',
                google_analytics)


def log_traffic(base_url, ip, user_agent=None):
    if not google_analytics:
        return
    url = urlparse(base_url)
    logger.info(
        'Logging GA traffic from %s to host %s with page %s', ip, url.hostname, url.path)
    tracker = Tracker(google_analytics, url.hostname)
    pyga_visitor = Visitor()
    pyga_visitor.ip_address = ip
    if user_agent:
        pyga_visitor.user_agent = user_agent
    pyga_session = Session()
    pyga_page = Page(url.path)
    try:
        tracker.track_pageview(pyga_page, pyga_session, pyga_visitor)
    except:
        logger.error('Unable to connect to analytics')
        logger.error(sys.exc_info()[0])


@app.route('/')
def root():
    log_traffic(request.base_url, request.access_route[0], request.user_agent)
    return redirect(redirect_target, code=redirect_type)


@app.route('/<path:page>')
def anypage(page):
    log_traffic(request.base_url, request.access_route[0], request.user_agent)
    return redirect('{new_url}#{page}'.format(page=page, new_url=redirect_target), code=redirect_type)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=listening_port)
