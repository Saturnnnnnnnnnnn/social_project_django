from django.shortcuts import render, redirect
from .forms import NewsForm
from .models import Profile

def dashboard(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            News = form.save(commit=False)
            News.user = request.user
            News.save()
            return redirect("djangram:dashboard")
            form = NewsForm()
    form = NewsForm()
    return render(request, "djangram/dashboard.html", {"form": form})



def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "djangram/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "djangram/profile.html", {"profile": profile})





