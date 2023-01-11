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