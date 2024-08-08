# Generated by Django 5.0.5 on 2024-07-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissao',
            name='arquivo_comite_etica',
            field=models.FileField(blank=True, help_text='Utilize arquivo compactado .ZIP', null=True, upload_to='midias', verbose_name='Arquivo ZIPADO com documentação necessária de pesquisa em Humanos e Animais'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='status',
            field=models.CharField(choices=[('EM EDICAO', 'Em edição'), ('EM ANALISE', 'Em análise'), ('EM CORRECAO', 'Em correção'), ('APROVADO', 'Aprovado'), ('RETIRADO PELO RESPONSAVEL', 'Retirado pelo responsável'), ('RETIRADO PELO COORDENADOR', 'Retirado pelo coordenador'), ('REPROVADO', 'Reprovado')], default='EM EDICAO', max_length=25, verbose_name='Status da submissão'),
        ),
    ]
