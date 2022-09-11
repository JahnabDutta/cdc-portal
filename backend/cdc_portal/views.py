import jwt
import datetime
import requests
import subprocess

from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from student.models import StudentProfile, BranchChangers
from .utils import get_config, edit_config, get_config_value, IsSuperUser
from decouple import config

SECRET_KEY = config('SECRET_KEY', cast=str)


class Login(views.APIView):

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Please provide email/password"}, status="400", content_type="application/json")

        email = request.data['email']
        password = request.data['password']
        users = User.objects.filter(email=email)
        if len(users) > 1:
            user = User.objects.filter(email=email, is_superuser=True)[0]
        elif len(users) == 1:
            user = users[0]
        else:
            return Response(
                {'Error': "Invalid credentials"},
                status=400,
                content_type="application/json"
            )
        if user and user.check_password(password):

            payload = {
                'id': user.id,
                'email': user.email,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }
            data = {'token': jwt.encode(payload, SECRET_KEY, algorithm="HS256")}
            data['Dname'] = user.email
            return Response(
                data,
                status=status.HTTP_200_OK)
        else:
            return Response(
                {'Error': "Invalid credentials"},
                status=400,
                content_type="application/json"
            )


class LDAPOAuth(views.APIView):

    def post(self, request, *args, **kwargs):
        if not get_config_value('AllowStudentLogin'):
            return Response({'Error': "Registration not started yet"}, status="400", content_type="application/json")
        if not request.data:
            return Response({'Error': "Please provide valid credentials"}, status="400", content_type="application/json")

        user_id = request.data['id']
        password = request.data['password']
        if not get_config_value('LDAPTestMode'):
            try:
                result = subprocess.check_output(['java', 'LDAP_login_api', user_id, password])
                result = result.decode('utf-8')
                if (result == "0"):
                    return Response(
                        {'Error': "Invalid credentials : Please provide valid credentials"},
                        status=400,
                        content_type="application/json"
                    )
                email = result.split("mail=mail: ")[1].split(",")[0].replace("}", "").replace("{", "")
                name = result.split("givenname=givenName: ")[1].split(",")[0].replace("}", "").replace("{", "").split(" ")
                roll_no = result.split("sn=sn: ")[1].split(",")[0].replace("(", "").replace(")", "").replace("}", "").replace("{", "")
                isBranchChanger = BranchChangers.objects.filter(old_roll_number=roll_no)
                if len(isBranchChanger) > 0:
                    roll_no = isBranchChanger[0].new_roll_number
            except:  # noqa: E722
                return Response(
                    {'Error': "LDAP Server Down"},
                    status=500,
                    content_type="application/json"
                )
        else:
            email = "test@iitj.ac.in"
            roll_no = "B19EE480"
            name = ["test", "user"]
        try:
            user = User.objects.get(email=email, username=roll_no)
        except User.DoesNotExist:
            if len(name) < 2:
                name.append("")
            user = User.objects.create(username=roll_no, email=email, first_name=" ".join(name[:-1]), last_name=name[-1])
        if user:
            payload = {
                'id': user.id,
                'email': user.email,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }
            data = {'token': jwt.encode(payload, SECRET_KEY, algorithm="HS256")}
            data['Dname'] = name[0] + " (" + roll_no + ")"
            try:
                StudentProfile.objects.get(user=user)
                return Response(
                    data,
                    status=status.HTTP_200_OK)
            except StudentProfile.DoesNotExist:
                if not get_config_value('AllowRegistration'):
                    return Response({'Error': "Registration Ended"}, status="400", content_type="application/json")
                return Response(
                    data,
                    status=status.HTTP_201_CREATED)
        else:
            return Response(
                {'Error': "Server Down"},
                status=500,
                content_type="application/json"
            )


class GoogleLogin(views.APIView):

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Please provide the token"}, status="400")

        token = request.data['token']
        resp = requests.post('https://oauth2.googleapis.com/tokeninfo', data={'id_token': token})
        data = resp.json()
        if not data['email'] or resp.status != 200:
            return Response(
                {'Error': "Invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = User.objects.filter(email=data['email']).first()
        if user is None:
            user = User.objects.create_user(
                email=data["email"], username=data["name"])
        if user:

            payload = {
                'id': user.id,
                'email': user.email,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }
            jwt_token = {'token': jwt.encode(payload, SECRET_KEY, algorithm="HS256")}

            return Response(
                jwt_token,
                status=status.HTTP_200_OK)


class Config(views.APIView):
    permission_classes = (IsSuperUser,)

    def get(self, request, *args, **kwargs):
        config = get_config()
        return Response(
            config,
            status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = request.data
        if data is None:
            return Response(status.HTTP_400_BAD_REQUEST)
        try:
            edit_config(data)
            return Response(status.HTTP_200_OK)
        except:  # noqa: E722
            return Response({'Error': "Invalid File format"}, status.HTTP_400_BAD_REQUEST)
