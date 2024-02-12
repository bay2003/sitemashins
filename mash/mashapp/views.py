from django.shortcuts import render, get_object_or_404
from .models import Project
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import json

def index(request):
    return render(request, 'mashapp/index.html')

def contact(request):
    return render(request, 'mashapp/contact.html')

def projects(request):
    return render(request, 'mashapp/projects.html')

def resume(request):
    return render(request, 'mashapp/resume.html')


from django.shortcuts import render


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    template = get_template('project_detail.html')
    html = template.render({'project': project})
    return HttpResponse(html)


# views.py

from django.http import JsonResponse


def submit_contact_form(request):
    if request.method == 'POST':
        # Получаем данные из POST-запроса
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Здесь можно добавить логику для сохранения данных в JSON-файл на компьютере
        # Например, создать словарь и сохранить его в файл
        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message
        }
        with open('contact_data.json', 'w') as f:
            json.dump(data, f)

        # Возвращаем JSON-ответ об успешной обработке формы
        return JsonResponse({'success': True})
    else:
        # Возвращаем ошибку, если метод запроса не POST
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)
