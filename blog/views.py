from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "blog/index.html")


def about(request):
    return render(request, "blog/a-propos.html")


def contact(request):
    return render(request, 'blog/contact.html')


def blog(request):
    return render(request, 'blog/blog.html')


@login_required
def admin_site(request):
    return render(request, 'blog/admin-site.html')