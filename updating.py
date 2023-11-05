from main import session
from models import User, Comment

comment = session.query(Comment).filter_by(id = 16).first()

if comment:
    comment.text = 'This is an updated comment'

    session.commit()
else:
    print('Comment not found')
