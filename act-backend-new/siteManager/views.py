import smtplib
import tempfile
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *


class ContactView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = ContactPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({'save': True})
        return Response({'save': False, 'message': serialized.errors})

    @staticmethod
    def get(request):
        queryset = Contact.objects.all()
        serialized = ContactGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


# {
#     "message": "This field is required.",
#     "name": "Michael",
#     "email": "mike@gmail.com"
# }

class ApplicationView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        print(data)
        serialized = ApplicationPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            # For sending an email of the application
            try:
                # Set up the SMTP server
                s_email = request.data['email']
                s_course = request.data['course']
                s_program = request.data['program']
                s_name = request.data['first_name'] + " " + request.data['last_name']
                s_message = "Application"

                smtp_server = "smtp.gmail.com"
                smtp_port = 587
                smtp_username = "michaelcyril71@gmail.com"
                smtp_password = "hcojkefeoctysmso"
                smtp_sender = s_email
                smtp_recipient = "michaelcyril71@gmail.com"

                # Create a message object
                message = MIMEMultipart()
                message['From'] = smtp_sender
                message['To'] = smtp_recipient
                message['Subject'] = 'APPLICATION EMAIL.'

                # Add a text message to the email
                text = "SENDER MESSAGE" + "\n" + s_message + '\n \n \n' + "APPLICANT INFORMATION" + "\n" + "Username: " + s_name + "\n" + "Email: " + s_email + "\n" + "Course: " + s_course + "\n" + "Program: " + s_program
                message.attach(MIMEText(text))

                # Connect to the SMTP server and send the email
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    server.sendmail(smtp_sender, smtp_recipient, message.as_string())

                # print()
                # return Response({'message': "Email sent successfully!"})
            except:
                # return Response({'message': "Authentication failed"})
                pass

            return Response({'save': True})
        return Response(serialized.errors)

    @staticmethod
    def get(request):
        queryset = Application.objects.all()
        serialized = ApplicationGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


class EventView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        print(data)
        serialized = EventPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({'save': True})
        return Response({'save': False, 'message': serialized.errors})

    @staticmethod
    def get(request):
        queryset = Event.objects.all()
        serialized = EventGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


class EventActions(APIView):
    @staticmethod
    def get(request, event_id):
        try:
            event = Event.objects.get(id=event_id)
            event.delete()
            return Response({'delete': True})
        except Event.DoesNotExist:
            return Response({'delete': False})

    @staticmethod
    def post(request, event_id):
        data = request.data
        try:
            event = Event.objects.get(id=event_id)
            event.title = data['title']
            event.description = data['description']
            event.date = data['date']
            event.time = data['time']
            event.save()
            return Response({'update': True})
        except Event.DoesNotExist:
            return Response({'update': False})


class SingleEvent(APIView):
    @staticmethod
    def get(request, event_id):
        event = Event.objects.get(id=event_id)
        return Response(EventGetSerializer(instance=event).data)


class DashboardView(APIView):
    @staticmethod
    def get(request):
        numberEvents = len(Event.objects.all())
        numberApplication = len(Application.objects.all())
        numberContact = len(Contact.objects.all())
        return Response(
            {'number_events': numberEvents, 'number_applications': numberApplication, 'number_contacts': numberContact})


class DeleteContact(APIView):
    @staticmethod
    def get(request, contact_id):
        try:
            contact = Contact.objects.get(id=contact_id)
            contact.delete()
            return Response({'delete': True})
        except:
            return Response({'delete': True})


class SendEmail(APIView):
    @staticmethod
    def post(request):
        try:
            # Set up the SMTP server
            s_email = request.data['email']
            s_name = request.data['name']
            s_message = request.data['message']
            uploaded_file = request.FILES['application_file']  # Replace 'file_field_name' with the actual field name

            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_file.read())
                temp_file_name = temp_file.name

            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            smtp_username = "michaelcyril71@gmail.com"
            smtp_password = "hcojkefeoctysmso"
            smtp_sender = s_email
            smtp_recipient = "michaelcyril71@gmail.com"

            # Create a message object
            message = MIMEMultipart()
            message['From'] = smtp_sender
            message['To'] = smtp_recipient
            message['Subject'] = 'EMAIL FROM CONTACT US.'

            # Attach the temporary file
            with open(temp_file_name, 'rb') as file:
                part = MIMEApplication(file.read(), Name=uploaded_file.name)
            part['Content-Disposition'] = f'attachment; filename={uploaded_file.name}'
            message.attach(part)

            # Add a text message to the email
            text = "SENDER MESSAGE" + "\n" + s_message + '\n \n \n' + "SENDER INFORMATION" + "\n" + "Username: " + s_name + "\n" + "Email: " + s_email
            message.attach(MIMEText(text))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(smtp_sender, smtp_recipient, message.as_string())

            print()
            return Response({'message': "Email sent successfully!"})
        except:
            return Response({'message': "Authentication failed"})

    # {
    #     "email": "erickshayo306@gmail.com",
    #     "name": "shayo",
    #     "message": "some demo"
    # }
