from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Blog


def index(req: HttpRequest) -> HttpResponse:
    blogs = Blog.objects.order_by("-created_at")
    return render(req, "blogs/index.html", {"blogs": blogs})


def detail(req: HttpRequest, blog_id: int) -> HttpResponse:
    blog = Blog.objects.get(id=blog_id)
    return render(req, "blogs/detail.html", {"blog": blog})
