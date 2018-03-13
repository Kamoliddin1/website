from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Articles


class IndexView(ListView):
    template_name = 'news/posts.html'

    def get_queryset(self):
        return Articles.objects.all().order_by('-date')[:20]


class Detail(DetailView):
    model = Articles
    template_name = 'news/post.html'


def detail_view(request, pk):
    try:
        obj = Articles.objects.get(id=int(pk))
        return render(request, "news/post.html", {"articles": obj})
    except Articles.DoesNotExist:
        raise Http404
