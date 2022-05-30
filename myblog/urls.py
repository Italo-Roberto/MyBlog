"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
#Configuração para exibição de imagens
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog, name='blog'),
    #Autenticação
    path('login/', views.login_user, name='login'),
    path('login/submit', views.submit_login),
    path('logout_user/', views.logout_user),
    #Blog
    path('post/<int:post_id>/', views.post, name='post'),
    path('form_posting/', views.form_posting, name='form_posting'),
    path('form_posting/posting', views.posting, name='posting'),
    path('render_update_post/<int:post_id>', views.render_update_post, name='render_update_post'),
    path('render_update_post/update_post', views.update_post, name='update_post'),
    path('login/delete_post/<int:post_id>', views.delete_post, name='delete_post'),
]

#Necessário para armazenamento de imagens
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)