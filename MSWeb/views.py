import requests
from django.shortcuts import render
from django.views import View


class ListView(View):
    def get(self, request):
        """
        Renderiza el home con un listado de los ultimos post publicados por los usuarios
        :param
        :return:
        """
        r = requests.get('http://127.0.0.1:9002/api/1.0/posts')
        posts = r.json()
        context = {'posts_list': posts[:5]}
        return render(request, "MSWeb/home.html", context)


class UserPostsListView(View):
    def get(self, request):
        """
        Renderiza el home con un listado de los ultimos post publicados por los usuarios
        :param
        :return:
        """
        blogger = request.META.get('HTTP_XBLOGGER')
        blogger_id = request.META.get('HTTP_XBLOGGERID')
        headers = {
            'XBLOGGER': blogger,
            'XBLOGGERID': blogger_id
        }
        r = requests.get('http://127.0.0.1:9002/api/1.0/userposts', headers=headers)
        userposts = r.json()
        context = {'posts_list': userposts[:5], 'blogger': blogger}
        return render(request, "MSWeb/includes/user_posts.html", context)


class WebPostDetailView(View):
    def get(self, request):
        """
        Renderiza el detalle de un post
        :param
        :return:
        """
        blogger = request.META.get('HTTP_X_BLOGGER')
        post_id = request.META.get('HTTP_X_POSTID')
        headers = {
            'X-BLOGGER': blogger,
            'X-POSTID': post_id
        }
        respuesta_post = requests.get('http://127.0.0.1:9002/api/1.0/postdetail', headers=headers)
        post = respuesta_post.json()

        respuesta_comments = requests.get('http://127.0.0.1:9003/api/1.0/comment/' + post_id)
        comments = respuesta_comments.json()

        context = {'post': post, 'comments_list': comments}
        return render(request, "MSWeb/includes/post_detail.html", context)
