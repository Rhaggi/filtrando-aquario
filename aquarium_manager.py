import json
from datetime import datetime
from pathlib import Path

arquivo = open('aquarium.json', encoding='utf8')
data = json.load(arquivo)
animals = data['data']

# Opção com função
def verify_fish(animal):
    if animal['type'] == 'fish':
        return True
    return False

# Opção com lambda
# animals_fish = list(filter(lambda animal: (animal['type'] == 'fish'), animals))

animals_fish = list(filter(verify_fish, animals))

def animal_name(animal):
    return animal['name']

animals_fish_name = list(map(animal_name, animals_fish))

def assign_to_tank(animals, name_selected, new_tank_number):
    def change_tank_number(animal):
        if animal['name'] in name_selected:
            animal['tank_number'] = 42
        return animal 
    return list(map(change_tank_number, animals))

new_aquario = assign_to_tank(animals, animals_fish_name, 42)

def save_new_version(data, base_dir="snapshots"):
    Path(base_dir).mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{base_dir}/aquarium_{ts}.json"
    with open(filename, "w", encoding="utf8") as f:
        json.dump({"data": data}, f, ensure_ascii=False, indent=2)
    print(f"Nova versão salva em: {filename}")

save_new_version(new_aquario)

arquivo.close()
