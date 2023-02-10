from django.views.generic import View
from django.core.mail import send_mail
from .models import *
from django.http import JsonResponse


class MessageForm(View):
    def post(self, request):
        if request.POST.get('action') == 'feedback_view':
            # print(request.POST)
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            project_type = request.POST.get('da[projectType]')
            project_platform = request.POST.get('da[projectPlatform]')
            project_status = request.POST.get('da[projectState]')
            start_project = request.POST.get('da[projectStart]')
            comment = request.POST.get('comment')
            file = request.POST.get('file')

            message = "\n" f"Имя: {name}" \
                      "\n" f"Телефон: {phone}" \
                      "\n" f"E-mail: {email}" \
                      "\n" f"Тип проекта: {project_type}" \
                      "\n" f"Платформа проекта: {project_platform}" \
                      "\n" f"Статус проекта: {project_status}" \
                      "\n" f"Время начала: {start_project}" \

            # send_mail(name, message, 'info@investsud.ru', ['sergeimakarenko5991@gmail.com'], fail_silently=False)
            Form.objects.create(
                type_project=project_type,
                platform=project_platform,
                project_status=project_status,
                start_project=start_project,
                name=name,
                phone=phone,
                email=email,
                comment=comment,
                file=file,
            )
            return JsonResponse({"result": 200}, status=200)
