#randomQuizGenerator.py - Creates quizzes with questions and answers in 
#random order, along with the answer key

import random

# The quiz data
capitals = {'Afghanistan': 'Kabul', 'Albania': 'Tirana', 'Algeria': 'Algiers', 'Andorra': 'Andorra la Vela', 'Angola':'Luanda', 'Antigua and Barbuda': 'Saint Johns',
            'Argentina': 'Buenos Aires', 'Armenia': 'Yerevan', 'Australia': 'Canberra', 'Austria': 'Vienna', 'Azerbaijan': 'Baku', 'Bahamas': 'Nassau', 'Bahrain': 'Manama',
            'Bangladesh': 'Dhaka', 'Barbados': 'Bridgetown', 'Belarus': 'Minsk', 'Belgium': 'Brussels', 'Belize': 'Belmopan', 'Benin': 'Proto-Novo', 'Bhutan': 'Thimphu',
            'Bolivia': 'Sucre', 'Bosnia': 'Sarajevo', 'Herzegovina': 'Sarajevo', 'Botswana': 'Gaborone', 'Brazil': 'Brasilia', 'Brunei': 'Bandar Seri Begawan',
            'Bulgaria': 'Sofia', 'Burkina Faso': 'Ouagadougou', 'Burundi': 'Bujumbura', 'Cabo Verde': 'Praia', 'Cambodia': 'Phnom Penh', 'Cameroon': 'Yaounde', 'Canada': 'Ottawa',
            'Central African Republic': 'Bangui', 'Chad': 'N Djamena', 'Chile': 'Santiago', 'China': 'Beijing', 'Colombia': 'Bogota', 'Comoros': 'Moroni', 'Democratic Republic of the Congo': 'Kinshasa',
            'Republic of the Congo': 'Brazzaville', 'Costa Rica': 'San Jose', 'Cote d Ivorie': 'Yamoussoukro', 'Croatia': 'Zagreb', 'Cuba': 'Havana', 'Cyprus': 'Nicosia', 'Czech Republic': 'Prague',
            'Denmark': 'Copenhagen', 'Djibouti': 'Djibouti City', 'Dominicia': 'Roseau', 'Dominican Republic': 'Santo Domingo', 'Ecuador': 'Quito', 'Egypt': 'Cairo', 'El Salvador': 'San Salvador', 'Equatorial Guinea': 'Malabo',
            'Eritrea': 'Asmara', 'Estonia': 'Tallinn', 'Ethiopia': 'Addis Ababa', 'Fiji': 'Suva', 'Finland': 'Helsinki', 'France': 'Paris', 'Gabon': 'Libreville', 'Gambia': 'Banjul', 'Georgia': 'Tbilisi', 'Germany': 'Berlin',
            'Ghana': 'Accra', 'Greece': 'Athens', 'Grenada': 'Saint Georges', 'Guatemala': 'Guatemala City', 'Guinea': 'Conarky', 'Guinea-Bissau': 'Bissau', 'Guyana': 'Georgetown', 'Haiti': 'Port-au-Prince', 'Honduras': 'Tegucigalpa', 'Hungary': 'Budapest',
            'Iceland': 'Reykjavik', 'India': 'New Delhi', 'Indonesia': 'Jakarta', 'Iran': 'Tehran', 'Iraq': 'Baghdad', 'Ireland': 'Dublin', 'Israel': 'Jerusalem', 'Italy': 'Rome',
            'Jamaica': 'Kingston', 'Japan': 'Tokyo', 'Jordan': 'Amman', 'Kazakhstan': 'Astana', 'Kenya': 'Nairobi', 'Kiribati': 'Tarawa', 'Kosovo': 'Pristina', 'Kuwait': 'Kuwait City',
            'Kyrgyzstan': 'Bishek', 'Laos': 'Vientiane', 'Latvia': 'Riga', 'Lebanon': 'Beirut', 'Lesotho': 'Maseru', 'Liberia': 'Monrovia', 'Libya': 'Tripoli', 'Liechtenstein': 'Vaduz',
            'Lithuania': 'Vilnius', 'Luxembourg': 'Luxembourg', 'Macedonia': 'Skopje', 'Madagascar': 'Antananarivo', 'Malawi': 'Lilongwe', 'Malaysia': 'Kuala Lumpur', 'Maldives': 'Male',
            'Mali': 'Bamako', 'Malta': 'Valletta', 'Marshall Islands': 'Majuro', 'Mauritania': 'Nouakchott','Mauritius': 'Port Louis', 'Mexico': 'Mexico City', 'Micronesia': 'Palikir', 'Moldova': 'Chisinau', 'Monaco': 'Monaco',
            'Mongolia': 'Ulaanbaatar', 'Montenegro': 'Podgorica', 'Morocco': 'Rabat', 'Mozambique': 'Maputo', 'Myanmar (Burma)': 'Naypyidaw', 'Namibia': 'Windhoek', 'Nauru': 'Yaren District',
            'Nepal': 'Kathmandu', 'Netherlands': 'Amsterdam', 'New Zealand': 'Wellington', 'Nicaragua': 'Managua', 'Niger': 'Niamey', 'Nigeria': 'Abuja', 'North Korea': 'Pyongyang', 'Norway': 'Oslo',
            'Oman': 'Muscat', 'Pakistan': 'Islamabad', 'Palau': 'Ngerulmud', 'Palestine': 'Jerusalem', 'Panama': 'Panama City', 'Papua New Guinea': 'Port Moresby', 'Paraguay': 'Asuncion', 'Peru': 'Lima',
            'Phillipines': 'Manila', 'Poland': 'Warsaw', 'Portugal': 'Lisbon', 'Qatar': 'Doha', 'Romania': 'Bucharest', 'Russia': 'Moscow', 'Rwanda': 'Kigali', 'Saint Kitts and Nevis': 'Basseterre',
            'Saint Lucia': 'Castries', 'Saint Vincent and the Grenadines': 'Kingstown', 'Samoa': 'Apia', 'San Marino': 'San Marino', 'Sao Tome and Principe': 'Sao Tome', 'Saudi Arabia': 'Riyadh',
            'Senegal': 'Dakar', 'Serbia': 'Belgrade', 'Seychelles': 'Victoria', 'Sierra Leone': 'Freetown', 'Singapore': 'Singapore', 'Slovakia': 'Bratislava', 'Slovenia': 'Ljubljana',
            'Solomon Islands': 'Honiara', 'Somalia': 'Mogadishu', 'South Africa': 'Pretoria', 'South Korea': 'Seoul', 'South Sudan': 'Juba', 'Spain': 'Madrid', 'Sri Lanka': 'Sri Jayawardenepura Kotte',
            'Sudan': 'Khartoum', 'Suriname': 'Paramaribo', 'Swaziland': 'Mbabane', 'Sweden': 'Stockholm', 'Switzerland': 'Bern', 'Syria': 'Damascus', 'Taiwan': 'Taipei', 'Tajikistan': 'Dushanbe',
            'Tanzania': 'Dodoma', 'Thailand': 'Bangkok', 'Timor-Leste': 'Dili', 'Togo': 'Lome', 'Tonga': 'Nukualofa', 'Trinidad and Tobago': 'Port of Spain', 'Tunisia':'Tunis', 'Turkey': 'Ankara', 'Turkmenistan': 'Ashgabat', 'Tuvalu': 'Funafuti',
            'Uganda': 'Kampala', 'Ukraine': 'Kyiv', 'United Arab Emirates': 'Abu Dhabi', 'United Kingdom': 'London', 'United States of America': 'Washington, DC', 'Uruguay': 'Montevideo',
            'Uzbekistan': 'Tashkent', 'Vanuatu': 'Port Vila', 'Vatican City': 'Vatican Sea', 'Venezuela': 'Caracas', 'Vietnam': 'Hanoi', 'Yemen': 'Sana a', 'Zambia': 'Lusaka', 'Zimbabwe': 'Harare'}


# Generate 35 Quiz Files
for quizNum in range(35):
    # Create the quiz and answer key files
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w', encoding='utf-8')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w', encoding='utf-8')

    # Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'World Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    countries = list(capitals.keys())
    random.shuffle(countries)

# Loop through each country and make a question for each
    for questionNum in range(198):
        #Get the correct and incorrect answers
        correctAnswer = capitals[countries[questionNum]]
        incorrectAnswers = list(capitals.values())
        del incorrectAnswers[incorrectAnswers.index(correctAnswer)]
        incorrectAnswers = random.sample(incorrectAnswers, 3)
        answerOptions = incorrectAnswers + [correctAnswer]
        random.shuffle(answerOptions)

    # Write the question  and the answer options to the quiz file
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, countries[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Wrie the answer key to a file
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
    
    

