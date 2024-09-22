
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Base, Claim, Item, Category, InsurancePolicy, setup_database
from datetime import datetime



#SQLite engine
engine = create_engine("sqlite:///home_database.db")
Session = sessionmaker(bind = engine)
session = Session()





def add_category(name):
    #add a new category
    category = Category(name = name)
    session.add(category)
    session.commit()
    print(f"Category '{name}' added successfully")

def add_item(name, value, category_name, purchase_date):
    # add a new item to the inventory
    category = session.query(Category).filter_by(name = category_name).first()

    if not category:
        print (f"Category '{category_name}' not found")
        category = Category(name = category_name)
        session.add(category)
        session.commit()
        print(f"Category '{category_name}' added")

    # create the item
    item = Item(name = name, value = value, category_id = category.id, purchase_date = purchase_date)
    session.add(item)
    session.commit()
    print (f"Item '{name}' added successfully")



def view_items()    :
    items = session.query(Item). all()
    if not items:
        print ("No items found")
    else:
        for item in items:
            print (f"Item ID: {item.id}, Name: {item.name}, Value: {item.value},Category: {item.category.name}, Purchase Date: {item.purchase_date}") 


def update_item(item_id, new_name=None, new_value=None, new_category_name=None, new_purchase_date=None):

    item = session.query(Item).filter_by(id = item_id).first()
    if not item:
        print(f"Item with ID {item_id} not found")
        return

# when we have new values
    if new_name:
        item.name = new_name
    if new_value:
        item.value = new_value
    if new_category_name:
        category = session.query(Category).filter_by(name = new_category_name).first()
        if category:
            item.category_id = category.id
        else:
            print(f"Category '{new_category_name}' not found")    
            return
    if new_purchase_date:
        item.purchase_date = new_purchase_date

    session.commit()    
    print(f"Item '{item_id}' updated successfully")


def delete_item(item_id):
    item = session.query(Item).filter_by(id = item_id).first()
    if not item:
        print(f"Item with ID {item_id} not found")
        return
    session.delete(item)
    session.commit()
    print(f"Item '{item.name}' deleted")

def add_insurance_policy(policy_number, provider, start_date, end_date, premium_amount):
    policy = InsurancePolicy(
        policy = policy_number,
        provider = provider,
        start_date = start_date,
        end_date = end_date,
        premium_amount = premium_amount
    )
    session.add(policy)
    session.commit()
    print(f"Insurance policy '{policy_number}' added successfully")

def view_policies():
    policies = session.query(InsurancePolicy).all()    
    if not policies:
        print("No policies found")
    else:
        for policy in policies:
            print(f"Policy Number: {policy.policy_number}, Provider: {policy.provider}, Start Date: {policy.start_date}, End Date: {policy.end_date}, Premium: {policy.premium_amount}")
def file_claim(item_id, claim_number, status,payout_amount, filed_date):
    item = session.query(Item).filter_by(id = item_id).first()
    if not item:
        print(f"Item with ID {item_id} not found")
        return
    claim = Claim(
        item_id = item_id,
        claim_number = claim_number,
        status = status,
        payout_amount = payout_amount,
        date_filed = filed_date
    )
    session.add(claim)
    session.commit()
    print(f"Claim '{claim_number}' filed")

def view_claims():

    claims = session.query(Claim).all()
    if not claims:
        print("No claims")
    else:
        for claim in claims:
            print(f"Claim Number: {claim.claim_number}, Item: {claim.item.name}, Status: {claim.status}, Payout: {claim.payout_amount}, Filed Date: {claim.date_filed}")

def main_menu():
    while True:
        print("\nHome Inventory & Insurance Tracker")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Add Insurance Policy")
        print("6. View Insurance Policies")
        print("7. File Claim")
        print("8. View Claims")
        print("9. Exit")


        choice = input("Choose Option: ")

        if choice == "1":
            name = input("Enter name of item: ")
            value = float(input("Enter item value:"))
            category_name = input("Enter category:")
            purchase_date = datetime.strptime(input("Enter date of purchase (YYYY - MM - DD)"), '%Y-%m-%d')
            add_item(name, value, category_name,purchase_date)

        elif choice == "2":
            view_items()

        elif choice == "3":
            item_id = int(input("Enter item ID:"))
            new_name = input("New name or press enter to continue:") or None
            new_value = input("New Value or press enter to continue:") or None
            new_category_name = input("New category name or press enter to continue:") or None
            new_purchase_date = input("New purchase date or press enter to continue:")

            if new_value:
                new_value = float(new_value)
            if new_purchase_date:
                new_purchase_date = datetime.strptime(new_purchase_date, '%Y-%m-%d')
        
            update_item(item_id, new_name, new_value, new_category_name, new_purchase_date)
        elif choice == "4":
            item_id = int(input("Enter item ID to delete: "))
            delete_item(item_id)

        elif choice == "5":
            policy_number  = input("Policy number:")
            provider = input ("Enter provider:")
            start_date = datetime.strptime(input("Enter start date (YYYY-MM-DD):"), '%Y-%m-%d')
            end_date = datetime.strptime(input("Enter end date (YYYY-MM-DD):"), '%Y-%m-%d')
            premium_amount = float(input("Enter amount"))
            add_insurance_policy(policy_number, provider, start_date, end_date, premium_amount)

        elif choice == "6":
            view_policies()

        elif choice == "7":
            item_id = int(input("Enter item ID for the claim: "))
            claim_number = input("Enter claim number: ")
            status = input("Enter claim status: ")
            payout_amount = float(input("Enter payout amount: "))
            filed_date = datetime.strptime(input("Enter filed date (YYYY-MM-DD): "), '%Y-%m-%d')
            file_claim(item_id, claim_number, status, payout_amount, filed_date)

        elif choice == "8":
            view_claims()

        elif choice == "9":
            print("Exiting...")    
            break
        else:
            print("Invalid choice")


if __name__ =="__main__":
    setup_database()

    #categoies examples
    # add_category("Electronics")


    main_menu()

    





    
                         




      