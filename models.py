from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
#from sqlalchemy.orm import sessionmaker


Base = declarative_base()

# Item Model (table for home inventory items)
class Item (Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key = True)
    name = Column (String, nullable = False)   #cannot have null values
    value = Column (Float, nullable= False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable = False)
    purchase_date = Column(Date, nullable = False)
    claims = relationship('Claim', primaryjoin="Item.id == Claim.item_id")


    # table relationships(items table and category table)
    category = relationship("Category", back_populates = "items")

    # relationship between Claims table and items table
    claims = relationship("Claim", back_populates = "item")

    def __repr__(self):                  # repr method for defining an instance of the class Item (creating object)
        return f" <Item(name = {self.name}, value = {self.value}, category = {self.category.name}, purchase_date = {self.purchase_date})>"


# Category Model (table 2- categories table)

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key = True)
    name  = Column (String, nullable = False)

    # table relationship (items table)
    items = relationship("Item", back_populates = "category")

    def __repr__(self):
        return f"<Category(name = {self.name})>"

# table 3: InsurancePolicy model(table)
class InsurancePolicy(Base):
    __tablename__ = "InsurancePolicies"

    id = Column(Integer, primary_key = True)
    policy_number = Column(String, nullable = False)
    provider = Column (String, nullable = False)
    start_date = Column(Date, nullable = False)
    end_date = Column (Date, nullable = False)
    premium_amount = Column(Float, nullable = False)


    def __repr__(self):
        return f" <InsurancePolicy(policy_number = {self.policy_number}, provider = {self.provider}, start_date = {self.start_date}, end_date = {self.end_date}, premium_amount = {self.premium_amount})>"
    
# table 4 - Claims table:
class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key = True)
    claim_number = Column(String, nullable =  False)
    status = Column (String, nullable = False)
    payout_amount = Column(Float)
    date_filed = Column(Date, nullable = False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable = False)

     #foreign key
    item_id = Column(Integer, ForeignKey("items.id"), nullable = False)

    # table relationship (items table)

    item = relationship("Item", back_populates = "claims")

   

    def __repr__(self):
        return f"<Claim(claim_number = {self.claim_number}, status = {self.status}, payout_amount = {self.payout_amount})>"



# the SQLite database
def setup_database():
        engine = create_engine('sqlite:///home_database.db')
        Base.metadata.create_all(engine)
if __name__ == '__main__':
    setup_database()
    print("Setup Complete")        


