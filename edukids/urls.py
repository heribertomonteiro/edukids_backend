from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('lista', views.PostListView.as_view(), name='lista'),
    path('criar', views.PostCreateView.as_view(), name='criar'),
    path('calendario/', views.CalendarioAnualView.as_view(), name='calendario'),
    path('calendario/evento/novo/', views.EventoCreateView.as_view(), name='calendario_evento_novo'),
    path('evento/<int:pk>/', views.DetalhesEventoView.as_view(), name='evento'),
    path('financeiro/', views.financeiro, name='financeiro'),
    path('contato/', views.contato, name='contato'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('register/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)