from django.shortcuts import render


# Create your views here.
def user_dashboard(request, sub_path=None):
    paths = [component for component in sub_path.split('/') if '.' not in component and component != ''] if sub_path is not None else []
    context = {
        'paths': paths
    }
    return render(request, 'dashboard/user_dashboard.html', context)




