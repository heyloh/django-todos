from django.shortcuts import render
from todos.models import Todo

# Create your views here.
def homepage(request):
    data = Todo.objects.all()
    return render(request, "index.html", {'todos': data})

def todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    return render(request, '', {'todo': todo})