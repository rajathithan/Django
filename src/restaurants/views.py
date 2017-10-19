from django.views.generic import TemplateView

class homeView(TemplateView):
    template_name = "home.html"

class worksView(TemplateView):
    template_name = "works.html"

class citiesView(TemplateView):
    template_name = "cities.html"

class plansView(TemplateView):
    template_name = "plans.html"

