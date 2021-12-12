from django.shortcuts import render
from .models import Game
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def list_games(request):
	object_list = Game.objects.all()
	num = [1, 2, 3, 4, 9, 10, 12, 19]
	return render(
			request, 
			"appgames/list.html", 
			{"object_list": object_list, "num": num, }
		)