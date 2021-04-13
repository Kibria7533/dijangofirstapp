
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from .forms import StForm


def st(request):
     form = StForm(request.POST or None)
     if form.is_valid():
         form.save()

     context = {'form': form}

     return render(request, 'form.html', context)


def list_view(request):
    context = {}
    context["dataset"] = StForm.objects.all()
    return render(request, "list_view.html", context)


def update_view(request, id):
    context = {}
    obj = get_object_or_404(StForm, id=id)
    form = StForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("update/" + id)
    context["form"] = form
    return render(request, "update.html", context)


def delete(request, id):
    context = {}
    obj = get_object_or_404(StForm, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "delete.html", context)