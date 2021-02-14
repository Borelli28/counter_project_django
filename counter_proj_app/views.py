from django.shortcuts import redirect, render, HttpResponse

def index(request):
    # counter key exist in session, increment counter by 1
    if 'counter' in request.session:
        request.session['counter'] += 1
        print(request.session['counter'])
    # If counter does not exist create counter and assign value of 1
    else:
        request.session['counter'] = 1

    return render(request, 'index.html')

def destroy(request):
    print('redirected boyyy!')
    # request.session.clear()
    print("Destroy: And now counter was reset")
    return redirect('/')
