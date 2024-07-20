from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup_page.html", context={"form": form})
