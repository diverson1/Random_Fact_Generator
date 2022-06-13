import random

animal_facts = ['Fleas can jump 350 times its body length.','Hummingbirds are the only birds that can fly backwards.', 'Crocodiles cannot stick their tongue out.', 'Starfish do not have a brain.', 'Slugs have 4 noses.',]
fact_list2 = []
fact_list3 = []


def random_fact_generator(fact_list):  # function will print random fact from any of the lists
    '''Will randomly generator a number from a range equal to the fact list length, 
    this number will be used as the index to pull a random item from the list'''
    r_number = random.randrange(len(fact_list))
    print(fact_list[r_number])


random_fact_generator(animal_facts)