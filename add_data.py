#
#   Author  : Anjani Suresh Bhat
#   Date    : August 2016
#
#   This file add initial items to database
#
#

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_base import Base, Items

app = Flask(__name__)

engine = create_engine('sqlite:///item_list.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

tshirt1 = Items(name = "Avengers Tshirt", picture = "http://ep.yimg.com/ay/stylinonline/avengers-black-widow-assemble-logo-juniors-t-shirt-11.jpg", price ="25$", type_item = "Clothes", description = "Avengers 1 logo", brand_name = "levis")
tshirt2 = Items(name = "Batman Tshirt", picture="http://images.sportsdirect.com/images/imgzoom/59/59839703_xxl.jpg", price= "26$", type_item = "Clothes", description = "dark knight rises", brand_name = "adidas")
mobile1 = Items(name = "S6 Edge", picture = "http://newdaypost.com/wp-content/uploads/2015/07/Galaxy-S6-Edge-3.jpg", price = "700$", type_item = "Electronics", description = "New Unlocked", brand_name = "samsung")
mobile2 = Items(name = "Nexus 4", picture = "http://www.lg.com/uk/images/lg-mobile-phones/e960/gallery/medium06.jpg", price = "280$", type_item = "Electroincs", description = "New Unlocked 2008 edition", brand_name = "LG")
book1 = Items(name = "Wings of Fire", picture = "https://upload.wikimedia.org/wikipedia/en/3/3a/Wings_of_Fire_by_A_P_J_Abdul_Kalam_Book_Cover.jpg", price = "70$", type_item = "Books", description = "New Edition", brand_name = "MES Publishers")
book2 = Items(name = "Game of Thrones", picture = "http://i.lv3.hbo.com/custom-assets/img/free-episodes/game-of-thrones-1349.jpg", price = "80$", type_item = "Books", description  = "Second Book", brand_name = "GOT")

session.add(tshirt1)
session.add(tshirt2)
session.add(mobile1)
session.add(mobile2)
session.add(book1)
session.add(book2)

session.commit()
c = session.query(Items).all()
for x in c:
        print(x.name)