from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('lista', views.PostListView.as_view(), name='lista'),
    path('criar', views.PostCreateView.as_view(), name='criar'),
    path('post/<int:pk>/editar/', views.PostUpdateView.as_view(), name='post_editar'),
    path('post/<int:pk>/excluir/', views.PostDeleteView.as_view(), name='post_excluir'),
    path('calendario/', views.CalendarioAnualView.as_view(), name='calendario'),
    path('calendario/evento/novo/', views.EventoCreateView.as_view(), name='calendario_evento_novo'),
    path('evento/<int:pk>/', views.DetalhesEventoView.as_view(), name='evento'),
    path('evento/<int:pk>/editar/', views.EventoUpdateView.as_view(), name='evento_editar'),
    path('evento/<int:pk>/excluir/', views.EventoDeleteView.as_view(), name='evento_excluir'),
    path('financeiro/', views.financeiro, name='financeiro'),
    path('contato/', views.contato, name='contato'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('register/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)