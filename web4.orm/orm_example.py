from models.db_session import create_session, global_init
from models.user import User
from models.news import News


global_init("sqlite:///db/blogs.db")
session = create_session()

# создание пользователя
"""
user = User()
user.name = "Пользователь 2"
user.about = "Биография пользователя 2"
user.email = "email2@gmail.com"

session.add(user)
session.commit()
"""
# получить всех пользователей
users = session.query(User).all()
for user in users:
    print(user.name, user.email, user.created_date, user.about)


# пример с where
user = session.query(User).filter(User.id == 2)[0]
print(user.name, user.email, user.created_date, user.about)