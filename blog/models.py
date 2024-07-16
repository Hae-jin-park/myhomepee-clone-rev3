from django.db import models
from django.conf import settings
from froala_editor.fields import FroalaField

# from django_ckeditor_5.fields import CKEditor5Field
# from tinymce import models as tinymce_models
# from ckeditor_uploader.fields import RichTextUploadingField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    up_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.sub_name


# Create your models here.
class Post(BaseModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="my_post_set", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = FroalaField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
