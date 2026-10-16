import os
import sys
import traceback

# Add backend directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.abspath(os.path.join(current_dir, "..", "backend"))

if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

try:
    from django.core.wsgi import get_wsgi_application
    app = get_wsgi_application()
except Exception as e:
    traceback.print_exc()
    error_msg = traceback.format_exc()

    def app(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain; charset=utf-8')]
        start_response(status, headers)
        return [f"Django startup exception on Vercel:\n\n{error_msg}".encode('utf-8')]
