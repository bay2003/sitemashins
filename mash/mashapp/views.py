from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import ContextMixin
from .models import Project, Category
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.core.validators import EmailValidator, RegexValidator, URLValidator, ValidationError
from django.http import JsonResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    posts = Create.active_objects.all()
    paginator = Paginator(posts, 1)  # Показывать по 2 поста на странице
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    title = 'Главная страница'
    return render(request, 'mashapp/index.html', {'posts': posts, 'title': title})


def contact(request):
    title = "Контакты"
    return render(request, 'mashapp/contact.html', context={'title': title})


@user_passes_test(lambda u: u.is_superuser)
def projects(request):
    return render(request, 'mashapp/projects.html')

def resume(request):
    title = "Информация"
    return render(request, 'mashapp/resume.html', context={'title': title})

def project_list(request):
    title = "Проекты"
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects, 'title': title})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    template = get_template('project_detail.html')
    html = template.render({'project': project})
    return HttpResponse(html)

required_fields = ['name', 'email', 'phone']

def is_valid_email(email):
    try:
        EmailValidator(email)
        return True
    except ValidationError:
        return False

def is_valid_phone(phone):
    if phone[0] != '+':
        return False, "Phone number must start with '+'"
    if len(phone) != 12:
        return False, "Phone number must be 12 characters long"
    for char in phone[1:]:
        if not char.isdigit():
            return False, "Phone number must contain only digits after the country code"
    return True, None

def submit_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone', '')

        is_valid, error_message = is_valid_phone(phone)
        if not is_valid:
            return JsonResponse({'success': False, 'error': error_message}, status=400)

        if not is_valid_email(email):
            return JsonResponse({'success': False, 'error': 'Invalid email address'}, status=400)

        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message
        }
        try:
            with open('contact_data.json', 'w') as f:
                json.dump(data, f)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)

from .models import Page, Post

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Tag, Create
from .forms import MashForm, PostCategoryForm


@login_required
def create(request):
    if request.method == 'POST':
        form = MashForm(request.POST)
        if form.is_valid():
            create_instance = form.save(commit=False)
            create_instance.user = request.user  # Устанавливаем текущего пользователя
            create_instance.save()

            # Получаем страницу из формы и создаем новый объект Post, связанный с этой страницей и пользователем
            page = form.cleaned_data['page']
            post = Post.objects.create(page=page, title=create_instance.name, content=create_instance.text, user=request.user)  # Устанавливаем текущего пользователя
            post_url = post.get_absolute_url()

            return redirect('view_post', post_id=post.id)
    else:
        form = MashForm()
    return render(request, 'mashapp/create.html', {'form': form})

class NameContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Список тэгов'
        return context

def view_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Пост не найден")
    return render(request, 'mashapp/post_detail.html', {'post': post})

def resume_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'resume.html', context)

class TagListView(ListView, NameContextMixin):
    model = Tag
    template_name = 'tag_list.html'
    context_object_name = 'tags'
    paginate_by = 1

    def get_queryset(self):
        return Tag.active_objects.all()

class TagDetailView(UserPassesTestMixin, DetailView, NameContextMixin):
    model = Tag
    template_name = 'mashapp/tag_detail.html'
    def test_func(self):
        return self.request.user.is_superuser

    context_object_name = 'tags'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Список тэгов'
        return context

class TagCreateView(LoginRequiredMixin, CreateView, NameContextMixin):
    fields = '__all__'
    model = Tag
    success_url = reverse_lazy('tag_list')
    template_name = 'mashapp/tag_create.html'

    def form_valid(self, form):
        return super().form_valid(form)

class TagUpdateView(UserPassesTestMixin, UpdateView, NameContextMixin):
    fields = '__all__'
    model = Tag
    success_url = reverse_lazy('tag_list')
    template_name = 'mashapp/tag_create.html'
    def test_func(self):
        return self.request.user.is_superuser

class TagDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'mashapp/tag_delete_confirm.html'
    model = Tag
    success_url = reverse_lazy('tag_list')
    def test_func(self):
        return self.request.user.is_superuser


from .forms import ContactForm



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Здесь вы можете обработать валидные данные формы
            # Например, отправить email или сохранить данные в базу данных
            return HttpResponseRedirect('/resume/')  # Перенаправление после успешной обработки
    else:
        form = ContactForm()
    return render(request, 'mashapp/contactform.html', {'form': form})

class CategoryDetailView(DetailView):
    template_name = 'mashapp/category_detail.html'
    model = Category
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['form'] = PostCategoryForm()
        return context
from django.shortcuts import get_object_or_404
from django.urls import reverse

class PostCategoryCreateView(CreateView):
    model = Create
    template_name = 'category_detail.html'
    success_url = '/'
    form_class = PostCategoryForm

    def post(self, request, *args, **kwargs):
        self.category_pk = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        category = get_object_or_404(Category, pk=self.category_pk)
        form.instance.category = category
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('category_detail', kwargs={'pk': self.category_pk})


