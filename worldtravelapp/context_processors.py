from .models import Country,Review
from django.db.models import Count, Min, Sum, Avg

def countrys_f(request):
    return {"countrys_f": Country.objects.annotate(sort=Sum('tours__order_count')).order_by('-sort')[:5]}

def reviews(request):
    return {"reviews": Review.objects.order_by('-created_date')[:3]}
