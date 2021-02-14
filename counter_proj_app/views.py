from django.shortcuts import redirect, render, HttpResponse

def index(request):
    # counter key exist in session, increment counter by 1
    if 'counter' in request.session:
        request.session['counter'] += 1
        print(request.session['counter'])
    # If counter does not exist create counter and assign value of 1 to counter
    else:
        request.session['counter'] = 1

    return render(request, 'index.html')

def destroy(request):
    print('redirected boyyy!')
    # counter exist in session; then clear that mf
    if 'counter' in request.session:
        request.session.clear()
        print("Destroy: And now counter was reset")
    # else it will print to console that session is empty
    else:
        print(" 'counter' does not exist in session so, it was not reseted ")
    # Redirect to root
    return redirect('/')
