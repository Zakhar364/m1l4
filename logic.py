from random import randint
import requests

class Pokemon:
    pokemons = {}

    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer

        # количество покемонов на данный момент около 898,
        # но можем запрашивать 1..1000 и падать на Pikachu
        self.pokemon_number = randint(1, 1000)
        self.img = self.get_img()
        self.name = self.get_name()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # front_default содержит ссылку на изображение
            sprite = data['sprites']['other']['dream_world']['front_default']
            if sprite:
                return sprite
        # fallback: Pikachu sprite
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['forms'][0]['name']
        else:
            return "Pikachu"

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img



