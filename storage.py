import csv
from pathlib import Path

new_data = ['продукт', 'количество', 'время', 'аллергия']
on_screen = str()
on_file = list()

# checks if foods.csv exists
def get_data():
    global on_file
    file_path = Path('foods.csv')
    if file_path.exists():
        with open('foods.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            on_file= list(reader)

# adds a new entry to the main screen and to foods.csv
def add_new_food():
    global new_data
    global on_file
    global on_screen
    def_new_data = ['продукт', 'количество', 'время', 'аллергия']
    new_data[0] = on_screen
    on_file.append(new_data)
    new_data = def_new_data
    with open('foods.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for food in on_file:
            writer.writerow(food)
    get_data()

# updates the .csv with new data
def write_to_file():
    global on_file
    file_path = Path('foods.csv')
    if file_path.exists():
        with open('foods.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for food in on_file:
                writer.writerow(food)

# deletes an entry from the main screen and from the .csv file
def remove_from_file():
    global on_file
    global on_screen
    get_data()
    file_path = Path('foods.csv')
    if file_path.exists():
        for x in on_file:
            for y in x:
                if y == on_screen:
                    on_file.remove(x)
                    break
    with open('foods.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for food in on_file:
            writer.writerow(food)
    get_data()