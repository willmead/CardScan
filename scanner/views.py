from django.views import generic
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Card
from .scan_tools.card_factory import CardFactory
from .scan_tools.scanner import Scanner


class IndexView(generic.TemplateView):
    template_name = 'scanner/index.html'
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'cards': Card.objects.all().order_by('number')})
        return context


class AddCardView(generic.TemplateView):
    template_name = 'scanner/add_card.html'


@csrf_exempt
def scan_card(request):

    card_factory = CardFactory()
    scanner = Scanner()

    image = request.FILES["image"]
    card_text = scanner.scan(image)
    number, year, name, team = card_factory.create_card(card_text)

    card = Card()
    card.number = int(number)
    card.year = int(year)
    card.name = name
    card.team = team
    card.save()

    data = {
        'number': number,
        'year': year,
        'name': name,
        'team': team
    }
    return JsonResponse(data)
