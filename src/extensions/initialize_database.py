from src.model.role import Role
from src.model.user import User
from src.extensions.extensions import bcrypt, db

def initialize_database():
    db.create_all()

    roles = Role.query.all()
    if not roles:
        role1 = Role(name="ROLE_ADMIN")
        role2 = Role(name="ROLE_USER")
        db.session.add_all([role1, role2])
        db.session.commit()

