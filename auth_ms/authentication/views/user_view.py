from django.http import JsonResponse
from authentication.exceptions import WrongVerificationCode
from authentication.services import UserService
from authentication.exceptions import UsernameAlreadyExists, EmailAlreadyExists
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
            if not request.body:
                return JsonResponse({"error": "Request body is empty."}, status=400)

            data = json.loads(request.body.decode('utf-8'))
            user_name = data.get('user_name')
            password = data.get('password')
            email = data.get('email')

            if not user_name or not password or not email:
                return JsonResponse({'error': 'All fields are required'}, status=400)

            UserView.userService.registerUser(username=user_name, password=password, email=email)

            return JsonResponse({'message': "created"} ,status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)
        except (UsernameAlreadyExists, EmailAlreadyExists) as e:
            return JsonResponse({'error': str(e)}, status=409)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
    @staticmethod
    @csrf_exempt
    @require_http_methods(['POST'])
    def VerifyUser(request):
        try:
            if not request.body:
                return JsonResponse({"error": "Request body is empty."}, status=400)
            
            body = json.loads(request.body.decode('utf-8'))
            user_name = body.get('user_name')
            verification_code = body.get('verification_code')

            if not user_name or not verification_code:
                return JsonResponse({'error': 'All fields are required'}, status=400)
            
            UserView.userService.verifyUser(userName=user_name, verificationCode=verification_code)
            return JsonResponse({'message': "ok"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)
        except WrongVerificationCode as e:
            return JsonResponse({"error": e.message}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

