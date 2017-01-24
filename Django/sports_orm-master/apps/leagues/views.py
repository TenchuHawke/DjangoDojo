from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

from . import team_maker

def index(request):
	context = {
		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		# "players": Player.objects.all(),
		# "leagues": League.objects.filter(sport__contains = "Baseball")
		# "leagues": League.objects.filter(name__contains = "Women",
		"leagues": League.objects.filter(sport__contains = "Hockey"),
		# "leagues": League.objects.exclude(sport__contains = "Football")
		# "leagues": League.objects.filter(name__contains = "Conference")
		# "leagues": League.objects.filter(name__contains = "Atlantic")
		# "teams": Team.objects.filter(location__contains = "Dallas"),
		# "teams": Team.objects.filter(team_name__contains = "raptors")
		# "teams": Team.objects.filter(location__contains = "city")
		# "teams": Team.objects.filter(location__contains = "Dallas"),
		# "teams": Team.objects.filter(team_name__startswith = "T")
		# "teams": Team.objects.order_by('location')
		# "teams": Team.objects.order_by('-team_name')
		# "players": Player.objects.filter(last_name__contains = 'Cooper'),
		# "players": Player.objects.filter(first_name__contains = 'Joshua'),
		# "players": Player.objects.filter(last_name__contains = 'Cooper').exclude(first_name__contains = 'Joshua')
		# "players": Player.objects.filter(Q(first_name__contains = 'Wyatt') | Q(first_name__contains = 'Alexander')),
		# "teams" : Team.objects.filter(league__name__contains="Atlantic soccer Conference"),
		# "players" : Player.objects.filter(curr_team__team_name__contains = "penguins")
		# "players" : Player.objects.filter(curr_team__league__name__contains = "International Collegiate Baseball Conference")
		# "players" : Player.objects.filter(Q(curr_team__league__name__contains = "American Conference of Amateur Football")&Q(last_name__contains = "Lopez"))
		# "players" : Player.objects.filter(curr_team__league__sport__contains = "Football")
		# "teams" : Team.objects.filter(curr_players__first_name__contains = "Sophia")
		# "leagues" : League.objects.filter(teams__curr_players__first_name__contains = "Sophia"),
		# "players" : Player.objects.filter(last_name__contains = "flores").exclude(curr_team__team_name__contains = "Roughriders")
		# "teams" : Team.objects.filter(Q(all_players__last_name__contains ='evans')&Q(all_players__first_name__contains = "samuel")),
		# "players" : Player.objects.filter(all_teams__team_name__contains = "Tiger-Cats"),
		# "players" : Player.objects.filter(all_teams__team_name__contains = "Vikings").exclude(curr_team__team_name__contains = "vikings")

		"grid" : Player.objects.all(),
		"players" : Player.objects.all(),
		"teams" : Team.objects.annotate(player_count=Count('all_players')).filter(player_count__gte=12),
		"players" : Player.objects.annotate(team_count=Count('all_teams')).order_by('-team_count')

	}

	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
