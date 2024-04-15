from app import app, db
from models import Major, User
from werkzeug.security import generate_password_hash

with app.app_context():
    db.drop_all()
    db.create_all()

    # Initial loading of majors
    majors = ['Accounting', 'Finance', 'Information Systems', 'International Business', 'Management', \
              'Operations Management & Business Analytics', 'Supply Chain Management']
    for each_major in majors:
        print(f'{each_major} inserted into major')
        a_major = Major(major=each_major)
        db.session.add(a_major)
        db.session.commit()

    # Initial loading of users
    users = [
        # sample
        # --- USER: MANAGER - Daya
        {'username': 'admin', 'email': 'admin@umd.edu', 'first_name': 'Daya', 'last_name': 'Novich',
         'password': generate_password_hash('adminpw', method='pbkdf2:sha256'), 'role': 'ADMIN'},

        # --- USER: EMPLOYEE - TBD
        {'username': 'manager', 'email': 'manager@umd.edu', 'first_name': 'Joe', 'last_name': 'King',
         'password': generate_password_hash('managerpw', method='pbkdf2:sha256'), 'role': 'MANAGER'},

        # --- USER: CUSTOMER
        {'username': 'customer', 'email': 'vlee791@terpmail.umd.edu', 'first_name': 'Victor', 'last_name': 'Lee',
         'password': generate_password_hash('customerpw', method='pbkdf2:sha256'), 'role': 'STUDENT'},

        {'username': 'customer2', 'email': 'rsmi123@terpmail.umd.edu', 'first_name': 'Robert', 'last_name': 'Smith',
         'password': generate_password_hash('customerpw2', method='pbkdf2:sha256'), 'role': 'STUDENT'}
    ]

    for each_user in users:
        print(f'{each_user["username"]} inserted into user')
        a_user = User(username=each_user["username"], email=each_user["email"], first_name=each_user["first_name"],
                      last_name=each_user["last_name"], password=each_user["password"], role=each_user["role"])
        db.session.add(a_user)
        db.session.commit()
