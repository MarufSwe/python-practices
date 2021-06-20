MarufBio = {
    'first_name': "Maruf",
    'last_name': "Khan",
    'age': 25,
    'Experiences': {
        'mobileApp': "ADN Telecom",
        'webApp': "Cloud Production",
        'Skills': {
            'language': "Java, Python, PHP",
            'framework': "Vue, Django"
        }
    }
}

for bio, exp in MarufBio.items():
    print(bio, ":", exp)

    # for key in bio:
    #     print(bio[key])