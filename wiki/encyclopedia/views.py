from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import random as rand
from math import *

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    
    if name:
        entry = util.get_entry(name)
        if entry:
        
            return render(request, 'encyclopedia/post.html', {
                "entry": entry,
                "name":name
               

                          })
        else:
            return render(request, 'encyclopedia/error.html', {
                    "messages": f"{name} does not exist",

                              })
    
def search(request):
    name = request.GET['q']
    print(name)
    entry = util.get_entry(name)
    if entry:
        return render(request, 'encyclopedia/post.html', {
            "entry": entry
            
                      })
    else:
        return render(request, 'encyclopedia/error.html', {
            "messages": f"{name} does not exist",
            
                      })
        
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        if util.get_entry(title):
            return render(request, 'encyclopedia/error.html', {
            "messages": f"{title} already exists",
            
                      })
        else:
            util.save_entry(title, content)
            
    return render(request, 'encyclopedia/create.html')
        
def edit(request, title): 
    if title:
        entry = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            "entry": entry,
            'title':title
        })
    return render(request,"encyclopedia/index.html")
 

def entry_save(request, title):
    if request.method == 'POST':
        content = request.POST['new_content']
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse('post', args=(title,)))
    
def random(request):
    ls = util.list_entries()
    ran = len(ls)
    num = rand.randrange(ran-1)
    return render(request,"encyclopedia/random.html",{
        "ls":util.get_entry(ls[num])
    })
        
    
 	
    



 	

