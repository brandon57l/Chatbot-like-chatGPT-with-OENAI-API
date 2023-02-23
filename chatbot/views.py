import json
from urllib import response
from django.shortcuts import render
import os
import openai
from dotenv import load_dotenv
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


from .models import *

# Create your views here.

@csrf_exempt
def chatbot(request):

    prompt = request.POST.get('prompt')

    # print(json.loads(request.body))

    load_dotenv()   

    openai.api_key = "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"

    infosModel = "Adresse: 8 Rue du Père Potot, 57000 Metz, proche de la gare, proche du parking Coilsin, proche du parking Saint-Thiébault, proche du Centre Pompidou\n Prix moyen: 26 €\n Info: Réservez sur TheFork pour cumuler des Yums et profiter de remises fidélité exclusives\n Menus : Menu Saint-Valentin prix 40 € ce menu comprend apéritif (Kir Royal et amuse bouche) + Entrée (Noix de St Jacques rôtie, velouté d'Endives, Gros Lardons) + Plat principal (Pavé de Veau poêlé, Bouquet de légumes du moment, huile de Morille Blanche) + Dessert (Délice de Chocolat, fruit de la Passion, salpicon d'ananas et citron vert), MENU Formule 16 € Ce menu comprend : Plat du marché + Dessert du marché  qui change tous les jours, Menu 21 € Ce menu comprend : Entrée du marché + Plat du marché + Dessert du marché qui change tous les jour\n Entrée : Quiche aux poireaux et pignons de pin 8 €, Poêlée de champignons et escargots persillés 9 €, Gratin de queues d'écrevisses, fondue de carottes 8 €, Velouté de butternut et sésame doré 8 €, Salade de chou frisé, pomme et lardons 8 € \n Plat : Burger by Karousel 10€, Escalope de veau, crème de chorizo 18€, Risotto de volaille et champignons 16€, Penne à la tomate, fêta e basilic 16 €, Bavette à l'échalote 18 €, Lasagne de chèvre, saumon fumé et épinard 16 €, Filet de Dorade Royale, sauce crustacée 18 €, Steak tartare, frites , salade16 €, Pizza maison aux 3 fromages (Comté, Mozzarella, chèvre) 13,9 €, Pizza maison sicilienne 14,5 € Chorizo, poivrons, champignons, oeuf, Pizza maison végétarienne 13,9 €, Pizza maison Régina 12,9 €\n Dessert: Moelleux au chocolat noir 7 €, Véritable crème brûlée à la vanille 7 €, Feuillantine à la compotée de poire et pistache 7 €, Poêlée de pommes au beurre salé , glace caramel 7 €, Café gourmand 8 €\n Boissons: Bouteille d'eau 3,3 €, Demi-bouteille d'eau 2,8 €, Café 1,9 € \n Choix alimentaires: Options Sans Gluten, Options Vegan, Options Végétariennes \n\n"


    prompt += f"infosModel{str(prompt)}\nConseillé: "
    
    try:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
        )


        chatbot_response = response["choices"][0]["text"]
    except:
        chatbot_response="Error API Connection"


    return JsonResponse({"chatbot_response":chatbot_response})

def chat(request):
    
    context = {"chatbot_response":""}
    return render(request, 'chatbot/chat.html', context)


# DESIGNE INTERFACE

def front_end (request):
    context = {}
    return render(request , 'chatbot/front_end.html', context)
               
        