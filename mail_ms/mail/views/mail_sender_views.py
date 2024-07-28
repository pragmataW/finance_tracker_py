from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from mail.services import MailSender
from mail.dto import Mail

class MailSenderViews:
    mailSender = MailSender()
    
    @staticmethod
    @csrf_exempt
    @require_http_methods(['POST'])
    def SendMail(request):
        try:
            body = json.loads(request.body)
            toMail = body.get("to_mail")
            toName = body.get("to_name")
            subject = body.get("subject")
            html = body.get("html")

            if not toMail or not toName or not subject or not html:
                return JsonResponse({'error': 'All fields are required'}, status=400)

            mail = Mail(subject=subject, html=html, to_mail=toMail, user_name=toName)

            status_code = MailSenderViews.mailSender.sendMail(mail)
            if status_code != 200:
                return JsonResponse({'error': "internal server error"}, status=500)
            
            return JsonResponse({'message': 'mail sent'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status = 400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)