from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import PostModel
from .forms import PostForm
from rest_framework.response import Response
from django.shortcuts import redirect

class ListClass(ListView):
    template_name = 'list.html'
    model = PostModel
    form_class = PostForm

    def form_valid(self, request):
        print(request)

class FormClass(CreateView):
    template_name = 'form.html'
    model = PostModel
    success_url = reverse_lazy('formapp:list')
    form_class = PostForm

def deletePost(request, pk):
    print(pk)
    post = PostModel.objects.get(id=pk)
    post.delete()

    return redirect('formapp:list')
