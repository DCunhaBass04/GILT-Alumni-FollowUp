from django.shortcuts import render, redirect
#from .models import Post
from django.contrib.auth.decorators import login_required
import pandas as pd
import configparser

from automation.change_date import DateChanger

from .forms import DatasForm
from datetime import datetime, time, timezone, timedelta
# Create your views here.


@login_required(login_url="/users/login/")
def posts_list(request):
    config = configparser.ConfigParser()
    config.read('..\conf.cfg')
    url = config['START']['excel_file_path']
    posts = pd.read_excel(url, "Respostas")
    return render(request, 'posts/posts_list.html', {
        'posts': posts.to_html(classes='styled-table', header="true")
    })

@login_required(login_url="/users/login")
def posts_changetime(request):
    form = DatasForm(request.POST)
    if form.is_valid():
        inicio = form.cleaned_data['data_inicio']
        fim = form.cleaned_data['data_fim']

        # Adicionar hora (09:00) e converter para UTC
        dt_inicio = datetime.combine(inicio, time(9, 0)).replace(tzinfo=timezone.utc)
        dt_fim = datetime.combine(fim, time(9, 0)).replace(tzinfo=timezone.utc)

        # Formato: "YYYY-MM-DDTHH:MM:SS.000Z"
        iso_inicio = dt_inicio.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        iso_lembrete = (dt_fim - timedelta(days=3)).strftime('%Y-%m-%dT%H:%M:%S.000Z')
        iso_fim = dt_fim.strftime('%Y-%m-%dT%H:%M:%S.000Z')

        # Aqui podes chamar o método externo
        resultado = processar_datas(iso_inicio, iso_lembrete, iso_fim)

        return render(request, 'posts/posts_changesaccepted.html', {
            'inicio': iso_inicio,
            'fim': iso_fim,
            'resultado': resultado
        })
    return render(request, 'posts/posts_changedate.html', {'form': form})

# Exemplo de método externo
def processar_datas(data_inicio, data_lembrete, data_fim):
    dateChanger = DateChanger()
    return dateChanger.run(data_inicio, data_lembrete, data_fim)