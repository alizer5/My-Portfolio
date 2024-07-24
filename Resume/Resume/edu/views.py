from django.shortcuts import render

def skills(request):
    context={'skills':'active'}
    return render(request,'edu/skill.html',context)
def resume(request):
    context={
        'resume': 'active'
    }
    return render(request,'edu/res.html',context)