from django.shortcuts import render, redirect
from reservations.models import Reservation, Cleaner, ServiceTime
from django.contrib.auth.decorators import login_required
from reservations.forms import ReservationForm


# Create your views here.
@login_required
def ReservationListView(request):
    if request.method == "GET":
        print(request.GET)
    context = {"reservations": Reservation.objects.filter(user=request.user)}

    return render(request, "reservations/home.html", context)

@login_required
def ReservationCreateView(request):
    if request.method == "GET":
        request.GET
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            form.save_m2m()
            print(request.POST)
            return redirect("home")
    else:
        form = ReservationForm()
    context = {"form": form, "service_times":ServiceTime.objects.all()}
    return render(
        request,
        "reservations/create.html",
        context,
    )
