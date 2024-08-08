from __future__ import unicode_literals

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from decimal import Decimal

from utils.gerador_hash import gerar_hash 

#NOTA; colocar campo para liberar avaliação/banca ao aluno/professores ou por data

class Avaliacao(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    CONCORDA = (
        ('SIM', 'Sim'),
        ('NÃO', 'Não'),
    )
    
    CONCORDA_APTO = (
        ('SIM', 'Sim'),
        ('NÃO', 'Não'),
        ('NÃO INFORMADO', 'Não informado')
    )
    submissao = models.OneToOneField('submissao.Submissao', verbose_name='Selecione um artigo submetido para avaliação *', on_delete=models.PROTECT)
    
    avaliador_responsavel = models.ForeignKey('usuario.Usuario', verbose_name='Selecione um membro como avaliador 1 *', related_name='avaliador_responsavel', on_delete=models.PROTECT)
    avaliador_suplente = models.ForeignKey('usuario.Usuario', verbose_name='Selecione um membro como avaliador 2 *', related_name='avaliador_suplente', null=True, blank=True, on_delete=models.PROTECT)
    avaliador_convidado = models.ForeignKey('usuario.Usuario', verbose_name='Selecione um membro como avaliador 3', related_name='avaliador_convidado', null=True, blank=True, on_delete=models.PROTECT)
    
    parecer_liberado = models.CharField('Coordenador, você libera o parecer ao autor?', max_length=4, choices=CONCORDA, null=True,blank=True, default='NÃO')
    
    #Campos de parecer avaliador responsavel
    dt_avaliacao_responsavel = models.DateTimeField('Data da avaliação do avaliador 1', null=True, blank=True)
    parecer_avaliador_responsavel = models.TextField('Parecer do avaliador 1 (5000 caracteres)', max_length=5000, null=True, blank=True, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    parecer_rebanca_avaliador_responsavel = models.TextField('Parecer de REAVALIAÇÃO do avaliador 1 (5000 caracteres)', max_length=5000, null=True, blank=True, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    
    merito_relevancia_responsavel = models.DecimalField('Relevância: O artigo aborda um problema atual e relevante em alguma das áreas especificadas para o evento?',help_text='De 0 a 5', max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True, default = 0, help_text=' Nota 0 equivale a NÃO atende, enquanto, nota 5 atende COMPLETAMENTE.')
    merito_contribuicao_responsavel = models.DecimalField('Relevância: O artigo aborda um problema atual e relevante em alguma das áreas especificadas para o evento?',help_text='De 0 a 5', max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True, default = 0, help_text=' Nota 0 equivale a NÃO atende, enquanto, nota 5 atende COMPLETAMENTE.')
    
    merito_desenvolvimento_responsavel = models.DecimalField('Desenvolvimento',help_text='Máximo 10 pontos', max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10)], null=True, blank=True, default = 0)
    merito_redacao_responsavel = models.DecimalField('Redação do texto',help_text='Máximo 10 pontos', max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10)], null=True, blank=True, default = 0)
    merito_apresentacao_responsavel = models.DecimalField('Apresentação',help_text='Máximo 10 pontos', max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10)], null=True, blank=True, default = 0)
    
    nota_final_responsavel = models.DecimalField('Final Avaliador 1',help_text='Máximo 10 pontos', max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10)], null=True, blank=True, default = 0)    
    arquivo_corrigido_responsavel = models.FileField('Arquivo do artigo corrigido pelo avaliador 1', null=True, blank=True, upload_to='midias', help_text='Use formato .pdf para enviar seu arquivo corrigido')

    #Campos de parecer avaliador suplente
    dt_avaliacao_suplente = models.DateTimeField('Data da avaliação do avaliador 2', null=True, blank=True)
    parecer_avaliador_suplente = models.TextField('Parecer do avaliador 2 (5000 caracteres)', max_length=5000, null=True, blank=True, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    parecer_rebanca_avaliador_suplente = models.TextField('Parecer de REAVALIAÇÃO do avaliador 2 (5000 caracteres)', max_length=5000, null=True, blank=True, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
   
    merito_desenvolvimento_suplente = models.DecimalField('Desenvolvimento',help_text='Máximo 10 pontos', max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10)], null=True, blank=True, default = 0)
    merito_redacao_suplente = models.DecimalField('Redação do texto'),help_text='Máximo 10 pontos', max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10)], null=True, blank=True, default = 0)
    merito_apresentacao_suplente = models.DecimalField('Apresentação'),help_text='Máximo 10 pontos', max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10)], null=True, blank=True, default = 0)
    nota_final_suplente = models.DecimalField('Final Avaliador 2'),help_text='Máximo 10 pontos', max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10)], null=True, blank=True, default = 0)    
    arquivo_corrigido_suplente = models.FileField('Arquivo do artigo corrigido pelo avaliador 2'), null=True, blank=True, upload_to='midias', help_text='Use formato .pdf para enviar seu arquivo corrigido')

    #campos de parecer avaliador convidado
    dt_avaliacao_convidado = models.DateTimeField('Data da avaliação do avaliador 3', null=True, blank=True)
    parecer_avaliador_convidado = models.TextField('Parecer do avaliador 3 (5000 caracteres)', max_length=5000, null=True, blank=True, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    parecer_rebanca_avaliador_convidado = models.TextField('Parecer de REAVALIAÇÃO do avaliador 3 (5000 caracteres)', max_length=5000, null=True, blank=True, help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    merito_desenvolvimento_convidado = models.DecimalField('Desenvolvimento'),help_text='Máximo 10 pontos', max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10)], null=True, blank=True, default = 0)
    merito_redacao_convidado = models.DecimalField('Redação do texto'),help_text='Máximo 10 pontos', max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10)], null=True, blank=True, default = 0)
    merito_apresentacao_convidado = models.DecimalField('Apresentação'),help_text='Máximo 10 pontos', max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10)], null=True, blank=True, default = 0)
    nota_final_convidado = models.DecimalField('Final Avaliador 3'),help_text='Máximo 10 pontos', max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10)], null=True, blank=True, default = 0)    
    arquivo_corrigido_convidado = models.FileField('u''Arquivo do artigo corrigido pelo avaliador 3', null=True, blank=True, upload_to='midias', help_text='Use formato .pdf para enviar seu arquivo corrigido')

    media_final_avaliacao = models.DecimalField('Média Final',help_text='Máximo 10 pontos', default = 0, max_digits=4, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10)], null=True, blank=True)    
    intercorrencias = models.TextField('Intercorrências do processo de avaliação (20000 caracteres)', max_length=20000, null=True, blank=True, help_text='Coordenador, use esse espaço para anotar qualquer intercorrência do processo de avaliação!')
    
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)
    
    dic_pesos = {
        "merito_acompanhamento_orientador" : 2,
        "merito_desenvolvimento_orientador" : 4,
        "merito_redacao_orientador" : 3,
        "merito_apresentacao_orientador" : 1,
        "merito_desenvolvimento_responsavel_suplente" : 5,
        "merito_redacao_responsavel_suplente" : 3,
        "merito_apresentacao_responsavel_suplente" : 2,
    }
    
    class Meta:
        ordering = ['submissao__turma','submissao__aluno__nome']

    def __str__(self):
        return '%s' % (self.submissao)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
            
        super(Avaliacao, self).save(*args, **kwargs)
    
    @property
    def get_absolute_url(self):
        return reverse('avaliacao_update', kwargs={'slug': self.slug})
    
    @property
    def get_delete_url(self):
        return reverse('avaliacao_delete', kwargs={'slug': self.slug})

    @property
    def get_avaliacao_coordenador_orientador_url(self):
        return reverse('minha_avaliacao_orientador', kwargs={'slug': self.slug})
  
    @property
    def get_avaliacao_coordenador_responsavel_url(self):
        return reverse('minha_avaliacao_responsavel', kwargs={'slug': self.slug})

    @property
    def get_avaliacao_coordenador_suplente_url(self):
        return reverse('minha_avaliacao_suplente', kwargs={'slug': self.slug})

    # para appmembro
    @property
    def get_avaliacao_orientador_url(self):
        return reverse('appmembro_minha_avaliacao_orientador', kwargs={'slug': self.slug})
  
    @property
    def get_avaliacao_responsavel_url(self):
        return reverse('appmembro_minha_avaliacao_responsavel', kwargs={'slug': self.slug})

    @property
    def get_avaliacao_suplente_url(self):
        return reverse('appmembro_minha_avaliacao_suplente', kwargs={'slug': self.slug})
    
    @property
    def get_avaliacao_convidado_url(self):
        return reverse('appmembro_minha_avaliacao_convidado', kwargs={'slug': self.slug})

    @property
    def get_media_atualizada(self):
        if  self.avaliador_convidado:
            return (self.nota_final_orientador + self.nota_final_responsavel + self.nota_final_suplente + self.nota_final_convidado) / 4
        
        return (self.nota_final_orientador + self.nota_final_responsavel + self.nota_final_suplente) / 3

    @property
    def get_parecer_liberado_url(self):
        return reverse('avaliacao_parecer_detail', kwargs={'slug': self.slug})
    
    @property
    def get_parecer_liberado_aluno_url(self):
        return reverse('appaluno_avaliacao_parecer_detail', kwargs={'slug': self.slug})
    
    @property
    def get_parecer_liberado_orientador_url(self):
        return reverse('appmembro_avaliacao_parecer_detail', kwargs={'slug': self.slug})

    @property
    def get_parecer_impressao_url(self):
        return reverse('avaliacao_pdf', kwargs={'slug': self.slug})
    
    @property
    def get_termo_banca_impressao_url(self):
        return reverse('avaliacao_termobanca_pdf', kwargs={'slug': self.slug})
    
    @property
    def get_termo_biblioteca_impressao_url(self):
        return reverse('avaliacao_termobiblioteca_pdf', kwargs={'slug': self.slug})
    
    @property
    def get_meu_parecer_impressao_url(self):
        return reverse('minha_avaliacao_pdf', kwargs={'slug': self.slug})
    