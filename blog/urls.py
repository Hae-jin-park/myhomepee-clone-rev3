
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("blog/", views.index, name="index"),
    # path("1/", login_required(TemplateView.as_view(template_name="root.html")), name="root"),
]
