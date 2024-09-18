from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey


Base = declarative_base()

# Item Model (table for home inventory items)
class Item (Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key = True)
    name = Column (String, nullable = False)   #cannot have null values
    value = Column (Float, nullable= False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable = False)
    purchase_date = Column(Date, nullable = False)


    # table relationships(items table and category table)
    category = relationship("Category", back_populates = "items")

    # relationship between Claims table and items table
    claims = relationship("Claim", back_populates = "items")

    def __repr__(self):                  # repr method for defining an instance of the class Item (creating object)
        return f" <Item(name = {self.name}, value = {self.value}, category = {self.category.name}, purchase_date = {self.purchase_date})>"


# table 2- categories table

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key = True)
    name  = Column (String, nullable = False)

    # table relationship (items table)
    items = relationship("Item", back_populates = "category")

    def __repr__(self):
        return f"<Category(name = {self.name})>"




# the SQLite database
def setup_database():
    engine = create_engine('sqlite:///home_database.db')
    Base.metadata.create_all(engine)
