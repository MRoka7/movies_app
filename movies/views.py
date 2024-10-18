from django.shortcuts import render, HttpResponse
# the render() function is used to generate and return an HTTP response with a template rendered with the given context (data). It’s one of the most commonly used functions in Django views to display dynamic content on web pages.

# Create your views here.

def index(request):
    context = {
        "movies": ["seven", "topGun", "last Samurai", "gladiator"]
    }
    return render(request, 'movies/index.html', context)

# django hase an expected folder structure for this template
# it expects to see the app name --> app/templates/app/index.html here is movies/templates/movies/index.html
def about(request):
    return render(request, 'movies/about.html',{})