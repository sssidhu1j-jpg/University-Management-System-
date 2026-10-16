import os
import sys
import traceback

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    from config.wsgi import app
except Exception:
    err = traceback.format_exc()
    def app(environ, start_response):
        start_response("200 OK", [("Content-Type", "text/plain; charset=utf-8")])
        return [f"Index Startup Exception on Vercel:\n\n{err}".encode("utf-8")]
