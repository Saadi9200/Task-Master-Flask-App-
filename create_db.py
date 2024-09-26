from app import db,app
print("Creating database and tables...")
with app.app_context():
    db.create_all()
    print(db.create_all)
    print("Database and tables created.")