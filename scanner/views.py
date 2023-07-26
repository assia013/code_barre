from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponseServerError
from .models import User, Category, Marque, Produit, code_serie
from django.contrib import messages
from . import models
from django import forms
from .forms import SignupForm, CategoryForm, marqueForm, produitForm, codeForm
from django.contrib.auth.decorators import login_required
from .camera import VideoCamera
#bib scan
import cv2 # read image/ camera / video input
from pyzbar import pyzbar #bib de decodage de code
import time
import threading 

def lire_code_barre(image):
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray) # Détecter les codes-barres dans l'image 
    code_serie = []
    # Vérifier si des codes-barres ont été détectés
    if len(barcodes) > 0:
        barcode = barcodes[0]
        code_serie = barcode.data.decode("utf-8")
    #elif serial in code_serie:
    #    serial ="ce code existe déjà"
    else:
        code_serie="Aucun code-barre n'a été détecté."
    return code_serie

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "You logged in successfully")

            return redirect('interface')
        else:
            messages.error(request, "Invalid Email or password. Try again!")

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user.username}!')
            return redirect('register')
        else:
            for error in form.errors:
                messages.error(request, form.errors[error])
    else:
        form = SignupForm()
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def is_user(user):
    return user.groups.filter(name='user').exists()

def afterlogin_view(request):
    if is_user(request.user):
        accountapproval=models.User.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('interface')
        else:
            return render(request,'login.html')

@login_required
def interface(request):
    user=User.objects.get(id=request.user.id)
    category = Category.objects.all()
    mark = Marque.objects.all()
    product = Produit.objects.all()
    #ouvrir la camera
    """video = cv2.VideoCapture(0)  
    serie = ""

    while True:
        ret, frame = video.read()
        if not ret:
            break
        cv2.imshow("Camera", frame)
        serie = lire_code_barre(frame)
        if serie != "Aucun code-barre n'a été détecté.":
            code = code_serie(code=serie)
            code.save()

        # Attendre l'appui sur la touche 'q' pour quitter
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libérer la capture vidéo et fermer les fenêtres
    video.release()
    cv2.destroyAllWindows()
    """
    context = {
        'category': category,
        'mark' : mark,
        'product' : product,
        #'serie': serie
    }
    return render(request,'interface.html',context)



def scanCode ():    
    video = cv2.VideoCapture(0)  
    serie = ""
    while True:
        ret, frame = video.read()
        if not ret:
            break
        cv2.imshow("Camera", frame)
        serie = lire_code_barre(frame)
        if serie != "Aucun code-barre n'a été détecté.":                
            break           
            # Attendre l'appui sur la touche 'q' pour quitter
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # Libérer la capture vidéo et fermer les fenêtres
    video.release()
    cv2.destroyAllWindows()
    return serie
def scanner(request):
    serie=scanCode()
    if request.method == 'POST' :
        form = codeForm(request.POST,initial={'code': serie})
        if form.is_valid():
            form.save()
            return redirect(f'/scanner/?serie={serie}')
    else:
        form = codeForm(initial={'code': serie})
    context={
        'form': form,
        'serie': serie
    }
    return render(request, 'scanner.html', context)



def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorie')
    else:
        form = CategoryForm()
    
    return render(request, 'categorie.html', {'form': form})
def ajouter_marque(request):
    if request.method == 'POST':
        form = marqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marque')
    else:
        form = marqueForm()
    
    return render(request, 'marque.html', {'form': form})
def ajouter_produit(request):
    if request.method == 'POST':
        form = produitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produit')
    else:
        form = produitForm()
    
    return render(request, 'produit.html', {'form': form})
