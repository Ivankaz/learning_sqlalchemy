from main import session
from models import User, Comment
from sqlalchemy import select

# get one user's comment
"""
statement = select(Comment).join(Comment.user).where(
    User.username == 'Ivan'
).where(
    Comment.text == 'Это мой второй комментарий!'
)

result = session.scalars(statement).one()

print(result)
"""

# get all comments with users
statement = select(Comment).join(Comment.user)

result = session.scalars(statement).all()

print(result)
