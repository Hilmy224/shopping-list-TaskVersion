[Link to the Application](https://hilmy-shoppping-list.adaptable.app)

## Setup Django
### Set up a directory and use a virtual environment:
Create a new directory for your project. Set up a virtual environment using tools like venv or virtualenv. A virtual environment isolates the dependencies of your project from the system Python environment, ensuring consistency and avoiding conflicts with other projects. This step is important because different projects may require different versions of libraries and packages.

### Install necessary tools and libraries:
Create a requirements.txt file that lists all the libraries and packages required for your Django project. You can install these dependencies using the pip package manager by running pip install -r requirements.txt. Make sure to regularly update this file as your project evolves and new dependencies are added.

###Run the django-admin command to create a new Django app:
Open a terminal or command prompt and navigate to your project directory.
Run the following command to create a new Django app: django-admin startapp appname. Replace appname with the desired name for your app.

### Set the allowed hosts in the settings.py file:
Open the settings.py file located in your project folder.
Locate the ALLOWED_HOSTS variable and add the appropriate host names or IP addresses that are allowed to access your Django app. This step is necessary for security reasons, as it helps prevent unauthorized access.
Create a .gitignore file:
Create a .gitignore file in the root directory of your project.
Add the necessary details to ignore files and directories that are not required to be tracked by version control. This usually includes files like database files, generated files, and sensitive information.

### Link your project to a GitHub repository:
Create a new repository on GitHub.
Initialize a Git repository in your project directory using the command git init.
Add your project files to the Git repository using git add ..
Commit the changes using git commit -m "Initial commit".
Set the remote origin to your GitHub repository using git remote add origin <repository-url>.
Push the code to the remote repository using git push -u origin master.

### Connect your app to an adaptable account:
This step is not clear from the provided search results. Please provide more specific information or requirements related to connecting your app to an adaptable account.
Create the MVT (Model-View-Template) structure:
Ensure that your virtual environment is activated.
Use the startapp command to create a new Django app within your project. For example: python manage.py startapp main.
Update the INSTALLED_APPS list in the settings.py file to include the newly created app.
Create a templates folder inside the app directory and add HTML templates for your web pages.
Customize the HTML templates to suit your needs. You can use Django template tags and filters to dynamically render data in the templates.

### Define models for the database:
Open the models.py file inside your app directory.
Define the necessary models using Django's model fields and relationships. Models represent database tables and their relationships.
Run the migration command (python manage.py makemigrations and python manage.py migrate) to create or update the database schema based on your models.

### Connect views and templates:
Open the views.py file inside your app directory.
Define view functions or classes that handle HTTP requests and render templates.
Use the Django template system to connect the views with the corresponding HTML templates.
Create URL patterns in the urls.py file inside your app directory to map URLs to the appropriate view functions or classes.
