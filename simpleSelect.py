from main import session
from models import User, Comment
from sqlalchemy import select

users = session.query(User).all()

# select all users
for user in users:
    print(user)

# select users with condition
statement = select(User).where(User.username.in_(['ivan', 'test']))

result = session.scalars(statement)

for user in result:
    print(user)
