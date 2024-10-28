import random
from django.shortcuts import render

def inventory_management_system_home(request):

    my_list =  [random.randint(1, 100) for _ in range(20)]
    # list_of_strings = [f"my number is {x}" for x in [102, 100, 13, 234, 1334, 2313]]
    # list_of_strings = [f"<li>my number is {x}</li>" for x in [random.randint(1, 100) for _ in range(20)]]

    context = {'my_list': my_list}
    return render(request, 'inventory_management_system/inventory_management_system_home.html', context)
