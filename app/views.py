from django.http.response import HttpResponse
from django.http.request import HttpRequest


def hey_view(request: HttpRequest, name) -> HttpResponse:
    return HttpResponse(f"Hey, {name}!")


def age_in_view(request: HttpRequest, end, birthyear) -> HttpResponse:
    ageInYear = end - birthyear
    return HttpResponse(ageInYear)


def order_view(request: HttpRequest, burgers, fries, drinks) -> HttpResponse:
    burgerPrice = burgers * 4.50
    friesPrice = fries * 1.5
    drinksPrice = drinks * 1
    totalPrice = burgerPrice + friesPrice + drinksPrice
    return HttpResponse(f"${totalPrice:.2f}")
