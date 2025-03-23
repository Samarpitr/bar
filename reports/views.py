from django.shortcuts import render
from .models import Expense, Income
from django.core.paginator import Paginator
from django.http import JsonResponse

def reports(request):

    income_years = Income.objects.dates('date', 'year', order='DESC')
    expense_years = Expense.objects.dates('date', 'year', order='DESC')
    years = sorted(set(date.year for date in income_years) | set(date.year for date in expense_years), reverse=True)
    context = {
        "years": years
    }
    return render(request, 'reports.html', context=context)


def records(request):
    year = request.GET.get('year')
    report_of = request.GET.get('report_of')
    import pdb; pdb.set_trace() 
    model = getattr(globals(), report_of, None)
    if model and model in [Income, Expense]:
        records = model.objects.filter(date__year=year)
    else:
        records = []

    records_paginator = Paginator(records, 10)  # Show 10 incomes per page
    page_number = request.GET.get('page')
    records = records_paginator.get_page(page_number)

    return JsonResponse({
        "records": records,
        "year": year
    })

