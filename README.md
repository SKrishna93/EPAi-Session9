# Session 9 Assignment of EPAi3.0

## namedtuples

### Question - 1

### Objective: Use the Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age

__timer (fn: "Function")__ :
+ This a decorator function which encloses the closure function inner
+ The method takes 1 positional argument _'fn'_
+ fn: Function which needs to be passed to the inner function
+ return: Inner function
+ __Algorithm__: The timer function returns the inner function and decorate the any function passed to it

__get_profiles (num: "int")__ :
+ This method generates *'num'* random user profiles from the faker library.
+ We use the namedtuples to store these profiles internally 
+ The method takes 1 positional argument _'num'_ integer type
+ return: consolidate_profile
+ __Algorithm__: We first create namedtuple with field names set based on fake.profile() output. We store the individual profiles in this namedtuple. A collection of these tuples are stored in the consolidate_profile named tuple which takes namedtuple profile as field

__get_largest_blood_group (consolidated_profiles: "namedtuple")__ :
+ This method will give the largest blood group in the profiles and its count
+ input - consolidated_profiles - namedtuple of the collection of tuples
+ return - tuple of largest blood group and the count
+ __Algorithm__: The profiles stored as namedtuple is passed to the method. The attribute 'blood_group' is accessed by iterating over the inner tuples and using '.' (dot) operator in the inner named tuple. Counter function is used to find the largest blood group

__get_mean_current_location (consolidated_profiles: "namedtuple")__ :
+ This method will compute the mean current location of the profiles
+ input - consolidated_profiles - namedtuple of the collection of tuples
+ return - tuple of mean of the current location
+ __Algorithm__: The profiles stored as namedtuple is passed to the method. The attribute 'current_location' is accessed by iterating over the inner tuples and using '.' (dot) operator in the inner named tuple. sum() of the corresponding x and y coordinate is computed and divided by the count of entries 

__get_mean_age (consolidated_profiles: "namedtuple")__ :
+ This method will compute the mean age of the profiles
+ input - consolidated_profiles - namedtuple of the collection of tuples
+ return - Mean age of the profiles
+ __Algorithm__: The profiles stored as namedtuple is passed to the method. The attribute 'birthdate' is accessed by iterating over the inner tuples and using '.' (dot) operator in the inner named tuple. datetime.date() method is used to compute the age (by dividing 365). The mean of all the age computed is returned.

__get_max_age (consolidated_profiles: "namedtuple")__ :
+ This method will compute the oldest persons age in the profiles
+ input - consolidated_profiles - namedtuple of the collection of tuples
+ return - max_age of the profiles
+ __Algorithm__: The profiles stored as namedtuple is passed to the method. The attribute 'birthdate' is accessed by iterating over the inner tuples and using '.' (dot) operator in the inner named tuple. The min() is used to compute the max of all the birthdate. datetime.date() method is used to compute the age (by dividing 365). 

### Question - 2

### Objective: Use the Faker library to get 10000 random profiles. Using dictionary, calculate the largest blood type, mean-current_location, oldest_person_age, and average age

__get_profiles_dict (num: "int")__ :
+ This method generates *'num'* random user profiles from the faker library.
+ We use the dictionaries to store these profiles internally 
+ The method takes 1 positional argument _'num'_ integer type
+ return: consolidate_profile_dict
+ __Algorithm__: We first create dictionary with keys set based on fake.profile() output. We store the individual profiles in this dictionary. A collection of these dictionaries are stored in the consolidate_profile_dict. With keys indexed based on the number of profiles generated

__get_largest_blood_group_dict (consolidated_profiles_dict: "dict")__ :
+ This method will give the largest blood group in the profiles and its count
+ input - consolidated_profiles_dict - Dictionary collection of fake profiles
+ return - dictionary of largest blood group, the count
+ __Algorithm__: The profiles stored as dictionary is passed to the method. The value stored in key 'blood_group' is accessed by iterating over the inner dictionary. Counter function is used to find the largest blood group

__get_mean_current_location_dict (consolidated_profiles_dict: "dict")__ :
+ This method will compute the mean current location of the profiles
+ input - consolidated_profiles_dict - Dictionary collection of fake profiles
+ return - tuple of mean of the current location
+ __Algorithm__: The profiles stored as dictionary is passed to the method. The value stored in key 'current_location' is accessed by iterating over the inner dictionary. The mean value of the x and y coordinate is calculated.

__get_mean_age_dict (consolidated_profiles_dict: "dict")__ :
+ This method will compute the mean age of the profiles
+ input - consolidated_profiles_dict - Dictionary collection of fake profiles
+ return - Mean age of the profiles
+ __Algorithm__: The profiles stored as dictionary is passed to the method. The value stored in key 'birthdate' is accessed by iterating over the inner dictionary. datetime.date() method is used to compute the age (by dividing 365). The mean of all the age computed is returned.

__get_max_age_dict (consolidated_profiles_dict: "dict")__ :
+ This method will compute the Max age of the profiles
+ input - consolidated_profiles_dict - Dictionary collection of fake profiles
+ return - Max age of the profiles
+ __Algorithm__: The profiles stored as dictionary is passed to the method. The value stored in key 'birthdate' is accessed by iterating over the inner dictionary. The max of all the age computed is computed by using min on birthdate value.  datetime.date() method is used to compute the age (by dividing 365).

### Question - 3

### Objective: Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day, and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple.

__generate_company_data (num: int)__ :
+ This menthod generates a namedtuple with stock price data of 'num' companies in a stock exchange
+ input - num - non-zero integer
+ return - namedtuple - containing the stock price of 'num' companies
+ __Algorithm__: The fake.company() is used to generate random company names and the first 4 letters in uppercase are stored as 'symbol', which along with randomly generated stock price with 'open', 'close', 'low' and 'high' using the random.uniform() method.
+ The open price is randomly generated between 10 and 10_000.
+ The low price is allowed to take values maximum 10% below open (lower circuit).
+ The high price is allowed to take values maximum 10% above open (upper circuit).
+ The closing is allowed to fluctuate between lower and higher prices.
+ The weight to the stock is randonly assigned such that the sum of the weights of all the stock is ~1
+ The individual stock_price data is stored in a namedtuple.
+ The collection of all the company's stock listed are stored as a namedtuple to give the exchange_data

__compute_exchange_movement (stock_exchange: "namedtuple")__ :
+ This method computes the open, close, low and high movement of the stock index and
+ retuns 'Bullish' if close more than open or 'Bearish' if close less than open
+ input - stock_exchange - namedtuple data of stock price data of listed companies
+ return - index_data 'Bullish' or 'Bearish' depending on the index positive or negative
+ __Algorithm__: The inner namedtuple is accessed and the open, close, low and high data for all the compamy's listed are computed. Along, with the weights assigned to each of the stock, the overall exchange's open, close, low and high is computed.
+ Based on the index's open and close price movement. The indicator 'Bullish' or 'Bearish' is returned.