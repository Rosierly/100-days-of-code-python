# Day 31 - Flash Card App
A language-learning flashcard application that displays random vocabulary cards, automatically reveals translations, and saves learning progress between sessions using CSV files.


### Packages used (only for NATO Alphabet Converter):
- pandas → data manipulation and analysis library for working with structured (tabular) data using DataFrames

## Notes

### Getting a Key from a Dictionary in Python `(next(iter())` vs `keys())`
###### When working with dictionaries, you may need to access a key directly without using a for loop.
`keys()`
```python
random_pair = {"bonjour": "hello", "merci": "thank you"}

print(random_pair.keys())  # output: dict_keys(['bonjour', 'merci'])

first_key = random_pair.keys()[0]  # ❌ TypeError: 'dict_keys' object is not subscriptable
# This tries to do indexing ([0]) on a dict_keys object, But dict_keys does NOT support indexing.


# Convert to list before indexing
random_pair = {"bonjour": "hello", "merci": "thank you"}

first_key = list(random_pair.keys())[0]  # convert to a list to avoid getting an error
print(first_key)
```
`(next(iter())`
```python
random_pair = {"bonjour": "hello", "merci": "thank you"}

first_key = next(iter(random_pair))
print(first_key)

# Creates an iterator over the keys -> it behaves like a “cursor” that goes through
it = iter(random_pair)

# Gets keys
print(next(it))  # first key
print(next(it))  # second key
```
***

### Using `.items()` in Python Dictionaries
###### The .items() method is used to get both keys and values from a dictionary at the same time. It is especially useful when you need to work with paired data.
```python
random_pair = {"bonjour": "hello", "merci": "thank you"}
print(random_pair.items())
# Output:
# dict_items([('bonjour', 'hello'), ('merci', 'thank you')])
# Each element is a tuple containing: (key, value)
```
#### Summary  
`.keys()` → only keys  
`.values()` → only values  
`.items()` → both key and value together (as tuples)
***

### References:
- *[Pandas DataFrame to dict Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html)*
- *[Wiktionary: Frequency lists](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists)*
- *[2018 Frequency Lists from Hermit Dave](https://github.com/hermitdave/FrequencyWords/tree/master/content/2018)*
- *[Google Translate for Google Sheets](https://support.google.com/docs/answer/3093331?hl=en-GB)*
- *[Google Translate Language Codes](https://docs.cloud.google.com/translate/docs/languages?hl=en)*
***
