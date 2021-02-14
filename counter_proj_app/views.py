from django.shortcuts import redirect, render, HttpResponse

def index(request):
    print("Inside of Index")
    request.session['counter'] += 1
    print(request.session['counter'])
    return render(request, 'index.html')

# def destroy(request):
#     print('redirected boyyy!')
#     del request.session['counter']
#     print("Destroy: And now counter was reset")
#     return redirect('/')
