from models.database import engine, Base, SessionLocal
from models.user import User
from models.child import Child
from models.logs import Log
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_tables():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)

def create_admin_user():
    db = SessionLocal()
    existing_admin = db.query(User).filter(User.email == "admin@example.com").first()
    if not existing_admin:
        admin = User(
            full_name="Admin User",
            email="admin@example.com",
            hashed_password=pwd_context.hash("admin123"),
            role="admin"
        )
        db.add(admin)
        db.commit()
        print("Admin user created!")
    else:
        print("Admin user already exists.")
    db.close()

if __name__ == "__main__":
    create_tables()
    create_admin_user()
