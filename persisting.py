from models import User, Comment
from main import session

ivan = User(
    username = 'Ivan',
    email_address = 'ivankaz9@yandex.ru',
    comments = [
        Comment(text = 'Это мой первый комментарий!'),
        Comment(text = 'Это мой второй комментарий!')
    ]
)

john = User(
    username = 'John',
    email_address = 'john@google.com',
    comments = [
        Comment(text = 'Это комментария Джона')
    ]
)

session.add_all([ivan, john])

session.commit()
