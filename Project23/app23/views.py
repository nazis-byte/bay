from django.views.generic import CreateView, ListView
from .models import FilesModel


class FileUpload(CreateView):
    model = FilesModel
    fields = "__all__"
    template_name = "index.html"
    success_url = '/view_all/'


class ViewAllFiles(ListView):
    model = FilesModel
    template_name = "showall.html"
