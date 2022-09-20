from django.shortcuts import render, redirect
from reservations.models import Reservation, Address
from django.contrib.auth.decorators import login_required
from reservations.forms import AddressForm, ReservationDeleteForm, ReservationForm
from datetime import datetime, timedelta
import pandas as pd


# Create your views here.
@login_required
def ReservationListView(request):
    if request.method == "GET":
        print(request.GET)
    context = {"reservations": Reservation.objects.filter(user=request.user),
    "address": Address.objects.filter(user=request.user).last()
    }

    return render(request, "reservations/home.html", context)

@login_required
def AddressCreateView(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            form.save_m2m()
            print(request.POST)
            return redirect("home")
    else:
        form = AddressForm()
    context = {"form": form}
    return render(
        request,
        "addresses/add_address.html",
        context,
    )


@login_required
def ReservationDetailView(request, pk):
    context = {"reservation": Reservation.objects.filter(user=request.user).get(pk=pk)}

    return render(request, "reservations/detail.html", context)


@login_required
def ReservationCreateView(request):
    plan = Reservation.objects.filter(user=request.user)
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.address = Address.objects.filter(user=request.user).last()
            str_date = request.POST["date"]
            list_date = str_date.split(",")
            month = int(list_date[1])
            plan.service_date_time = datetime(int(list_date[0]),month,int(list_date[2]),0,0)
            plan.save()
            form.save_m2m()
            return redirect("time_pick", pk=plan.pk)

    context = {"reservations": Reservation.objects.filter(user=request.user)}

    return render(request, "reservations/create_reservation.html", context)

@login_required
def NewReservationPickDateView(request):
    date_list = pd.date_range(start=datetime.today().strftime('%Y-%m-%d'),end=(datetime.today() + timedelta(days=7)),freq="D").to_pydatetime().tolist()
    filtered_list = []
    for item in Reservation.objects.values_list('service_date_time').all():
        if item[0]:
            year = item[0].year
            month = item[0].month
            day = item[0].day
            hour = item[0].hour
            filtered_list.append(datetime(year,month,day,hour,0))
    days_list = []
    for date in date_list:
        year = date.year
        month = date.month
        day = date.day
        days_list.append(datetime(year,month,day,10,0))
    if request.method == "GET":
        print(request.GET)

    context = {"reservation": Reservation.objects.filter(user=request.user), "dates": days_list}

    return render(request, "reservations/create_reservation.html", context)



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

@login_required
def ReservationDateUpdateView(request, pk):
    plan = Reservation.objects.filter(user=request.user).get(pk=pk)
    if request.method == "POST":
        str_date = request.POST["date"]
        list_date = str_date.split(",")
        month = int(list_date[1])
        plan.service_date_time = datetime(int(list_date[0]),month,int(list_date[2]),0,0)
        plan.save()
        return redirect("time_pick", pk=pk)

    context = {"reservations": Reservation.objects.filter(user=request.user)}

    return render(request, "reservations/datepick.html", context)

@login_required
def ReservationPickDateView(request, pk):
    date_list = pd.date_range(start=datetime.today().strftime('%Y-%m-%d'),end=(datetime.today() + timedelta(days=7)),freq="D").to_pydatetime().tolist()
    filtered_list = []
    for item in Reservation.objects.values_list('service_date_time').all():
        if item[0]:
            year = item[0].year
            month = item[0].month
            day = item[0].day
            hour = item[0].hour
            filtered_list.append(datetime(year,month,day,hour,0))
    days_list = []
    for date in date_list:
        year = date.year
        month = date.month
        day = date.day
        days_list.append(datetime(year,month,day,10,0))
    if request.method == "GET":
        print(request.GET)
    context = {"reservation": Reservation.objects.filter(user=request.user).get(pk=pk), "dates": days_list}

    return render(request, "reservations/datepick.html", context)


@login_required
def ReservationTimeUpdateView(request, pk):
    plan = Reservation.objects.filter(user=request.user).get(pk=pk)
    if request.method == "POST":
        str_date = request.POST["time"]
        list_date = str_date.split(",")
        year = plan.service_date_time.year
        month = plan.service_date_time.month
        day = plan.service_date_time.day
        plan.service_date_time = datetime(year,month,day,int(list_date[3]),0)
        plan.save()

    context = {"reservations": Reservation.objects.filter(user=request.user)}

    return render(request, "reservations/home.html", context)

@login_required
def ReservationPickTimeView(request, pk):
    plan = Reservation.objects.filter(user=request.user).get(pk=pk)
    filtered_list = []
    for item in Reservation.objects.values_list('service_date_time').all():
        if item[0]:
            year = item[0].year
            month = item[0].month
            day = item[0].day
            hour = item[0].hour
            filtered_list.append(datetime(year,month,day,hour,0))
    time_list = []
    exist_year = plan.service_date_time.year
    exist_month = plan.service_date_time.month
    exist_day = plan.service_date_time.day
    for hour in range(9,19):
        if datetime(exist_year,exist_month,exist_day,hour,0) not in filtered_list:
            time_list.append(datetime(year,month,day,hour,0))
    if request.method == "GET":
        print(request.GET)

    context = {"reservation": Reservation.objects.filter(user=request.user).get(pk=plan.pk), "times": time_list}

    return render(request, "reservations/timepick.html", context)
