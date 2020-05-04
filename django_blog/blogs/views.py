from django.shortcuts import render
from django.http.request import HttpRequest

from .models import Blog


def index(req: HttpRequest) -> render:
    blogs = Blog.objects.order_by("-created_at")
    return render(req, "blogs/index.html", {"blogs": blogs})


def detail(req: HttpRequest, blog_id: int) -> render:
    blog = Blog.objects.get(id=blog_id)
    return render(req, "blogs/detail.html", {"blog": blog})
