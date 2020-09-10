from django.views.generic.base import TemplateView
from django.apps import apps


#--- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#        context['app_list'] = ['polls', 'books']
#       아래는 새로 추가 되는 줄
        dictVerbose = {}
        for app in apps.get_app_configs():
            if 'site-packages' not in app.path:
                dictVerbose[app.label] = app.verbose_name
        
        context['verbose_dict'] = dictVerbose
        return context