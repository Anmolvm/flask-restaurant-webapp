from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

restaurantOne = Restaurant(name = "Pasta PLace")

session.add(restaurantOne)
session.commit()
session.query(Restaurant).all()

pasta = MenuItem(name = "Aglio Oglio", course = "Entree", description = "Pasta aglio oglio", price = "Rs. 7.50", restaurant = restaurantOne)

session.add(pasta)
session.commit()
session.query(MenuItem).all()
