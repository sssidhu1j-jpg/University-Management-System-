import os
import sys
import shutil
import traceback

# Add backend directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
backend_dir = os.path.abspath(os.path.join(root_dir, "backend"))

for path in [backend_dir, root_dir]:
    if path not in sys.path:
        sys.path.insert(0, path)

# On Vercel, copy db.sqlite3 to /tmp so it is writable
tmp_db = "/tmp/db.sqlite3"
if not os.path.exists(tmp_db):
    for candidate in [
        os.path.join(backend_dir, "db.sqlite3"),
        os.path.join(root_dir, "db.sqlite3"),
    ]:
        if os.path.exists(candidate):
            try:
                shutil.copyfile(candidate, tmp_db)
                break
            except Exception:
                pass

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

try:
    from django.core.wsgi import get_wsgi_application
    _django_app = get_wsgi_application()

    def app(environ, start_response):
        try:
            return _django_app(environ, start_response)
        except Exception:
            traceback.print_exc()
            error_msg = traceback.format_exc()
            status = '500 Internal Server Error'
            headers = [('Content-Type', 'text/plain; charset=utf-8')]
            start_response(status, headers)
            return [f"Django runtime exception on Vercel:\n\n{error_msg}".encode('utf-8')]

except Exception:
    traceback.print_exc()
    error_msg = traceback.format_exc()

    def app(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain; charset=utf-8')]
        start_response(status, headers)
        return [f"Django startup exception on Vercel:\n\n{error_msg}".encode('utf-8')]
