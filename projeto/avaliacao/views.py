from __future__ import unicode_literals

from datetime import datetime

from django import forms
from django.contrib import messages
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from easy_pdf.views import PDFTemplateResponseMixin

from utils.decorators import LoginRequiredMixin, CoordenadorRequiredMixin, SecretariaCoordenadorAdministradorRequiredMixin

from .models import Avaliacao

from .forms import AvaliacaoForm, BuscaAvaliacaoForm

from appprofessor.forms import MinhaAvaliacaoOrientadorForm
from appprofessor.forms import MinhaAvaliacaoResponsavelForm
from appprofessor.forms import MinhaAvaliacaoSuplenteForm

from submissao.models import Submissao

class AvaliacaoListView(LoginRequiredMixin, CoordenadorRequiredMixin, ListView):
    model = Avaliacao
    template_name = 'avaliacao/avaliacao_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaAvaliacaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaAvaliacaoForm()
        return context
    
    def get_queryset(self):
        qs = Avaliacao.objects.all()
        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaAvaliacaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaAvaliacaoForm()
            
        if form.is_valid():
            nome_aluno = form.cleaned_data.get('nome_aluno')
            curso = form.cleaned_data.get('curso')
            turma = form.cleaned_data.get('turma')
            nome_orientador = form.cleaned_data.get('nome_orientador')
            nome_avaliador = form.cleaned_data.get('nome_avaliador')

            if nome_aluno:
                qs = qs.filter(submissao__aluno__nome__icontains=nome_aluno)
                
            if curso:
                qs = qs.filter(submissao__turma__curso=curso)

            if turma:
                qs = qs.filter(submissao__turma=turma) 

            if nome_orientador:
                qs = qs.filter(submissao__orientador__nome__icontains=nome_orientador)

            if nome_avaliador:
                qs = qs.filter(Q(avaliador_responsavel__nome__icontains=nome_avaliador) | Q(avaliador_suplente__nome__icontains=nome_avaliador) | Q(avaliador_convidado__nome__icontains=nome_avaliador))
                
        return qs


class AvaliacaoAndamentoListView(LoginRequiredMixin, CoordenadorRequiredMixin, ListView):
    model = Avaliacao
    template_name = 'avaliacao/avaliacao_andamento_list.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaAvaliacaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaAvaliacaoForm()
        return context

    def get_queryset(self):
        # qs = Avaliacao.objects.all()
        qs = Avaliacao.objects.all().filter(submissao__status = 'EM ANDAMENTO')

        
        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaAvaliacaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaAvaliacaoForm()

        if form.is_valid():
            nome_aluno = form.cleaned_data.get('nome_aluno')
            curso = form.cleaned_data.get('curso')
            turma = form.cleaned_data.get('turma')
            nome_orientador = form.cleaned_data.get('nome_orientador')
            nome_avaliador = form.cleaned_data.get('nome_avaliador')
            
            if nome_aluno:
                qs = qs.filter(submissao__aluno__nome__icontains=nome_aluno)
                
            if curso:
                qs = qs.filter(submissao__turma__curso=curso)

            if turma:
                qs = qs.filter(submissao__turma=turma)
                
            if nome_orientador:
                qs = qs.filter(submissao__orientador__nome__icontains=nome_orientador)
    
            if nome_avaliador:				
                qs = qs.filter(Q(avaliador_responsavel__nome__icontains=nome_avaliador) | Q(avaliador_suplente__nome__icontains=nome_avaliador) | Q(avaliador_convidado__nome__icontains=nome_avaliador))

        return qs


class AvaliacaoMinhasAndamentoListView(LoginRequiredMixin, ListView):
    model = Avaliacao
    template_name = 'avaliacao/avaliacao_andamento_minhas_list.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaAvaliacaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaAvaliacaoForm()
        return context

    def get_queryset(self):
        # qs = Avaliacao.objects.all()
        qs = Avaliacao.objects.all().filter(Q(submissao__status = 'EM ANDAMENTO'))
        qs = qs.filter(Q(submissao__avaliacao__avaliador_responsavel = self.request.user) | Q(submissao__avaliacao__avaliador_suplente = self.request.user) | Q(submissao__orientador = self.request.user))

        
        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaAvaliacaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaAvaliacaoForm()

        if form.is_valid():
            nome_aluno = form.cleaned_data.get('nome_aluno')
            curso = form.cleaned_data.get('curso')
            turma = form.cleaned_data.get('turma')
            nome_orientador = form.cleaned_data.get('nome_orientador')
            nome_avaliador = form.cleaned_data.get('nome_avaliador')
            
            if nome_aluno:
                qs = qs.filter(submissao__aluno__nome__icontains=nome_aluno)
                
            if curso:
                qs = qs.filter(submissao__turma__curso=curso)

            if turma:
                qs = qs.filter(submissao__turma=turma)
                
            if nome_orientador:
                qs = qs.filter(submissao__orientador__nome__icontains=nome_orientador)
    
            if nome_avaliador:				
                qs = qs.filter(Q(avaliador_responsavel__nome__icontains=nome_avaliador) | Q(avaliador_suplente__nome__icontains=nome_avaliador) | Q(avaliador_convidado__nome__icontains=nome_avaliador))

        return qs



class AvaliacaoImpressaoListView(LoginRequiredMixin, SecretariaCoordenadorAdministradorRequiredMixin, ListView):
    model = Avaliacao   
    template_name = 'avaliacao/impressao_avaliacao_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaAvaliacaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaAvaliacaoForm()
        return context
    
    def get_queryset(self):
        qs = Avaliacao.objects.all().filter(submissao__status='FINALIZADO')
        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaAvaliacaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaAvaliacaoForm()
            
        if form.is_valid():
            nome_aluno = form.cleaned_data.get('nome_aluno')
            curso = form.cleaned_data.get('curso')
            turma = form.cleaned_data.get('turma')
            nome_orientador = form.cleaned_data.get('nome_orientador')
            nome_avaliador = form.cleaned_data.get('nome_avaliador')
            
            if nome_aluno:
                qs = qs.filter(submissao__aluno__nome__icontains=nome_aluno)
                
            if curso:
                qs = qs.filter(submissao__turma__curso=curso)

            if turma:
                qs = qs.filter(submissao__turma=turma)
                
            if nome_orientador:
                qs = qs.filter(submissao__orientador__nome__icontains=nome_orientador)
    
            if nome_avaliador:				
                qs = qs.filter(Q(avaliador_responsavel__nome__icontains=nome_avaliador) | Q(avaliador_suplente__nome__icontains=nome_avaliador) | Q(avaliador_convidado__nome__icontains=nome_avaliador))

        return qs
    
    
class MinhaAvaliacaoListView(LoginRequiredMixin, CoordenadorRequiredMixin, ListView):
    model = Avaliacao
    template_name = 'avaliacao/minha_avaliacao_list.html' 


class AvaliacaoMinhaCoordenacaoListView(LoginRequiredMixin, CoordenadorRequiredMixin, ListView):
    model = Avaliacao
    template_name = 'avaliacao/avaliacao_andamento_list.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        
        return qs.filter(submissao__turma__professor=self.request.user)


class AvaliacaoCreateView(LoginRequiredMixin, CoordenadorRequiredMixin, CreateView):
	model = Avaliacao
	form_class = AvaliacaoForm
	success_url = 'submissao_andamento_list'

	def get_initial(self):
		initials = super().get_initial()
		initials['submissao'] = Submissao.objects.get(id=self.request.GET.get('submissao_id'))
		return initials

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['submissao'] = Submissao.objects.get(id=self.request.GET.get('submissao_id'))
		return context

	def get_success_url(self):
		messages.success(self.request, 'Instância de avaliação criada com sucesso!!')
		return reverse(self.success_url)


class AvaliacaoUpdateView(LoginRequiredMixin, CoordenadorRequiredMixin, UpdateView):
	model = Avaliacao
	form_class = AvaliacaoForm
	success_url = 'avaliacao_andamento_list'
 
	def form_valid(self, form):
    	#Grava a data avaliação do coordenador ou como orientador, ou como resposavel, ou como suplente
		
		avaliacao = form.save(commit=False)
		# print('usuario logado: ', self.request.user)
		# print('parecer orientador: ', avaliacao.dt_avaliacao_orientador)
		# print('parecer responsavel: ', avaliacao.dt_avaliacao_responsavel)
		# print('parecer suplente: ', avaliacao.dt_avaliacao_suplente)
  
		if (self.request.user == avaliacao.submissao.orientador):
			avaliacao.dt_avaliacao_orientador = timezone.now()
		elif (self.request.user == avaliacao.avaliador_responsavel):
			avaliacao.dt_avaliacao_responsavel = timezone.now()
		elif (self.request.user == avaliacao.avaliador_suplente):
			avaliacao.dt_avaliacao_suplente = timezone.now()
   
		if avaliacao.dt_avaliacao_orientador or avaliacao.dt_avaliacao_responsavel or avaliacao.dt_avaliacao_suplente:
			avaliacao.parecer_liberado = 'SIM'

		avaliacao.save()
		return super().form_valid(form)
  		# return super(AvaliacaoForm, self).form_valid(form)

	def get_success_url(self):
		messages.success(self.request, 'Avaliação atualizada com sucesso!!')
		return reverse(self.success_url)


class MinhaAvaliacaoOrientadorUpdateView(LoginRequiredMixin, CoordenadorRequiredMixin, UpdateView):
    model = Avaliacao
    form_class = MinhaAvaliacaoOrientadorForm
    template_name = 'avaliacao/minha_avaliacao_orientador_form.html'
    success_url = 'avaliacao_minhas_andamento_list'
    
    def get_object(self, queryset=None):
        # Não deixa entrar no formulário de avaliação se ele não foi designado como 
        # avaliador orientador
        pk = self.kwargs.get('pk')
        try:
            obj = Avaliacao.objects.get(pk=pk, submissao__orientador=self.request.user)
        except:
            raise Http404("Você não foi designado como avaliador para esta submissão")
        return obj

    def form_valid(self, form):
        # Grava a data avaliação do responsável
        avaliacao = form.save()
        avaliacao.dt_avaliacao_orientador = timezone.now()
        avaliacao.parecer_liberado = 'SIM'
        avaliacao.save()
        return super(MinhaAvaliacaoOrientadorUpdateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Seu parecer como avaliador orientador foi enviado com sucesso!')
        return reverse(self.success_url)


class MinhaAvaliacaoResponsavelUpdateView(LoginRequiredMixin, CoordenadorRequiredMixin, UpdateView):
    model = Avaliacao
    form_class = MinhaAvaliacaoResponsavelForm
    template_name = 'avaliacao/minha_avaliacao_responsavel_form.html'
    success_url = 'avaliacao_minhas_andamento_list'
    
    def get_object(self, queryset=None):
        #Não deixa entrar no formulário de avaliação se ele não foi designado como 
        #avaliador responsável
        pk = self.kwargs.get('pk')
        try:
            obj = Avaliacao.objects.get(pk=pk, avaliador_responsavel=self.request.user)
        except:
            raise Http404("Você não foi designado como avaliador para esta submissão")
    
        return obj


    def form_valid(self, form):
        #Grava a data avaliação do responsável
        avaliacao = form.save()
        avaliacao.dt_avaliacao_responsavel = timezone.now()
        avaliacao.parecer_liberado = 'SIM'
        avaliacao.save()
        return super(MinhaAvaliacaoResponsavelUpdateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Seu parecer como avaliador 1 foi enviado com sucesso!')
        return reverse(self.success_url)


class MinhaAvaliacaoSuplenteUpdateView(LoginRequiredMixin, CoordenadorRequiredMixin, UpdateView):
    model = Avaliacao
    form_class = MinhaAvaliacaoSuplenteForm
    template_name = 'avaliacao/minha_avaliacao_suplente_form.html'
    success_url = 'avaliacao_minhas_andamento_list'

    def get_object(self, queryset=None):
        #Não deixa entrar no formulário de avaliação se ele não foi designado como 
        #avaliador suplente
        pk = self.kwargs.get('pk')
        try:
            obj = Avaliacao.objects.get(pk=pk, avaliador_suplente=self.request.user)
        except:
            raise Http404("Você não foi designado como avaliador suplente para esta submissão")
        return obj

    def form_valid(self, form):
        #Grava a data avaliação do suplente
        avaliacao = form.save()
        avaliacao.dt_avaliacao_suplente = timezone.now()
        avaliacao.parecer_liberado = 'SIM'
        avaliacao.save()
        return super(MinhaAvaliacaoSuplenteUpdateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Seu parecer como avaliador 2 foi enviado com sucesso!')
        return reverse(self.success_url)


class AvaliacaoDeleteView(LoginRequiredMixin, CoordenadorRequiredMixin, DeleteView):
	model = Avaliacao
	success_url = 'avaliacao_andamento_list'

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()		
		success_url = self.get_success_url()
		try:
			self.object.delete()
			messages.success(request, 'Avaliação excluída com sucesso!') 
		except Exception as e:
			messages.error(request, 'Há dependências ligadas à essa avaliação, permissão negada!')
		return redirect(self.success_url)


class AvaliacaoDetailView(LoginRequiredMixin, DetailView):
    model = Avaliacao
    template_name = 'avaliacao/avaliacao_parecer_detail.html'
    success_url = 'avaliacao_andamento_list'
    
    
class AvaliacaoPdfView(LoginRequiredMixin, PDFTemplateResponseMixin, DetailView):
    model = Avaliacao
    template_name = 'avaliacao/impressoes/avaliacao_pdf.html'
    
    
class AvaliacaoTermoBancaPdfView(LoginRequiredMixin, PDFTemplateResponseMixin, DetailView):
    model = Avaliacao
    template_name = 'avaliacao/impressoes/avaliacao_termobanca_pdf.html'
    
class AvaliacaoTermoBibliotecaPdfView(LoginRequiredMixin, PDFTemplateResponseMixin, DetailView):
    model = Avaliacao
    template_name = 'avaliacao/impressoes/avaliacao_termobiblioteca_pdf.html'
    