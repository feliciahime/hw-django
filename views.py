import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # This is similar to ones we have done before. Instead of keeping
    # the HTML / template in a separate directory, we just reply with
    # the HTML embedded here.
    return HttpResponse('''
        <h1>Welcome to my home page!</h1>
        <a href="/about-me">About me</a> <br />
        <a href="/github-api-example">See my GitHub contributions</a> <br />
    ''')


def about_me(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
        'name': 'Felicia Becerra',
        'pokemon': 'Mittens',
    }
    return render(request, 'about_me.html', context)


def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://github.com/feliciahime')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

def my_portfolio(request):
    # We can also combine Django with APIs
    context = {
        'name': 'Felicia Becerra',
        'pokemon': 'Mittens',
    }
    return render(request, 'portfolio.html', context)

