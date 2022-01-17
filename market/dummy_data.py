from market.models import db
from market.models import Item
from market.models import User
db.drop_all()
db.create_all()

item1= Item(name= 'phone', barcode='123456789012', price=500, describtion='personal phone')
item2= Item(name= 'laptop', barcode='987654321011', price=1500, describtion='personal computer')

user1= User(user_name='hossam', email_address='hossam@outlook.com',password_hash='12345')

db.session.add(item1)
db.session.commit()
db.session.add(item2)
db.session.commit()
Item.query.all()

for item in Items.query.all():
    item.name

for item in Item.query.filter_by(price=500):
    item.name