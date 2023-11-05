from main import session
from models import User

ivan = session.query(User).filter_by(username = 'Ivan').first()

print(ivan)
