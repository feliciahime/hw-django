import requests
from django.http import HttpResponse
from django.shortcuts import render
import glob
import os


all_html_files = glob.glob("content/*.html")
print(all_html_files)
print(all_html_files[0])
print("--------------")

pages = [ ]
x = 0

title_list = ["Blog ", "Home ", "About Me ", "Portfolio"]

for page in all_html_files:
    file_path = all_html_files[x]
    print(file_path)
    file_name = os.path.basename(file_path) 
    print(file_name)
    name_only, extension = os.path.splitext(file_name) 
    print(name_only)
    print(x)
    pages.append({
        "filename": str(file_path),
        "title": title_list[x],
        "output": ("./docs/" + file_name),
        "link": ("./" + str(file_name)) })
    x += 1

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

