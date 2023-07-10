from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView
from django.http.response import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.

class IndexView(TemplateView):
    template_name = 'portfolio_app/index.html'

projects = {
    # project_title/url : file name
    'jellyfin_music_organizer':'jellyfin_music_organizer',
    'hand_convex':'hand_convex',
    'library_login':'library_login',
    'folder_factory':'folder_factory',
    'openearly':'openearly',
    'pong':'pong',
    'states_game':'states_game',
    'model_forms':'model_forms',
    'snake_game':'snake_game',
    'turtle_crossing':'turtle_crossing',
    'blackjack':'blackjack',
}

def project_view(request, project_title):
    try:
        result = projects[project_title]
        template_name = f'portfolio_app/{result}.html'
        context = {'project_title':project_title.title()}
        return render(request, template_name, context)
    except KeyError:
        raise Http404("404 Generic Error")

def project_with_link_view(request, project_title):
    link_url = reverse('portfolio_app:project_page', args=[project_title])
    return redirect(link_url)

