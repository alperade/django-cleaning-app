from django.shortcuts import render, redirect
from reservations.models import Reservation
from django.contrib.auth.decorators import login_required
from reservations.forms import ReservationForm, ReservationDeleteForm
from datetime import datetime, timedelta
import pandas as pd


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
            return redirect("datetime", pk=plan.pk)
    else:
        form = ReservationForm()
    context = {"form": form}
    return render(
        request,
        "reservations/create.html",
        context,
    )

@login_required
def ReservationPickDateTimeView(request, pk):
    date_list = pd.date_range(start=datetime.today().strftime('%Y-%m-%d'),end=(datetime.today() + timedelta(days=7)),freq="D").to_pydatetime().tolist()
    filtered_list = []
    for item in Reservation.objects.values_list('service_date_time').all():
        if item[0]:
            year = item[0].year
            month = item[0].month
            day = item[0].day
            hour = item[0].hour
            filtered_list.append(datetime(year,month,day,hour,0))
    new_list = []
    for date in date_list:
        year = date.year
        month = date.month
        day = date.day
        for hour in range(9,19):
            if datetime(year,month,day,hour,0) not in filtered_list:
                new_list.append(datetime(year,month,day,hour,0))
    if request.method == "GET":
        print(request.GET)
    context = {"reservation": Reservation.objects.filter(user=request.user).get(pk=pk), "times": new_list}

    return render(request, "reservations/datetime.html", context)

@login_required
def ReservationUpdateView(request, pk):
    plan = Reservation.objects.filter(user=request.user).get(pk=pk)
    if request.method == "POST":
        str_date = request.POST["date"]
        list_date = str_date.split(",")
        month = int(list_date[1])
        plan.service_date_time = datetime(int(list_date[0]),month,int(list_date[2]),int(list_date[3]),0)
        plan.save()

    context = {"reservations": Reservation.objects.filter(user=request.user)}

    return render(request, "reservations/home.html", context)



@login_required
def ReservationDetailView(request, pk):
    context = {"reservation": Reservation.objects.filter(user=request.user).get(pk=pk)}

    return render(request, "reservations/detail.html", context)


@login_required
def ReservationDeleteView(request, pk):
    plan = Reservation.objects.filter(user=request.user).get(pk=pk)
    if request.method == "POST":
        form = ReservationDeleteForm(request.POST, instance=plan)
        if form.is_valid():
            plan.delete()
            return redirect("home")
    else:
        form = ReservationDeleteForm(instance=plan)
    context = {
        "form": form,
        "reservation": plan,
    }
    return render(request, "reservations/delete.html", context)
