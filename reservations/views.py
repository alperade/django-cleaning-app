from django.shortcuts import render, redirect
from reservations.models import Reservation, Cleaner, Time
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
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            form.save_m2m()
            print(request.POST)
            return redirect("detail", pk=plan.pk)
    else:
        form = ReservationForm()
    context = {"form": form}
    return render(
        request,
        "reservations/create.html",
        context,
    )

@login_required
def ReservationDetailView(request, pk):
    times = Time.times
    if request.method == "GET":
        print(request.GET)
    context = {"reservation": Reservation.objects.filter(user=request.user).get(pk=pk), "times": times}

    return render(request, "reservations/detail.html", context)

@login_required
def ReservationUpdateView(request, pk):
    plan = Reservation.objects.filter(user=request.user).get(pk=pk)
    if request.method == "POST":
        print(request.POST)
        plan.service_time = request.POST["service_time"]
        plan.save()
        Time.times.remove(request.POST["service_time"])
        # what's the best way to create time slots per day


    context = {"reservations": Reservation.objects.filter(user=request.user)}

    return render(request, "reservations/home.html", context)
