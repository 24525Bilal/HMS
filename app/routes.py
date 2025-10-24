# This file defines all the URLs for your application
# (e.g., '/', '/login', '/dashboard')

from flask import Blueprint, render_template
from flask_login import login_required, current_user # We'll use these later

# Create a Blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/index')
def index():
    # Renders the 'index.html' template
    return render_template('index.html')

@main_bp.route('/login')
def login():
    # Renders the 'login.html' template
    return render_template('login.html')

@main_bp.route('/register')
def register():
    # Renders the 'register.html' template
    return render_template('register.html')

@main_bp.route('/logout')
def logout():
    return "<h1>Logged Out (Placeholder)</h1>"


# --- DASHBOARD ROUTES ---

@main_bp.route('/admin_dashboard')
def admin_dashboard():
    # Renders the 'admin_dashboard.html' template
    return render_template('admin_dashboard.html')

@main_bp.route('/doctor_dashboard')
def doctor_dashboard():
    # Renders the 'doctor_dashboard.html' template
    return render_template('doctor_dashboard.html')

@main_bp.route('/patient_dashboard')
def patient_dashboard():
    # Renders the 'patient_dashboard.html' template
    return render_template('patient_dashboard.html')