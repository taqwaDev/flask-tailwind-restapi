import os
import logging

from flask import Flask, request, jsonify, render_template, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

template_dir = os.path.abspath(os.getcwd())
template_dir = os.path.join(template_dir, 'templates')
template_dir2 = os.path.join(template_dir, 'public')


def create_app():

    app = Flask(__name__, template_folder=template_dir,
                static_folder=template_dir2)
    basedir = os.path.abspath(os.getcwd())
    # basedir = os.path.abspath(os.path.dirname(__file__))
    app.logger.info(basedir)
    app.logger.info("test")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        os.path.join(basedir, 'test.db')

    from .model import db, ma
    db.init_app(app)
    ma.init_app(app)

    @app.route('/', methods=['GET'])
    def status():
        return render_template('index.html')

    # letakan router disini
    from .route.api import api as api_route
    # register api router
    app.register_blueprint(
        api_route,
        url_prefix='/api/v1'
    )

    return app
