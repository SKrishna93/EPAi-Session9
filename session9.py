# Importing required Packages

from collections import namedtuple, Counter
from decimal import Decimal
import datetime
from functools import wraps
from time import perf_counter
from typing import Type
from random import random, uniform
from faker import Faker

fake = Faker()
length_of_profile = 0
length_of_profile_dict = 0
size_of_exchange = 0

# Timer deecorator

def timer(fn: "Function"):
    '''This is a timer decorator which takes the function as input and return a closure'''
    @wraps(fn)
    def inner(*args, **kwargs) -> "Function Output":
        '''
        Inner closure function to compute time taken for function execution
        '''
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        time_delta = (end - start)
        print('Run time: {0:.6f}s'.format(time_delta))
        return result, time_delta
    return inner

# Namedtuple profile creation
@timer
def get_profiles(num: int)-> "consolidate_profile":
    '''This method will generate 10_000 profiles using the Faker library
    and store them in a namedtuple profile. A collection of these profile is stored in nametuple profiles
    input - num - integer, number of profile to be generated
    return - consoliddate_profile - namedtuple with Collection of profiles created'''
    if not isinstance(num, int):
        raise TypeError("num has to be a non-zero positive integer")
    if not num > 0:
        raise ValueError("num has to be a non-zero positive integer")
    global length_of_profile
    profile = namedtuple('profile',fake.profile().keys())
    profiles = namedtuple('profiles','profile')

    prof = profile(**fake.profile())
    consolidate_profile = profiles(prof)
    for i in range(num - 1):
        prof = profile(**fake.profile())
        p = profiles(prof)
        consolidate_profile += p
    length_of_profile = len(consolidate_profile)
    return consolidate_profile

@timer
def get_largest_blood_group(consolidated_profiles: "namedtuple")->"largest blood group type and count":
    '''This method will give the largest blood group in the profiles and its count
    input - consolidated_profiles - namedtuple of the collection of tuples
    return - tuple of largest blood group and the count'''
    if not isinstance(consolidated_profiles, tuple):
        raise TypeError("Consolidated_profiles passed should be a tuple")
    tup = Counter(consolidated_profiles[x].blood_group for x in range(length_of_profile)).most_common()[0]
    return tup

@timer
def get_mean_current_location(consolidated_profiles: "namedtuple")->"mean current location":
    '''This method will compute the mean current location of the profiles
    input - consolidated_profiles - namedtuple of the collection of tuples
    return - tuple of mean of the current location'''
    if not isinstance(consolidated_profiles, tuple):
        raise TypeError("Consolidated_profiles passed should be a tuple")
    mean_x = sum([consolidated_profiles[x].current_location[0] for x in range(length_of_profile)])/length_of_profile
    mean_y = sum([consolidated_profiles[x].current_location[1] for x in range(length_of_profile)])/length_of_profile
    return mean_x, mean_y

@timer
def get_mean_age(consolidated_profiles: "namedtuple")->"mean current location":
    '''This method will compute the mean age of the profiles
    input - consolidated_profiles - namedtuple of the collection of tuples
    return - Mean age of the profiles'''
    if not isinstance(consolidated_profiles, tuple):
        raise TypeError("Consolidated_profiles passed should be a tuple")
    mean_age = round(sum([(int(str(datetime.date.today() - consolidated_profiles[x].birthdate).split()[0])/365) for x in range(length_of_profile)])/length_of_profile,2)
    return mean_age

@timer
def get_max_age(consolidated_profiles: "namedtuple")->"mean current location":
    '''This method will compute the oldest persons age in the profiles
    input - consolidated_profiles - namedtuple of the collection of tuples
    return - Max age'''
    if not isinstance(consolidated_profiles, tuple):
        raise TypeError("Consolidated_profiles passed should be a tuple")
    #i = [str(consolidated_profiles[x].birthdate) for x in range(length_of_profile)].index(min(str(consolidated_profiles[x].birthdate) for x in range(length_of_profile)))
    #prof = consolidated_profiles[i]
    #max_age = int(max([int(str(datetime.date.today() - consolidated_profiles[x].birthdate).split()[0]) for x in range(length_of_profile)])/365)
    max_age = round(int(str(datetime.date.today() - min([consolidated_profiles[x].birthdate for x in range(length_of_profile)])).split()[0])/365,2)
    return max_age

# Same operations using Dict
@timer
def get_profiles_dict(num: int)-> "consolidate_profile":
    '''This method will generate 10_000 profiles using the Faker library
    and store them in a dictionary.
    input - num - integer, number of profile to be generated
    return - consolidate_profile_dict - dictionary with the collection of profiles created'''
    if not isinstance(num, int):
        raise TypeError("num should be an non-zero integer")
    if not num > 0:
        raise TypeError("num should be an non-zero integer")
    global length_of_profile_dict
    consolidate_profile_dict = {}
    for i in range(num):
        consolidate_profile_dict[i] = fake.profile()
    length_of_profile_dict = len(consolidate_profile_dict)
    return consolidate_profile_dict

@timer
def get_largest_blood_group_dict(consolidated_profiles_dict: dict)->"largest blood group type and count":
    '''This method will give the largest blood group in the profiles and its count
    input - consolidated_profiles_dict - Dictionary collection of fake profiles
    return - tuple of largest blood group, the count and time taken to execute the code'''
    if not isinstance(consolidated_profiles_dict, dict):
        raise TypeError("Consolidated_profiles_dict passed should be a dictionary")
    values_per_key = []
    for i in range(length_of_profile_dict):
        d = consolidated_profiles_dict[i].items()
        for k, v in d:
            if k == 'blood_group':
                values_per_key.append(v)
    tup = Counter(values_per_key).most_common()[0]
    return tup

@timer
def get_mean_current_location_dict(consolidated_profiles_dict: dict)->"mean current location":
    '''This method will compute the mean current location of the profiles
    input - consolidated_profiles_dict - Dictionary collection of fake profiles
    return - tuple of mean of the current location'''
    if not isinstance(consolidated_profiles_dict, dict):
        raise TypeError("Consolidated_profiles_dict passed should be a dictionary")    
    values_per_key = []
    for i in range(length_of_profile_dict):
        d = consolidated_profiles_dict[i].items()
        for k, v in d:
            if k == 'current_location':
                values_per_key.append(v)
    mean_x = sum([values_per_key[x][0] for x in range(length_of_profile_dict)])/length_of_profile_dict
    mean_y = sum([values_per_key[x][1] for x in range(length_of_profile_dict)])/length_of_profile_dict
    return mean_x, mean_y

@timer
def get_mean_age_dict(consolidated_profiles_dict: dict)->"mean age":
    '''This method will compute the mean age of the profiles
    input - consolidated_profiles_dict - Dictionary collection of fake profiles
    return - Mean age of the profiles'''
    if not isinstance(consolidated_profiles_dict, dict):
        raise TypeError("Consolidated_profiles_dict passed should be a dictionary")
    values_per_key = []
    for i in range(length_of_profile_dict):
        d = consolidated_profiles_dict[i].items()
        for k, v in d:
            if k == 'birthdate':
                values_per_key.append(v)
    mean_age = sum([(int(str(datetime.date.today() - values_per_key[x]).split()[0])/365) for x in range(length_of_profile_dict)])/length_of_profile_dict
    return round(mean_age,2)

@timer
def get_max_age_dict(consolidated_profiles_dict: "dict")->"max age":
    '''This method will compute the Max age of the profiles
    input - consolidated_profiles_dict - Dictionary collection of fake profiles
    return - Max age of the profiles'''
    if not isinstance(consolidated_profiles_dict, dict):
        raise TypeError("Consolidated_profiles_dict passed should be a dictionary")    
    values_per_key = []
    for i in range(length_of_profile_dict):
        d = consolidated_profiles_dict[i].items()
        for k, v in d:
            if k == 'birthdate':
                values_per_key.append(v)
    max_age = round(int(str(datetime.date.today() - min(values_per_key)).split()[0])/365,2)
    #max_age = max([(int(str(datetime.date.today() - values_per_key[x]).split()[0])/365) for x in range(length_of_profile_dict)])
    return max_age

# Stockmarket problem

def generate_company_data(num: int)->"namedtuple with company and stock price":
    '''This menthod generates a namedtuple with stock price data of 'num' companies in a stock exchange
    input - num - non-zero integer
    return - namedtuple - containing the stock price of 'num' companies'''
    if not isinstance(num, int):
        raise TypeError("num should be a non-zero integer")
    if not num > 0:
        raise ValueError("num should be a non-zero integer")
    #global size_of_exchange
    stock_price = namedtuple("stock","name, symbol, open, low, high, close, wt")
    random_list = [random() for x in range(num)]
    s = sum(random_list)
    random_wt = [x/s for x in random_list]

    Exchange = namedtuple("ListedCompanies","stock_price")
    RocketStockExchange = Exchange(stock_price(fake.company(), 'AMZN', 244, 240, 246, 245, random_wt.pop()))
    for i in range(num - 1):
        name = fake.company()
        symbol = name[:4].upper()
        stock_open = round(uniform(10, 10_000),2)
        low = round(uniform(0.9 * stock_open, stock_open),2)
        high = round(uniform(stock_open, 1.1 * stock_open),2)
        close = round(uniform(low, high),2)
        company_data = stock_price(name, symbol, stock_open, low, high, close, random_wt.pop())
        RocketStockExchange += Exchange(company_data)
    #size_of_exchange = len(RocketStockExchange)
    return RocketStockExchange

def compute_exchange_movement(stock_exchange: "namedtuple")->"index_data and 'Bullish' or 'Bearish'":
    '''This method computes the open, close, low and high movement of the stock index and
    retuns 'Bullish' if close more than open or 'Bearish' if close less than open
    input - stock_exchange - namedtuple data of stock price data of listed companies
    return - index_data 'Bullish' or 'Bearish' depending on the index positive or negative'''
    if not isinstance(stock_exchange, tuple):
        raise TypeError("Stock Exchange data is not a namedtuple")
    size_of_exchange = len(stock_exchange)
    if not all([True if str(type(stock_exchange[x])).split('.')[1][:5] == 'stock' else False for x in range(size_of_exchange)]):
        raise ValueError("Stock Exchange data is not a namedtuple of type stock")
    ind = namedtuple("index", "exchange_open exchange_close exchange_low exchange_high")
    exchange_open = round(sum([stock_exchange[x].open * stock_exchange[x].wt for x in range(size_of_exchange)]),2)
    exchange_close = round(sum([stock_exchange[x].close * stock_exchange[x].wt for x in range(size_of_exchange)]),2)
    exchange_low = round(sum([stock_exchange[x].low * stock_exchange[x].wt for x in range(size_of_exchange)]),2)
    exchange_high = round(sum([stock_exchange[x].high * stock_exchange[x].wt for x in range(size_of_exchange)]),2)

    World_Index = ind(exchange_open, exchange_close, exchange_low, exchange_high)

    if exchange_close - exchange_open >= 0:
        return World_Index, 'Bullish'
    else:
        return World_Index, 'Bearish'