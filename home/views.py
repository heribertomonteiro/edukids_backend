from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView,DetailView
from django.urls import reverse_lazy
from .models import Post, Evento
import calendar
from datetime import datetime, timedelta
from .forms import PostForm, EventoForm

# Create your views here.
def home(request):
    return render(request, "index.html")

class PostListView(ListView):
    template_name = "listpost.html"
    model = Post
    context_object_name = 'posts'

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "createpost.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('lista')

    def form_valid(self, form):
        return super().form_valid(form)
    
class DetalhesEventoView(DetailView):
    model = Evento
    template_name = 'detalhes_evento.html' # Crie este template
    context_object_name = 'evento' # O nome da variável no template
    
class CalendarioAnualView(TemplateView):
    template_name = 'calendario.html' # Certifique-se que o nome do template está correto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Sempre usa o ano atual
        year = datetime.now().year 
        
        cal = calendar.Calendar()
        meses_com_eventos = []

        # Otimização: Busque todos os eventos do ano de uma vez
        eventos_do_ano = Evento.objects.filter(
            data__year=year
        ).order_by('data')

        for month_num in range(1, 13): # De janeiro (1) a dezembro (12)
            month_name = calendar.month_name[month_num]
            month_calendar = cal.monthdayscalendar(year, month_num)
            
            dias_do_mes = []
            for week in month_calendar:
                semana = []
                for day in week:
                    dia_data = None
                    eventos_no_dia = []
                    if day != 0: # 0 representa dias fora do mês
                        dia_data = datetime(year, month_num, day).date()
                        eventos_no_dia = [
                            evento for evento in eventos_do_ano 
                            if evento.data == dia_data
                        ]
                    
                    semana.append({
                        'dia_numero': day,
                        'data_completa': dia_data,
                        'eventos': eventos_no_dia,
                        'hoje': (dia_data == datetime.now().date()) if dia_data else False
                    })
                dias_do_mes.append(semana)

            meses_com_eventos.append({
                'numero': month_num,
                'nome': month_name,
                'dias': dias_do_mes
            })

        context['year'] = year
        context['meses'] = meses_com_eventos
        # Removemos 'next_year' e 'prev_year' do contexto
        
        return context

class EventoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create_event.html'
    model = Evento
    form_class = EventoForm
    success_url = reverse_lazy('calendario')