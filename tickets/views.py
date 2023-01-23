from django.shortcuts import render

# Create your views here.


def ticket(request, tn):
    return render(request, 'ticket.html')

