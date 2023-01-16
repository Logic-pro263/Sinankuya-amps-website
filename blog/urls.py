from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("a-propos/", views.about, name="a-propos"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name="blog"),
    path(
        "amps-admin/login",
        LoginView.as_view(
            template_name="blog/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path(
        "amps-admin/logout",
        LogoutView.as_view(template_name="blog/logout.html"),
        name="logout",
    ),
    path("amps-admin/Dashboard/", views.admin_site, name="admin-site"),
    path("amps-admin/nouveau-article/", views.add_post, name="add-post"),
    path(
        "envoi-de-message-reussi/", views.confirm_send_message, name="success-message"
    ),
]
