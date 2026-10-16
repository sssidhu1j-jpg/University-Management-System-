import os
import sys
import traceback

# Ensure backend and root directories are in Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

ROOT_DIR = os.path.dirname(BASE_DIR)
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

try:
    from django.core.wsgi import get_wsgi_application
    _django_application = get_wsgi_application()

    def application(environ, start_response):
        try:
            return _django_application(environ, start_response)
        except Exception:
            traceback.print_exc()
            err = traceback.format_exc()
            start_response("200 OK", [("Content-Type", "text/plain; charset=utf-8")])
            return [f"Django Runtime Exception on Vercel:\n\n{err}".encode("utf-8")]

except Exception:
    traceback.print_exc()
    err = traceback.format_exc()

    def application(environ, start_response):
        start_response("200 OK", [("Content-Type", "text/plain; charset=utf-8")])
        return [f"Django Startup Exception on Vercel:\n\n{err}".encode("utf-8")]

app = application
