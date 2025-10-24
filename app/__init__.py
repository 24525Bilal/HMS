# This file initializes your Flask application
# and brings all the pieces together.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Load configuration
    app.config['SECRET_KEY'] = 'a_very_secret_key'
    
    # Define the SQLite database path
    # It will be in the 'instance' folder
    db_path = os.path.join(app.instance_path, 'hospital.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize extensions with the app
    db.init_app(app)
    login_manager.init_app(app)
    
    # Configure Flask-Login
    login_manager.login_view = 'main.login' 
    login_manager.login_message_category = 'info' 

    with app.app_context():
        # Import routes
        from . import routes
        app.register_blueprint(routes.main_bp)

        # Import models to ensure they are known to SQLAlchemy
        from . import models

        # Create database tables
        # This satisfies the "programmatic creation" requirement
        db.create_all() 
        
        # Call the function to create the admin user
        models.create_admin()

        return app