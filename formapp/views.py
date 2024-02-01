from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import PostModel
from .forms import PostForm
from rest_framework.response import Response
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import render

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

class PostListView(ListView):
    model = PostModel
    context_object_name = 'post'
    ordering = ['-created_date']
    template_name =('formapp:list')

# def formapp_list(request):
#         posts = PostModel.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
#         return render(request, 'templates/list.html', {'posts': posts})