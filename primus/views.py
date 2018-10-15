from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .forms import LogIn
from .models import Graphs

import os
import json

#django views

def homepage(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            graphs = Graphs.objects.all()
            print(len(graphs))
            context= {
                'Graphs':graphs,
                'printthis':"hello beautiful"}
            return render(request,'admin_panel.html',context)

    else:
        form = LogIn()
    return render(request,'index.html',{'form':form})

def GraphTypeChoosen(request,id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_authenticated:
        form = LogIn
        message = "To continue please login."
        context = {
            "form":form,
            "message":message
        }
        return render (request,'login.html',context)

    graph = get_object_or_404(Graphs, id = id)
    context={
        "graph":graph
    }
    return render(request,'graph_options.html',context)


def Visualise(request):
        if request.method == 'POST':
            # if form.is_valid():
            name = request.POST['name']
            node_file = request.FILES.getlist('nodes')
            print(node_file)
            for nodes in node_file:
                print(nodes.read())
            print(name)
            context= {
                'printthis':"hello beautiful"}
            return render(request,'admin_panel.html',context)
