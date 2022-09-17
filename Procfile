web: gunicorn main:main --workers 6 --threads 6 --bind 0.0.0.0:$PORT --timeout 864000 --worker-class aiohttp.GunicornWebWorker & python -m bot
