import os
from flask_cors import CORS, cross_origin


def init_cors():
    frontend = os.getenv('FRONTEND_URL')
    backend = os.getenv('BACKEND_URL')
    origins = [frontend, backend]
    cors = CORS(
    app,
    resources={r"/api/*": {"origins": origins}},
    headers=['Content-Type', 'Authorization'],
    expose_headers='Authorization',
    methods="OPTIONS,GET,HEAD,POST"
    )