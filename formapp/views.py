from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import PostModel
from .forms import PostForm

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

    # def form_valid(self, form):
    #     print(form.cleaned_data.get("image"))
    #     postform = PostForm(image=form.cleaned_data.get("image"), title=form.cleaned_data.get("title"))
    #     if postform.is_valid():
    #         post = PostModel()
    #         # post.image = form.FILES['image']
    #         post.save()

    #     pd = postform.save(commit=False)
    #     pd.user = self.request.user
    #     pd.save()
    #     return super().form_valid(postform)
