from django.http.response import HttpResponse
from django.http.request import HttpRequest


def hey_view(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"Hey, {name}!")


def age_in_view(request: HttpRequest, end: int, birthyear: int) -> HttpResponse:
    ageInYear = end - birthyear
    return HttpResponse(ageInYear)


def order_view(
    request: HttpRequest, burgers: int, fries: int, drinks: int
) -> HttpResponse:
    burgerPrice = burgers * 4.50
    friesPrice = fries * 1.5
    drinksPrice = drinks * 1
    totalPrice = burgerPrice + friesPrice + drinksPrice
    return HttpResponse(f"${totalPrice:.2f}")
