from django.shortcuts import render

# Create your views here.
from django.views import View

from accounts.models import CustomUser


class ORMVIew(View):
    def get(self, request):
        results = CustomUser.objects.all()
        return render(request, 'templates/home.html', {'results': results})