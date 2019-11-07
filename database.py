from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def Add_Product(name, price, picture_link, description)
	product_object = Product(
        Name=name,
        Price=price,
        Picture_Link=picture_link,
        Description=description)
    session.add(product_object)
    session.commit()


Add_Product("Olive Pizza", 15.99, "https://slice.seriouseats.com/images/2011/08/20110822-olives-poll-way-or-no-way.jpg", "Best Olive Pizza in the Area")




