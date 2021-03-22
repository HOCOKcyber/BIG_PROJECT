from flask import Flask
from dotenv import load_dotenv
import os
from data import db_session
from data.users import User

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('KEY')


def main():
    db_session.global_init('db/blogs.db')
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'

#    user.surname = "D"
#    user.name = "Alex"
#    user.age = 19
#    user.position = 'worker'
#    user.speciality = 'engineer'
#    user.address = 'module_2'
#    user.email = 'D_D@mars.org'
#
#    user.surname = "B"
#    user.name = "LIl"
#    user.age = 20
#    user.position = 'worker'
#    user.speciality = 'medic'
#    user.address = 'module_2'
#    user.email = 'B_lil@mars.org'
#
#    user.surname = "F"
#    user.name = "Pudge"
#    user.age = 30
#    user.position = 'hoooker'
#    user.speciality = 'cooker'
#    user.address = 'module_4'
#    user.email = 'Pudge_ru@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()

