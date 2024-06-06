from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def restricted_page(request):
    context = {
        'title': 'Restricted Page',
        'content': '<h1>Great, you are logged in!</h1>'
    }
    return render(request, 'general.html', context)
