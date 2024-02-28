import sys
import os

# # Add the directory containing your Django project to the Python path
# sys.path.append('/home/actseminary/backend/ACTS_backend')

# # Set the DJANGO_SETTINGS_MODULE environment variable to the settings module for your project
# os.environ['DJANGO_SETTINGS_MODULE'] = 'ACTS_backend.settings'

# # Import the Django WSGI application
# from django.core.wsgi import get_wsgi_application

# # Create a WSGI application object that can be used by Phusion Passenger
# application = get_wsgi_application()

from ACTS_backend.wsgi import application