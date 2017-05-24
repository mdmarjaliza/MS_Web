import requests
from django.shortcuts import render
from django.views import View


class ListView(View):
    def get(self, request):
        """
        Renderiza el home con un listado de los ultimos post publicados por los usuarios
        :param request: objeto HttpRequest con los datos de la peticion
        :return:
        """
        r = requests.get('http://127.0.0.1:9002/api/1.0/posts')
        posts = r.json()
        context = {'posts_list': posts}
        return render(request, "MSWeb/home.html", context)
