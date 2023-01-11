import random

destination_list = ['Georgia', 'Utah', 'California', 'Nevada']
restaurants_list = ['Bacoa Finca + Fogon','Cafe Mutton',"Smoke'N Ash BBQ", 'San Ho Won']
transport_means_list = ['car','plane','train']
entertainment_list = ['Club/Bar','Cinema/Theater','Museum/Tour Bus','Hiking/Mountain Climbing']

def demop1(list):
    random_destination = random.choice(list)
    return random_destination

def demop2(list):
    random_restaurant = random.choice(list)
    return random_restaurant

def demop3(list):
    transport = random.choice(list)
    return transport

def demop4(list):
    entertainment = random.choice(list)
    return entertainment

def master_function():
    print("Welcome to random trip generator")
    print('Here is your complete list of your randomly generated day trip')
    result = demop1(destination_list)
    result_1 = demop2(restaurants_list)
    result_2 = demop3(transport_means_list)
    result_3 = demop4(entertainment_list)
    print(f'Destination: {result}')
    print(f'Restaurant: {result_1}')
    print(f'Transport: {result_2}')
    print(f'Entertainment: {result_3}')
master_function()

def satisfaction():
    satisfied = input('Are all these aspects of the day trip satisfactory? (yes/no): ')
    if satisfied == 'yes':
        print('Random day trip complete.')
    elif satisfied == 'no':
        choice = input('Which aspect or the day trip were you dissatisfied with?: ')
        if choice == 'destination' or 'Destination':
            user_picked = False
            while user_picked == False:
                new_destination = demop1(destination_list)
                print(f'New destination selected: {new_destination}')
                confirmation = input(f'Are you satisfied with {new_destination} as your new destination?(yes/no): ')
                if confirmation == 'yes':
                    print(master_function())
                    satisfactory_question = satisfaction()
                    print(satisfactory_question)
                elif confirmation == 'no':
                    print('Reselecting destination')
                else:
                    print('Type (yes/no)')
        elif choice == 'restaurant' or 'Restaurant':
            user_picked_1 = False
            while user_picked_1 == False:
                new_restaurant = demop2(restaurants_list)
                print(f'New restaurant selected: {new_restaurant}')
                confirmation_1 = input(f'Are you satisfied with {new_restaurant} as your new restaurant?(yes/no): ')
                if confirmation_1 == 'yes':
                    print(master_function())
                    satisfactory_question = satisfaction()
                    print(satisfactory_question)
                elif confirmation_1 == 'no':
                    print('Reselecting restaurant')
                else:
                    print('Type (yes/no)')
        elif choice == 'transport' or 'Transport':
            user_picked_2 = False
            while user_picked_2 == False:
                new_transport = demop3(transport_means_list)
                print(f'New means of transport selected: {new_transport}')
                confirmation_2 = input(f'Are you satisfied with {new_transport} as your new means of transport?(yes/no): ')
                if confirmation_2 == 'yes':
                    print(master_function())
                    satisfactory_question = satisfaction()
                    print(satisfactory_question)
                elif confirmation_2 == 'no':
                    print('Reselecting means of transport')
                else:
                    print('Type (yes/no)')
        elif choice == 'entertainment' or 'Entertainment':
            user_picked_3 = False
            while user_picked_3 == False:
                new_entertainment = demop4(entertainment_list)
                print(f'New entertainment selected: {new_destination}')
                confirmation_3 = input(f'Are you satisfied with {new_entertainment} as your new form of entertainment?(yes/no): ')
                if confirmation_3 == 'yes':
                    print(master_function())
                    satisfactory_question = satisfaction()
                    print(satisfactory_question)
                elif confirmation_3 == 'no':
                    print('Reselecting new form of entertainment')
                else:
                    print('Type (yes/no)')
        else:
            print('Please select a day trip aspect that you would like to change.')