from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.
def index(request):
    # use of : "from .models import Todo"
    queryset = Todo.objects.all()
    form = TodoForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=True)
        instance.save()
        return redirect('index')
    context = {
        "queryset": queryset,
        'form': form,
    }
    return render(request, 'index.html', context)


def done(request, id):
    query = Todo.objects.get(id=id)
    query.done = True
    query.save()
    return redirect('index')


def undone(request,id):
    query = Todo.objects.get(id=id)
    query.done = False
    query.save()
    return redirect('index')


def delete(request,id):
    query = Todo.objects.get(id=id)
    query.delete()
    return redirect('index')


