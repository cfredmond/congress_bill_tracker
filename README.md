# Congress Bill Tracker

Congress Bill Tracker is a Django application that retrieves and stores information about bills from the Congress.gov API. It provides a simple way to track and analyze congressional bills and their latest actions.

## Features

- Retrieves bill data from the Congress.gov API
- Stores bill information in a database
- Provides a user-friendly web interface to view the data

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/congress-bill-tracker.git
   cd congress-bill-tracker
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate  # For Windows
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```
   python manage.py migrate
   ```

5. Retrieve bill data from the Congress.gov API:

   ```
   python manage.py runcrons --force
   ```

   This command will fetch the latest bill data from the API and store it in the database.

6. Start the development server:

   ```
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://localhost:8000`.

## Configuration

- Update the `SECRET_KEY`, `DEBUG`, and `CONGRESS_GOV_API_KEY` settings in the `.env` file.

## Usage

- Use the web interface to browse and search for bills.
- Filter bills by congress, bill type, chamber, or other criteria.
- Click on a bill to view its details, including the latest action.
- Use the Django admin interface to manage bills and latest actions.