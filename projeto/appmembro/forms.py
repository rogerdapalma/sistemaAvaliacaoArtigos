from django import forms

from evento.models import Evento
from submissao.models import Submissao
from usuario.models import Usuario


class MembroCreateForm(forms.ModelForm):
    #(técnico, graduando, graduado, especialista, mestre, doutor)
    TITULACAO = (
        ('TECNICO', 'Técnico'),
        ('GRADUANDO', 'Graduando' ),
        ('GRADUADO', 'Graduado' ),        
        ('ESPECIALISTA', 'Especialista'),
        ('MESTRE', 'Mestre' ),
        ('DOUTOR', 'Doutor' ),        
    )

    #(Ciências Humana, Ciências da Saúde, Ciências Sociais, Ciências Tecnológicas)
    AREA = (
        ('HUMANAS', 'Ciências Humanas'),
        ('SAUDE', 'Ciências da Saúde' ),
        ('SOCIAIS', 'Ciências Sociais' ),        
        ('TECNOLOGICA', 'Ciências Tecnológicas'),        
    )

    nome = forms.CharField(label='Nome completo *', help_text='* Campos obrigatórios',required=True)
    titulacao = forms.ChoiceField(label='Titulação *',choices=TITULACAO, help_text='Selecione a maior titulação', required=False)
    area = forms.ChoiceField(label='Área de pesquisa do usuário *', choices=AREA, help_text='Escolha área de interesse de trabalho',required=True)
    instituicao = forms.CharField(label='Instituição a que pertence *', help_text='Registre a instituição, ou universidade, ou empresa',required=True)
    email = forms.EmailField(label='Email *', help_text='Use o email válido. Será usado para acessar sistema e recuperar senha!',required=True)
    celular = forms.CharField(label='Número celular com DDD *', help_text="Use DDD, por exemplo 55987619832",required=True)
    cpf = forms.CharField(label='CPF *',required=True)    
    
        
    class Meta:
        model = Usuario
        fields = ['nome','titulacao', 'area', 'instituicao', 'email', 'celular', 'cpf']


class SubmissaoForm(forms.ModelForm):
    evento = forms.ModelChoiceField(label='Evento para a submissão *', queryset=Evento.eventos_ativos)    
 
    class Meta:
        model = Submissao
        fields = ['evento', 'titulo', 'resumo' , 'abstract', 'palavras_chave', 'arquivo_sem_autores', 'arquivo_final', 
                  'arquivo_comite_etica', 'observacoes']

    # def clean_colaborador(self):
    #     colaborador = self.cleaned_data.get('colaborador')
    #     responsavel = self.cleaned_data.get('responsavel')

    #     if (responsavel in colaborador.all()):
    #         raise forms.ValidationError('Um professor não pode ser ao mesmo tempo responsável e colaborador')
    #     return colaborador


class BuscaSubmissaoForm(forms.Form):     
    STATUS = (
        (None, '-----------'),
        ('EM EDICAO', 'Em edição'),
        ('EM ANALISE', 'Em análise'),
        ('EM CORRECAO', 'Em correção' ),        
        ('APROVADO', 'Aprovado' ),
        ('RETIRADO PELO RESPONSAVEL', 'Retirado pelo responsável'),
        ('RETIRADO PELO COORDENADOR', 'Retirado pelo coordenador' ),
        ('REPROVADO', 'Reprovado' ),  
    )         
    
    situacao = forms.ChoiceField(label='Status da submissão', choices=STATUS, required=False)
    pesquisa = forms.CharField(label='Pesquisa livre', required=False)
    