age_recommendations = {
    "0-9": "Focus on play-based learning, sensory experiences, and developing basic social skills.",
    "10-19": "Encourage independence, self-expression, critical thinking, and relationship-building.",
    "20-29": "Support career exploration, personal growth, relationship building, and goal setting.",
    "30-39": "Emphasize work-life balance, personal health, family building, and skill development.",
    "40-49": "Focus on career stability, managing stress, healthy living, and pursuing hobbies.",
    "50-59": "Encourage health check-ups, financial planning, and active social engagement.",
    "60-69": "Support active lifestyle, healthy retirement planning, and staying socially connected.",
    "70-79": "Focus on mental and physical well-being, light activities, and family connections.",
    "80-89": "Emphasize comfort, social interaction, gentle physical activity, and mental engagement.",
    "90-99": "Encourage emotional support, family bonds, and maintaining familiar routines.",
    "100+": "Celebrate life achievements, ensure comfort, and provide emotional presence."
}

def random_platform(text, age):
    return (f'{text}: {age} ')

def recom_age():
    while True:
        print('Choose your age or q-to exit:\n'
        "0-9\n"
        "10-19\n"
        "20-29\n"
        "30-39\n"
        "40-49\n"
        "50-59\n"
        "60-69\n"
        "70-79\n"
        "80-89\n"
        "90-99\n"
        "100+")
        age = input('Enter your age diapazon: ') 
        if age in age_recommendations:
            age = age_recommendations[age]
            actual_recomendation = random_platform('Your recomindatiions are:', age)
            print(f'{actual_recomendation}')       
recom_age()