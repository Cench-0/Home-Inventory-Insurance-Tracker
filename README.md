
### Home Inventory & Insurance Tracker

Project Overview:
The Home Inventory & Insurance Tracker is a CLI tool designed to help homeowners manage their home assets, track insurance policies, and handle insurance claims. Users can add, edit, and categorize their home items, update their insurance records, and file claims for damaged or lost items. This tool utilizes a database to store all the information, providing efficient asset and insurance management.

## Features:
# Item Management
Users can add, edit, and remove items in their home inventory. Each item has a name, value, category, and purchase date.

# Insurance Policy Management
Users can update their insurance policy details to reflect their current coverage for items.

# Claims Management
Users can file claims for items and track the status of their claims (e.g., pending, approved, denied).

# Item Categorization
Users can categorize their items (e.g., furniture, electronics) to better organize their inventory.

## Technology
1. SQLAlchemy ORM: Used for managing the database, making it easier to interact with data through Python objects.
2. Alembic: Used for database migrations, which manage changes to the database schema over time.
3. Pipenv: Used for managing the project’s virtual environment and dependencies.
4. Python: Main language for the command-line interface (CLI) and database interactions.

## How to Install and Run the Project:
Clone the Repository:

git clone <https://github.com/Dev-Divaa/Home-Inventory-Insurance-Tracker>

cd Home-Inventory-Insurance-Tracker

Set Up the Virtual Environment Using Pipenv:

pip install pipenv
pipenv install
pipenv shell
Install Dependencies: All required libraries, including SQLAlchemy and Alembic, will be installed through the Pipfile.

pipenv install sqlalchemy alembic
Initialize the Database: Initialize your SQLite database using Alembic.

# alembic init migrations
Run Migrations: After creating your models (which we will guide you through), apply migrations to create your database schema.

alembic revision --autogenerate -m "Create initial tables"
alembic upgrade head

## Run the CLI:

Build your models first (Items, Insurance Policies, Claims, Categories).
Set up Alembic migrations to manage your schema changes.
Create the CLI functions to add, update, delete, and view items, policies, and claims.
