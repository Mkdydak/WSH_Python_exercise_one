female_fnames = ['Kate', 'Agnieszka', 'Anna', 'Maria', 'Joss', 'Eryka']
male_fnames = ['James', 'Bob', 'Jan', 'Hans', 'Orestes', 'Saturnin']
surnames = ['Smith', 'Kowalski', 'Yu', 'Bona', 'Muster', 'Skinner', 'Cox', 'Brick', 'Malina']
countries = ['Poland', 'United Kingdom', 'Germany', 'France', 'Other']
import random

for i in range(5):
    zm_female_fnames = random.choice(female_fnames)
    zm_male_fnames = random.choice(male_fnames)
    zm_surnemes = random.choice(surnames)
    zm_countries = random.choice(countries)
    zm_age = random.randint(5, 45)

    dictionary_female = {
        'firstname': zm_female_fnames,
        'lastname': zm_surnemes,
        'country': zm_countries,
        'email': zm_female_fnames.lower() + '.' + zm_surnemes.lower() + '@example.com',
        'age': zm_age,
        'adult': '',
        'birth_year': 2019 - zm_age
    }

    dictionary_male = {
        'firstname': zm_male_fnames,
        'lastname': zm_surnemes,
        'country': zm_countries,
        'email': zm_male_fnames.lower() + '.' + zm_surnemes.lower() + '@example.com',
        'age': zm_age,
        'adult': '',
        'birth_year': 2019 - zm_age
    }
    if zm_age >= 18:
        dictionary_female['adult'] = True
    else:
        dictionary_female['adult'] = False

    if zm_age >= 18:
        dictionary_male['adult'] = True
    else:
        dictionary_male['adult'] = False

    print(dictionary_female)
    print('Hi! I\'m ' + dictionary_female['firstname'] + ' ' + dictionary_female['lastname'] + '. I come from ' + dictionary_female['country'] + ' and I was born in ' + str(dictionary_female['birth_year']))
    print(dictionary_male)
    print('Hi! I\'m ' + dictionary_male['firstname'] + ' ' + dictionary_male['lastname'] + '. I come from ' + dictionary_male['country'] + ' and I was born in ' + str(dictionary_male['birth_year']))
