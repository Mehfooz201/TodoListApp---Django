from django.shortcuts import redirect, render, HttpResponseRedirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http  import require_POST

# Create your views here.

def home(request):
    todoList = Todo.objects.order_by('id')
    form = TodoForm()
    context = {'todoList':todoList, 'form':form }
    return render(request, 'myapp/home.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('home')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('home')



def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    
    return redirect('home')


def deleteAll(request):
    Todo.objects.all().delete()
    
    return redirect('home')

