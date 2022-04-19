from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Cars, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'cars/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'cars/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


class HomeCars(ListView):
    model = Cars
    template_name = 'cars/home_cars_list.html'
    context_object_name = 'cars'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Cars.objects.filter(is_published=True).select_related('category')


class CarsByCategory(ListView):
    model = Cars
    template_name = 'cars/home_cars_list.html'
    context_object_name = 'cars'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Cars.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewCars(DetailView):
    model = Cars
    context_object_name = 'cars_item'


class CreateCars(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'cars/add_cars.html'
    raise_exception = True

