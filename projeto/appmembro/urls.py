from __future__ import unicode_literals
from django.urls import path

from core.views import HomeRedirectView

from .views import (DadosMembroUpdateView, EventoListView, #InscricaoListView, InscricaoCreateView, InscricaoDeleteView,
                    HomeView, AboutView,
                    SubmissaoListView, SubmissaoCreateView, SubmissaoUpdateView, SubmissaoPendenteUpdateView, SubmissaoAprovadoUpdateView, 
                    SubmissaoDeleteView)

urlpatterns = [
   path('home', HomeView.as_view(), name='appmembro_home'), 
   # path('', HomeRedirectView.as_view(), name='home_redirect'),
   path('about', AboutView.as_view(), name='appmembro_about'),
   path('eventos/', EventoListView.as_view(), name='appmembro_evento_list'),

   path('meus-dados/', DadosMembroUpdateView.as_view(), name='appmembro_dados_update'),

   path('minhas-submissoes', SubmissaoListView.as_view(), name='appmembro_submissao_list'),
   path('minhas-submissoes/cad/', SubmissaoCreateView.as_view(), name='appmembro_submissao_create'),
   # path('minhas-submissoes/pendente/<slug:slug>/', SubmissaoPendenteUpdateView.as_view(), name='appmembro_submissao_pendente_update'),
   # path('minhas-submissoes/aprovado/<slug:slug>/', SubmissaoAprovadoUpdateView.as_view(), name='appmembro_submissao_aprovado_update'),
   path('minhas-submissoes/<slug:slug>/', SubmissaoUpdateView.as_view(), name='appmembro_submissao_update'),
   path('minhas-submissoes/<slug:slug>/delete/', SubmissaoDeleteView.as_view(), name='appmembro_submissao_delete'),


   
   # path('minhas-inscricoes', InscricaoListView.as_view(), name='appmembro_inscricao_list'),
   # path('minhas-inscricoes/cad/', InscricaoCreateView.as_view(), name='appmembro_inscricao_create'),
   # path('<slug:slug>/delete/', InscricaoDeleteView.as_view(), name='appmembro_inscricao_delete'), 
]
