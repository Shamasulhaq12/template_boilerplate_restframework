from rest_framework.views import APIView    
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailExistAPIView(APIView):
    
    """ 
        Here you can check if email already exists or not
    """

    def post(self, request):
        try:
            """
            Parameters:
                email
            """
            if User.objects.filter(email=request.data['email']).exists():
                return Response({"message": False, "status": "400"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': True, "status": "200"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e), "status": "500"}, status.HTTP_500_INTERNAL_SERVER_ERROR)

