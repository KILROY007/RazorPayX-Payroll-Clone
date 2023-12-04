from rest_framework.views import APIView
from userAuth.serializers import RegisterSerializers 
from rest_framework.response import Response
from rest_framework import status , exceptions
from . import services
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterAPI(APIView):
  
  def post(self, request):
    instance  = request.data
    serializer = RegisterSerializers(data= instance)

    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    serializer.instance = services.create_user(user_dc=data)

    user_data = {
      'email': serializer.instance.email,
      'id' : serializer.instance.id
    }

    return Response({
      'message' : 'User has been Registered',
      **user_data
    }, status= status.HTTP_201_CREATED,  )
  

class LoginAPI(APIView):
  
  def post(self,request):
    email = request.data["email"]
    password = request.data["password"]

    user = services.user_email_validator(email=email)

    if user is None:
        raise exceptions.AuthenticationFailed("Invalid Credentials")

    if not user.check_password(raw_password=password):
        raise exceptions.AuthenticationFailed("Invalid Credentials")
    
    refresh = RefreshToken.for_user(user)

    return Response({
       'id': user.id,
       'refreshToken' : str(refresh),
       'accessToken' : str(refresh.access_token)
    }, status= status.HTTP_200_OK)
  
class LogoutAPI(APIView):
  def post(self,request):
    try:
        refresh_token = request.data.get("refresh_token")
        token = RefreshToken(token=refresh_token, verify=True)
        token.blacklist()

        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
      return Response(status=status.HTTP_400_BAD_REQUEST)
      
  
