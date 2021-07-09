import pytest
import random
import session9
import os
import inspect
import re
from collections import namedtuple
from datetime import datetime
from random import random, uniform
from faker import Faker
from functools import reduce
from session9 import get_profiles, get_largest_blood_group, get_mean_current_location, get_mean_age, get_max_age
from session9 import get_profiles_dict, get_largest_blood_group_dict, get_mean_current_location_dict
from session9 import get_mean_age_dict, get_max_age_dict
from session9 import generate_company_data, compute_exchange_movement
from session9 import length_of_profile, length_of_profile_dict, size_of_exchange

fake = Faker()

README_CONTENT_CHECK_FOR = [
    'get_profiles',
    'get_largest_blood_group',
    'get_mean_current_location',
    'get_mean_age',
    'get_max_age',
    'get_profiles_dict',
    'get_largest_blood_group_dict',
    'get_mean_current_location_dict',
    'get_mean_age_dict',
    'get_max_age_dict',
    'generate_company_data',
    'compute_exchange_movement'
]

def test_session9_readme_exists():
    """
    Method checks if there is a README.md file. 
    failure_message: "README.md file missing!"  
    """
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session9_readme_500_words():
    """
    Method checks if there are atleast 500 words in the README.md file
    failures_message: Make your README.md file interesting! Add atleast 500 words
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_session9_readme_proper_description():
    """
    Method checks if all the functions are described in the README.md file
    failures_message: You have not described all the functions/classes well in your README.md file
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_session9_readme_file_for_more_than_10_hashes():
    """
    Method checks if README.md file has atleast 10 '#' (indentations)
    failures_message: You have not described all the functions/classes well in your README.md file 
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_session9_indentations():
    """
    Method checks for proper indentations \
    Returns pass if used four spaces for each level of syntactically significant indenting.
    failures_message_1: Your script contains misplaced indentations
    failures_message_2: Your code indentation does not follow PEP8 guidelines
    """
    lines = inspect.getsource(session9)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_session9_function_name_had_cap_letter():
    """
    Method checks for any Upper case in the function names in session9.py
    failures_message: You have used Capital letter(s) in your function names
    """
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

############################## Assignment Validations ###########################

profiles_tup = get_profiles(100)
profiles_dict = get_profiles_dict(100)

# Fake profile with namedtuple

def test_session9_get_profiles_length():
    """
    This method checks the length of the profile namedtuple generated
    failures_message: Mismatch in the length of the tuple expected
    """
    profile = get_profiles(10)
    assert len(profile) == 10, "Mismatch in the length of the tuple"

def test_session9_get_profiles_num():
    """
    This method checks the exception handling of the num argument
    failures_message: num has to be a non-zero positive integer
    """
    with pytest.raises(TypeError, match=r".*num has to be a non-zero positive integer*"):
        get_profiles('-21')
    with pytest.raises(TypeError, match=r".*num has to be a non-zero positive integer*"):
        get_profiles(1.5)
    with pytest.raises(TypeError, match=r".*num has to be a non-zero positive integer*"):
        get_profiles(5+8j)
    with pytest.raises(ValueError, match=r".*num has to be a non-zero positive integer*"):
        get_profiles(-21)

def test_session9_get_profiles():
    """
    This method checks type of the return value of get_profiles and the length of the profile tuple
    failures_message1: Store your profiles in a tuple
    failures_message2: Data Loss! You missed a few details of the profiles   
    """
    profiles = get_profiles(100)
    assert type(profiles) == tuple, "Store your profiles in a tuple!"
    assert set([len(profiles[x]) for x in range(100)]) == {13}, "Data Loss! You missed a few details of the profiles"

# Fake Profiles in dictionary

def test_session9_get_profiles_dict_length():
    """
    This method checks the length of the profile dictionary generated
    failures_message: Mismatch in the length of the dict
    """
    profile = get_profiles_dict(10)
    assert len(profile) == 10, "Mismatch in the length of the dict"

def test_session9_get_profiles_dict_num():
    """
    This method checks the exception handling of the num argument
    failures_message: num has to be a non-zero positive integer
    """
    with pytest.raises(TypeError, match=r".*num has to be a non-zero positive integer*"):
        get_profiles_dict('-21')
    with pytest.raises(TypeError, match=r".*num has to be a non-zero positive integer*"):
        get_profiles_dict(1.5)
    with pytest.raises(TypeError, match=r".*num has to be a non-zero positive integer*"):
        get_profiles_dict(5+8j)
    with pytest.raises(ValueError, match=r".*num has to be a non-zero positive integer*"):
        get_profiles_dict(-21)

def test_session9_get_profiles_dict():
    """
    This method checks type of the return value of get_profiles and the length of the profile tuple
    failures_message1: Store your profiles in a tuple
    failures_message2: Data Loss! You missed a few details of the profiles   
    """
    profiles = get_profiles_dict(100)
    assert type(profiles) == dict, "Store your profiles in a tuple!"
    assert set([len(profiles[x].keys()) for x in range(100)]) == {13}, "Data Loss! You missed a few details of the profiles"

# Comparing the performance of namedtuple and dictionary

def test_session9_time_it_get_max_age():
    """
    This method compares the time taken for computing the max age of the profiles stored in tuple and dict
    failures_message: Tuples are faster, backing the wrong horse here
    """
    *_, t_delta_tup = get_max_age(profiles_tup)
    *_, t_delta_dict = get_max_age_dict(profiles_dict)
    assert t_delta_tup <= t_delta_dict, "Tuples are faster, backing the wrong horse here"

def test_session9_time_it_get_mean_age():
    """
    This method compares the time taken for computing the mean age of the profiles stored in tuple and dict
    failures_message: Tuples are faster, backing the wrong horse here
    """
    mean_age_tup, t_delta_tup = get_mean_age(profiles_tup)
    mean_age_dict, t_delta_dict = get_mean_age_dict(profiles_dict)
    assert t_delta_tup <= t_delta_dict, "Tuples are faster, backing the wrong horse here"

def test_session9_time_it_get_largest_blood_group():
    """
    This method compares the time taken for computing the largest blood group in the profiles stored in tuple and dict
    failures_message: Tuples are faster, backing the wrong horse here
    """
    bg_tup, t_delta_tup = get_largest_blood_group(profiles_tup)
    bg_dict, t_delta_dict = get_largest_blood_group_dict(profiles_dict)
    assert t_delta_tup <= t_delta_dict, "Tuples are faster, backing the wrong horse here"

def test_session9_time_it_get_mean_current_location():
    """
    This method compares the time taken for computing the mean current location in the profiles stored in tuple and dict
    failures_message: Tuples are faster, backing the wrong horse here
    """
    bg_tup, t_delta_tup = get_mean_current_location(profiles_tup)
    bg_dict, t_delta_dict = get_mean_current_location_dict(profiles_dict)
    assert t_delta_tup <= t_delta_dict, "Tuples are faster, backing the wrong horse here"

# Stockmarket problem validations
stock_data = generate_company_data(100)

def test_session9_generate_company_data_num():
    """
    This method checks the exception handling of the num argument
    failures_message: num should be a non-zero integer
    """
    with pytest.raises(TypeError, match=r".*num should be a non-zero integer*"):
        generate_company_data('-21')
    with pytest.raises(TypeError, match=r".*num should be a non-zero integer*"):
        generate_company_data(1.5)
    with pytest.raises(TypeError, match=r".*num should be a non-zero integer*"):
        generate_company_data(5+8j)
    with pytest.raises(ValueError, match=r".*num should be a non-zero integer*"):
        generate_company_data(-21)

def test_session9_generate_company_data_length():
    """
    This method genrates 100 random company share data and checks its length
    failures_message: You did not generate enough data
    """
    exchange_data = generate_company_data(100)
    assert len(exchange_data) == 100, "You did not generate enough data"

def test_session9_generate_company_data_fields():
    """
    This method genrates 100 random company share data and checks the data field of the namedtuple
    failures_message: You did not generate all the fields related to company and stock price
    """
    exchange_data = generate_company_data(5)
    assert set([len(exchange_data[x]) for x in range(5)]) == {7}, "You did not generate all the fields related to company and stock price"

def test_session9_generate_company_data_open_close_low_high():
    """
    This method genrates 100 random company share data and checks the price open, close, high and low
    failures_message: Stock open price should be less than stock high
    failures_message: Stock close price should be greater than stock low
    failures_message: Stock open price should be less than stock high
    failures_message: Your weight index should add up to 1
    """
    assert all([stock_data[x].open <= stock_data[x].high for x in range(len(stock_data))]) == True, "Stock open price should be less than stock high"
    assert all([stock_data[x].close >= stock_data[x].low for x in range(len(stock_data))]) == True, "Stock close price should be greater than stock low"
    assert all([stock_data[x].high >= stock_data[x].low for x in range(len(stock_data))]) == True, "Stock high price should always be greater than stock low"
    assert round(sum([stock_data[x].wt for x in range(len(stock_data))])) == 1, "Your weight index should add up to 1"

def test_session9_compute_exchange_movement_arg():
    '''
    This method checks the exception handling of the argument passed to compute_exchange_movement function
    failures_message: Stock Exchange data is not a namedtuple
    '''
    with pytest.raises(TypeError, match=r".*Stock Exchange data is not a namedtuple*"):
        compute_exchange_movement([random.randint() for x in range(10)])

def test_session9_compute_exchange_movement_bullish():
    '''
    This method computes the stock exchnage movement
    failures_message: Its a Bullish index! Close higher
    failure_message: Its a Bullish index!!
    '''
    stock_price = namedtuple("stock","name, symbol, open, low, high, close, wt")
    random_list = [random() for x in range(10)]
    s = sum(random_list)
    random_wt = [x/s for x in random_list]

    Exchange = namedtuple("ListedCompanies","stock_price")
    BullishStockExchange = Exchange(stock_price(fake.company(), 'AMZN', 244, 240, 246, 245, random_wt.pop()))
    for i in range(9):
        name = fake.company()
        symbol = name[:4].upper()
        stock_open = round(uniform(10, 10_000),2)
        low = stock_open # Bullish - keeping low as open price
        high = round(uniform(stock_open, 1.1 * stock_open),2)
        close = round(uniform(stock_open, 1.1 * stock_open),2)
        if close > high:
            high = close
        company_data = stock_price(name, symbol, stock_open, low, high, close, random_wt.pop())
        BullishStockExchange += Exchange(company_data)
    world_index, indicator = compute_exchange_movement(BullishStockExchange)

    assert world_index.open < world_index.close, "Its a Bullish index! Close higher"
    assert indicator == 'Bullish', "Its a Bullish index!!"

def test_session9_compute_exchange_movement_bearish():
    '''
    This method computes the stock exchnage movement
    failures_message: Its a Bearish index! Open higher
    failure_message: Its a Bearish index!!
    '''
    stock_price = namedtuple("stock","name, symbol, open, low, high, close, wt")
    random_list = [random() for x in range(10)]
    s = sum(random_list)
    random_wt = [x/s for x in random_list]

    Exchange = namedtuple("ListedCompanies","stock_price")
    BearishStockExchange = Exchange(stock_price(fake.company(), 'AMZN', 244, 240, 246, 245, random_wt.pop()))
    for i in range(9):
        name = fake.company()
        symbol = name[:4].upper()
        stock_open = round(uniform(10, 10_000),2)
        low = round(uniform(0.9 * stock_open, stock_open),2)
        high = stock_open # Bearish - keeping high as open price
        close = round(uniform(0.9 * stock_open, stock_open),2)
        if close < low:
            low = close
        company_data = stock_price(name, symbol, stock_open, low, high, close, random_wt.pop())
        BearishStockExchange += Exchange(company_data)
    world_index, indicator = compute_exchange_movement(BearishStockExchange)

    assert world_index.open > world_index.close, "Its a Bearish index! Open higher"
    assert indicator == 'Bullish', "Its a Bearish index!!"