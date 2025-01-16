from django.shortcuts import render
from .models import Query
from .utils import get_gardening_advice

def home(request):
    response = None
    if request.method == 'POST':
        question = request.POST.get('question')
        response = get_gardening_advice(question)
        Query.objects.create(question=question, response=response)

    return render(request, 'advice/home.html', {'response': response})