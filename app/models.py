# This file defines your database tables (models).

from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='patient') # 'patient', 'doctor', 'admin'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# We will add the other models (Doctor, Patient, Appointment) here later.
# For now, this is enough to get the app running.

# --- FUNCTION TO CREATE PRE-EXISTING ADMIN ---
def create_admin():
    admin_user = User.query.filter_by(role='admin').first()
    if not admin_user:
        print("Creating admin user...")
        admin_user = User(
            username='admin',
            email='admin@hospital.com',
            role='admin'
        )
        admin_user.set_password('admin123') 
        db.session.add(admin_user)
        try:
            db.session.commit()
            print("Admin user created successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"Error creating admin user: {e}")