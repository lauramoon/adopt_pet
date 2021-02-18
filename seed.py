"""Seed file to make sample data for db."""

from models import Pet, db 
from app import app

db.drop_all()
db.create_all()

pet1 = Pet(name='Woofly', species='dog', 
           photo_url='https://cdn.pixabay.com/photo/2016/07/15/15/55/dachshund-1519374_960_720.jpg', 
           age=1)
pet2 = Pet(name='Porchetta', species='porcupine', 
           photo_url='https://cdn.pixabay.com/photo/2018/08/06/23/32/nature-3588682_960_720.jpg')
pet3 = Pet(name='Tigger', species='cat', 
           photo_url='https://cdn.pixabay.com/photo/2015/11/16/22/14/cat-1046544_960_720.jpg', age=10)
pet4 = Pet(name='Fluffy', species='dog', age=2)
pet5 = Pet(name='Mia', species='cat', 
           photo_url='https://cdn.pixabay.com/photo/2016/07/10/21/47/cat-1508613_960_720.jpg')
pet6 = Pet(name='Porky', species='porcupine', age=6, available=False)

db.session.add_all([pet1, pet2, pet3, pet4, pet5, pet6])
db.session.commit()