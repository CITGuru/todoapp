# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import TodoList, Category
from django.views.generic import TemplateView
import datetime
# Create your views here.


class Index(TemplateView):
    template_name = 'index.html'



    def get(self,request,**kwargs):
        todos = TodoList.objects.all()  # quering all todos with the object manager
        categories = Category.objects.all()
        return render(request, "index.html", {"todos": todos, "categories": categories})

    def post(self,request,**kwargs):
        todos = TodoList.objects.all() #quering all todos with the object manager
        categories = Category.objects.all() #getting all categories with object manager
        # if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in self.request.POST: #checking if there is a request to add a todo
            title = self.request.POST["description"] #title
            date = str(self.request.POST["date"]) #date
            category = self.request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo
            return redirect("/") #reloading the page

        if "taskDelete" in self.request.POST: #checking if there is a request to delete a todo
            checkedlist = self.request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo

        return render(self.request, "index.html", {"todos": todos, "categories":categories})
#
#
