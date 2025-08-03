from django.shortcuts import render, redirect
from .models import PredictionHistory
import joblib
import numpy as np
import pandas as pd
import os

model_path = os.path.join(os.path.dirname(__file__), '..', 'car_price_model.pkl')
model = joblib.load(model_path)

# Définis les listes une fois pour les utiliser dans la vue
BRANDS = ['Maruti', 'Hyundai', 'Datsun', 'Honda', 'Tata', 'Chevrolet',
          'Toyota', 'Jaguar', 'Mercedes-Benz', 'Audi', 'Skoda', 'Jeep',
          'BMW', 'Mahindra', 'Ford', 'Nissan', 'Renault', 'Fiat',
          'Volkswagen', 'Volvo', 'Mitsubishi', 'Land', 'Daewoo', 'MG',
          'Force', 'Isuzu', 'OpelCorsa', 'Ambassador', 'Kia']

FUELS = ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric']
SELLER_TYPES = ['Individual', 'Dealer', 'Trustmark Dealer']
TRANSMISSIONS = ['Manual', 'Automatic']

def home(request):
    if request.method == 'POST':
        return redirect('predict_price')
    return render(request, 'prediction/home.html')

def predict_price(request):
    if request.method == 'POST':
        brand = request.POST['Brand']
        fuel = request.POST['Fuel']
        seller_Type = request.POST['Seller_Type']
        transmission = request.POST['Transmission']
        KM_Driven = int(request.POST['KM_Driven'])
        car_Age = int(request.POST['Car_Age'])
        is_first_owner = request.POST.get('Is_First_Owner') == 'on'  # checkbox renvoie 'on'

        # Créer un DataFrame avec les bons noms de colonnes
        input_data = pd.DataFrame([{
            'Brand': brand,
            'Fuel': fuel,
            'Seller_Type': seller_Type,
            'Transmission': transmission,
            'KM_Driven': KM_Driven,
            'Car_Age': car_Age,
            'Is_First_Owner': is_first_owner
        }])

        # Prédiction
        prix = model.predict(input_data)[0]

        # Sauvegarde en base
        PredictionHistory.objects.create(
            brand=brand,
            fuel=fuel,
            seller_type=seller_Type,
            transmission=transmission,
            km_driven=KM_Driven,
            car_age=car_Age,
            is_first_owner=is_first_owner,
            predicted_price=prix
        )

        return render(request, 'prediction/result.html', {'prix': round(prix, 2)})

    # GET : afficher le formulaire avec les listes
    history = PredictionHistory.objects.order_by('-timestamp')[:10]
    return render(request, 'prediction/form.html', {
        'brands': BRANDS,
        'fuels': FUELS,
        'seller_types': SELLER_TYPES,
        'transmissions': TRANSMISSIONS,
        'history': history
    })

def clear_history(request):
    if request.method == 'POST':
        PredictionHistory.objects.all().delete()
    return redirect('predict_price')

def dashboard(request):
    # Infos synthétiques du modèle simple
    stats = {
        "Modele": "Random Forest",
        "Variables_utilisees": ["Brand", "Fuel", "Seller_Type", "Transmission", "KM_Driven", "Car_Age", "Is_First_Owner"],
        "Nombre_Ligne_Dataset": 4340,
        "Exemple_de_donnees": [
            {"Brand": "Maruti", "Fuel": "Petrol", "Seller Type": "Individual", "Transmission": "Manual", "KM_Driven": 70000, "Car_Age": 18, "Is_First_Owner": "First Owner"},
            {"Brand": "Maruti", "Fuel": "Petrol", "Seller Type": "Individual", "Transmission": "Manual", "KM_Driven": 50000, "Car_Age": 18, "Is_First_Owner": "First Owner"},
            {"Brand": "Hyundai", "Fuel": "Diesel", "Seller Type": "Individual", "Transmission": "Manual", "KM_Driven": 100000, "Car_Age": 13, "Is_First_Owner": "First Owner"},
            {"Brand": "Datsun", "Fuel": "Petrol", "Seller Type": "Individual", "Transmission": "Manual", "KM_Driven": 46000, "Car_Age": 8, "Is_First_Owner": "First Owner"},
            {"Brand": "Honda", "Fuel": "Diesel", "Seller Type": "Individual", "Transmission": "Manual", "KM_Driven": 141000, "Car_Age": 11, "Is_First_Owner": "Second Owner"}

        ]
    }
    return render(request, 'prediction/dashboard.html', {"stats": stats})