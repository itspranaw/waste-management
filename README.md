## Installation

To run this project locally, follow these steps:

1. Clone this repository to your local machine.

   ```
   git clone <repository-url>
   ```
   and go inside it using cd waste-management

2. Create a virtual environment and activate it.

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the project dependencies.

   ```
   pip install -r requirements.txt
   ```
   then go inside the waste_management (use cd waste_management)
   
5. Set up the Django database and run migrations.

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser account to access the admin panel.

   ```
   python manage.py createsuperuser
   ```
   you will be asked admin: email: password: etc give whatever you want can leave email also no issue

7. Start the development server.

   ```
   python manage.py runserver
   ```

8. Access the admin panel at `http://localhost:8000/admin/` and use your superuser credentials to log in.

## Usage

Once the project is set up and the server is running, users can access the Waste Management System through the web interface. Different user types (customers, waste collectors, and administrators) will have access to their respective functionalities.

## License

This project is licensed under the [MIT License](LICENSE).
