import os
from urllib.parse import urljoin
from datetime import datetime

from django.conf import settings
from django.core.files.storage import FileSystemStorage

path = "uploads/"+ str(datetime.now.year)+ "/"+ str(datetime.now.month)+ "/"+ str(datetime.now.day)+ "/"
class CustomStorage(FileSystemStorage):
    location = os.path.join(
        settings.MEDIA_ROOT,
        path,
    )
    base_url = urljoin(
        settings.MEDIA_URL,
        path,
    )
