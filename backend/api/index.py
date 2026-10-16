import os
import sys
import traceback

# Add backend directory to sys.path
api_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.dirname(api_dir)

if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

try:
    from config.wsgi import app
except Exception:
    err = traceback.format_exc()
    def app(environ, start_response):
        start_response("200 OK", [("Content-Type", "text/plain; charset=utf-8")])
        return [f"Backend API Startup Exception on Vercel:\n\n{err}".encode("utf-8")]
