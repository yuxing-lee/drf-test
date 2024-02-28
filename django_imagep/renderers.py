from django.views.generic import TemplateView


class ImageView(TemplateView):
    template_name = "index.html"
