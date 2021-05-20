from django.http import HttpResponse
from django.views.generic import TemplateView


class BlogClass(TemplateView):

    template_name = 'blog/blog.html'
