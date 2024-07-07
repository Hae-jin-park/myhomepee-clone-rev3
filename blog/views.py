from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Post

# Create your views here.
@login_required
def index(request):
    #pp_list = Post.objects.all()
    return render(
        request,
        "blog/index.html"
    )