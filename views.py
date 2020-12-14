import requests
from django.http import HttpResponse
from django.shortcuts import render
import glob
import os


def index(request):
    content_html = open("content/index.html").read() 
    context = {
        "content": content_html, }
    return render(request, "base.html", context)


def about_me(request):
    content_html = open("content/about.html").read() 
    context = {
        "content": content_html, }
    return render(request, "base.html", context)
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    # context = {
    #     'name': 'Felicia Becerra',
    #     'pokemon': 'Mittens',
    # }
    # return render(request, 'about_me.html', context)


def my_blog(request):
    # We can also combine Django with APIs
    response = requests.get('https://github.com/feliciahime')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'blog.html', context)

def my_portfolio(request):
    content_html = open("content/portfolio.html").read() 
    context = {
        "content": content_html, }

    return render(request, 'base.html', context)


    # # We can also combine Django with APIs
    # context = {
    #     'name': 'Felicia Becerra',
    #     'pokemon': 'Mittens',
    # }

# def github_api_example(request):
#     # We can also combine Django with APIs
#     response = requests.get('https://github.com/feliciahime')
#     repos = response.json()
#     context = {
#         'github_repos': repos,
#     }
#     return render(request, 'github.html', context)

