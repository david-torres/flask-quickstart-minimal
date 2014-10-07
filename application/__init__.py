from flask import Flask
from application.config import DevelopmentConfig
from application.config import ProductionConfig
import os

# init app
app = Flask(__name__)

# check APP_ENV environment variable and load the approprite config
if 'APP_ENV' in os.environ and os.environ['APP_ENV'] == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

import controllers
