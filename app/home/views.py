from bakery.views import BuildableTemplateView


class HomeView(BuildableTemplateView):
    template_name = "home/index.html"
    build_path = "index.html"
