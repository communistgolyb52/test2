from django.shortcuts import render

# Create your views here.


def main (request) :
    cities = ["Владимир", "Сургут", "Дзержинск", "Подольск"]

    return render (request, "index.html", {"cities": cities})