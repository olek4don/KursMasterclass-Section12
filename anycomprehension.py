from data import people, plants_list, plants_dict

people = []       # gotcha for 'all'

if bool(people) and all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipients")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

##### Tim's solution #####
if any(plant.plant_type == "Grass" for plant in plants_dict.values()):
    print("This dict contains grasses")
else:
    print("No grasses in a dict")

if any(plants_dict[key].plant_type == "Grass" for key in plants_dict):
    print("This dict contains grasses")
else:
    print("No grasses in a dict")


##### My solution of challenge #####
if any({PlantDetails.plant_type == "Grass" for PlantDetails in plants_dict.values()}):
    print("This pack contains grass")
else:
    print("No grasses in this pack")
