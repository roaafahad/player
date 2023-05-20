from django.shortcuts import render
from .models import Contact
# Create your views here.


def home(request):
    return render(request, 'P1//home.html')

def about(request):
    return render(request, 'P1//about.html')

# {Changed the name of the function to Contact to avoid collision}
def Contact(request):
    templates = 'contact.html'

    if request.method == 'POST':
        # part 1 take data from the form .
        v_n = request.POST.get('name')
        v_e = request.POST.get('email')
        v_s = request.POST.get('subject')
        v_m = request.POST.get('message')
        # part 2 create a object of the class contact.
        c = contact(name=v_n, email=v_e, subject=v_s, massage=v_m)
        # part 3 save the object in the database.
        c.save()
        # part 4 return the message to the user.
        return render(request, 'P1//T.html')
    else:

        return render(request, 'P1//contact.html')





# Old code

#  if request.method == 'POST':
#         # part 1 take data from the form .
#         v_n = request.POST.get('name')
#         v_e = request.POST.get('email')
#         v_s = request.POST.get('subject')
#         v_m = request.POST.get('massage')

#         contact.objects.contains(name=v_n, email=v_e, subject=v_s, massage=v_m)
#         return render(request,templates)


#         #part 2 send data to the DB :
#         v_con = contact(name=v_n, email=v_e, subject=v_s, massage=v_m)
#         # I import the class and sending the variable that the class need to create that object .
#         v_con.save() # save the object for back the DB.
#         return render(request, 'Aletry//T.html')
#         # After completing the contact us page, the user will be transferred to the thank you page
#     else:
#         return render(request, 'Aletry//contact.html')
