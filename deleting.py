from main import session
from models import User, Comment

comment = session.query(Comment).filter_by(id = 16).first()

if comment:
    session.delete(comment)
    session.commit()
else:
    print('Comment not found')
