from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comments, Message
from .forms import MessageForm, PostForm


def index(request):
    return render(request, "blog/index.html")


def about(request):
    return render(request, "blog/a-propos.html")


def contact(request):
    form = MessageForm()
    success = ""
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success-message")
    context = {
        "form": form,
    }
    return render(request, "blog/contact.html", context)


def blog(request):
    return render(request, "blog/blog.html")


@login_required
def admin_site(request):
    posts = Post.objects.all().order_by("-created_at")

    context = {
        "posts": posts,
    }
    return render(request, "blog/admin-site.html", context)


def add_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("admin-site")
    context = {"form": form}
    return render(request, "blog/add-post.html", context)


def confirm_send_message(request):
    success = (
        "Nous avons bien réçu votre message. Nous vous répondrons dans un bref délai"
    )
    return render(
        request, "blog/message-send-success.html", context={"success": success}
    )
