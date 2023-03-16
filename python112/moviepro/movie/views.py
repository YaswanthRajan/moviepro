from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import movieform
from .models import ko
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
def demo(request):
    l = ko.objects.all()
    return render(request, 'movie.html', {'ll': l})


def detail(request, id):
    z = ko.objects.get(id=id)
    return render(request, 'detail.html', {'sd': z})


def add(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        year = request.POST.get('year', )
        des = request.POST.get('des', )
        image = request.FILES['image']
        a = ko(name=name, year=year, des=des, image=image)
        a.save()
        return redirect('/')
    return render(request, 'addmovie.html')


def update(request, id):
    y = ko.objects.get(id=id)
    form = movieform(request.POST or None, request.FILES, instance=y)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = movieform(instance=y)

    return render(request, 'forms1.html', {'sd': y, 'form': form})


def delete(request, id):
    if request.method == "POST":
        x = ko.objects.get(id=id)
        x.delete()
        return redirect('/')

    return render(request, 'delete.html')


class movielistview(ListView):
    model = ko
    template_name = 'movie.html'
    context_object_name = 'll'


class moviedetailview(DetailView):
    model = ko
    template_name = 'detail.html'
    context_object_name = 'sd'


class movieupdateview(UpdateView):
    model = ko
    template_name = 'update.html'
    context_object_name = ''
    fields = ('name', 'des', 'image')

    def get_success_url(self):
        return reverse_lazy('movie.cbvdetail', kwargs={'pk': self.object.id})


class moviedeleteview(DeleteView):
    model = ko
    template_name = 'delete.html'
    success_url = reverse_lazy('movie:list')

