import smtplib
import tempfile
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.db.models import Sum
from rest_framework.permissions import AllowAny
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
    permission_classes = [AllowAny]

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
                smtp_username = "agbcgraduatestudies@gmail.com"
                smtp_password = "yslhqugkjkpdptlh"
                smtp_sender = s_email
                smtp_recipient = "agbcgraduatestudies@gmail.com"

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


            except Exception as e:
                return Response({'message': f"Email sending failed: {str(e)}"})

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
        numberCourse = len(Course.objects.all())
        numberStaff = len(Staff.objects.all())
        numberAdmin = len(Administration.objects.all())
        return Response(
            {'number_events': numberEvents,
             'number_applications': numberApplication,
             'number_contacts': numberContact,
             'number_course': numberCourse,
             'number_staff': numberStaff,
             'number_admin': numberAdmin
             })


class StaffView(APIView):

    @staticmethod
    def get(request):
        staff = Staff.objects.all()
        return


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
            smtp_username = "agbcgraduatestudies@gmail.com"
            smtp_password = "yslh qugk jkpd ptlh"
            smtp_sender = s_email
            smtp_recipient = "agbcgraduatestudies@gmail.com"

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


class CourseView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = CoursePostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        queryset = Course.objects.all()
        serialized = CourseGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


class DeleteUpdateCourseView(APIView):
    @staticmethod
    def post(request):
        # data = request.data
        pass

    @staticmethod
    def get(request):
        courseId = request.GET.get("id")
        course = Course.objects.get(id=courseId)
        course.delete()
        return Response({"delete": True})


class StuffView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = StaffPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        queryset = Staff.objects.all()
        serialized = StaffGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


class DeleteUpdateStuffView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        try:
            staff = Staff.objects.get(id=data['id'])
            staff.full_name = data['full_name']
            staff.titles = data['titles']
            staff.education = data['education']
            staff.save()
            return Response({'update': True})
        except:
            return Response({'update': False})

    @staticmethod
    def get(request):
        stuffId = request.GET.get("id")
        stuff = Staff.objects.get(id=stuffId)
        stuff.delete()
        return Response({"delete": True})


class AdministrationView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = AdministrationPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        queryset = Administration.objects.all()
        serialized = AdministrationGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


class DeleteUpdateAdministrationView(APIView):
    @staticmethod
    def post(request):
        # data = request.data
        pass

    @staticmethod
    def get(request):
        adminId = request.GET.get("id")
        admin = Administration.objects.get(id=adminId)
        admin.delete()
        return Response({"delete": True})


class MastersCostTableView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = MastersCostTablePostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        type = request.GET.get('type')
        queryset = MastersCostTable.objects.filter(type=type)
        total = MastersCostTable.objects.filter(type=type).aggregate(total=Sum('total_price'))['total']
        serialized = MastersCostTableGetSerializer(instance=queryset, many=True)
        return Response({'total': total, 'data': serialized.data})


class DeleteUpdateMastersCostTableView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        try:
            mct = MastersCostTable.objects.get(id=data['id'])
            mct.description = data['description']
            mct.units = data['units']
            mct.price_per_unit = data['price_per_unit']
            mct.total_price = data['total_price']
            mct.type = data['type']
            mct.save()
            return Response({'update': True})
        except:
            return Response({'update': False})

    @staticmethod
    def get(request):
        id = request.GET.get("id")
        mct = MastersCostTable.objects.get(id=id)
        mct.delete()
        return Response({"delete": True})


class PhdCostTableView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = PhdCostTablePostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        id = request.GET.get("id")
        course = Course.objects.get(id=id)
        queryset = PhdCostTable.objects.filter(course=course)
        total = PhdCostTable.objects.filter(course=course).aggregate(total=Sum('amount'))['total']
        serialized = PhdCostTableGetSerializer(instance=queryset, many=True)

        return Response(
            {'total': total, 'data': serialized.data, 'course': CourseGetSerializer(instance=course, many=False).data})


class DeleteUpdatePhdCostTableView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        try:
            pct = PhdCostTable.objects.get(id=data['id'])
            pct.course = data['course']
            pct.description = data['description']
            pct.amount = data['amount']
            pct.save()
            return Response({'update': True})
        except:
            return Response({'update': False})

    @staticmethod
    def get(request):
        id = request.GET.get("id")
        pct = PhdCostTable.objects.get(id=id)
        pct.delete()
        return Response({"delete": True})


class ImportantInformationView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = ImportantInformationPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        queryset = ImportantInformation.objects.all()
        serialized = ImportantInformationGetSerializer(instance=queryset, many=True)
        return Response(serialized.data[0])


class DeleteUpdateImportantInformationView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        id = request.GET.get('id')
        print(id)
        try:
            pct = ImportantInformation.objects.get(id=id)
            pct.mission = data['mission']
            pct.vision = data['vision']
            pct.message_from_president = data['message_from_president']
            pct.historical_background = data['historical_background']

            pct.save()
            return Response({'update': True})
        except:
            return Response({'update': False})

    @staticmethod
    def get(request):
        id = request.GET.get("id")
        pct = ImportantInformation.objects.get(id=id)
        pct.delete()
        return Response({"delete": True})


class GalleryView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serialized = GalleryPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        queryset = Gallery.objects.all()
        serialized = GalleryGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


class DeleteUpdateGalleryView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        pass

    @staticmethod
    def get(request):
        id = request.GET.get("id")
        pct = Gallery.objects.get(id=id)
        pct.delete()
        return Response({"delete": True})