from django.http import JsonResponse
from authentication.serializers import UserSerializer 
from authentication.services import UserService
from authentication.exceptions import UsernameAlreadyExists
from authentication.exceptions import EmailAlreadyExists
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

class UserView:
    userService = UserService()

    @staticmethod
    @csrf_exempt
    @require_http_methods(['POST'])
    def AddUser(request):
        try:
            data = json.loads(request.body)
            user_name= data.get('user_name')
            password = data.get('password')
            email = data.get('email')

            if not user_name or not password or not email:
                return JsonResponse({'error': 'All fields are required'}, status=400)
            
            try:
                user = UserView.userService.RegisterUser(username=user_name, password=password, email=email)
            except UsernameAlreadyExists or EmailAlreadyExists as e:
                return JsonResponse({'error': e.message}, status=409)
            
            serializer = UserSerializer(user)

            return JsonResponse(serializer.data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status = 400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 400)


