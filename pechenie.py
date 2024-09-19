recipe = {
    "название": "Печенье с шоколадными чипсами",
    "ингредиенты": [
        "200 г сливочного масла",
        "200 г сахара",
        "2 яйца",
        "1 ч. ложка ванильного экстракта",
        "300 г муки",
        "150 г шоколадных чипсов"
    ],
    "инструкции": [
        "1. Взбейте сливочное масло с сахаром до образования крема.",
        "2. Добавьте яйца и ванильный экстракт, продолжая взбивать.",
        "3. Постепенно добавляйте муку, тщательно перемешивая.",
        "4. Положите шоколадные чипсы и хорошо вымешайте тесто.",
        "5. Сформируйте небольшие шарики из теста и выложите их на противень, смазанный маслом.",
        "6. Выпекайте в духовке при 180 градусах Цельсия в течение 10-12 минут.",
        "7. Остудите печенье перед подачей и наслаждайтесь вкусом!"
    ],
    "время_приготовления": "30 минут",
    "количество_порций": 20
}

print("Рецепт: " + recipe["название"])
print("Ингредиенты:")
for ingredient in recipe["ингредиенты"]:
    print("- " + ingredient)
print("Инструкции:")
for step in recipe["инструкции"]:
    print(step)
print("Время приготовления: " + recipe["время_приготовления"])
print("Количество порций: " + str(recipe["количество_порций"]))
