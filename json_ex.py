# load json library and write functions
import json

def check_char_count(mystr):
    # assert statement only passes if mystr is a str type
    assert insinstance(mystr, str)
    
    if ( len(mystr) == 2 ):
        return( f'{mystr} count passes' )
    else:
        return( f'{mystr} count FAILS' )

def check_char_type(mystr):
    if ( mystr.isupper() and mystr.isalpha() ):
        return( f'{mystr} type passes' )
    else:
        return( f'{mystr} type FAILS' )

def check_char_match(str1, str2):
    if ( str1[0] == str2[0] ):
        return( f'{str1} match passes' )
    else:
        return( f'{str1} match FAILS' )

def main(): 

    with open('states.json', 'r') as f:
        states = json.load(f)


    for i in range(50):
        print(check_char_count( states['states'][i]['abbreviation'] ))
        print(check_char_type( states['states'][i]['abbreviation'] ))
        print(check_char_match( states['states'][i]['abbreviation'], states['states'][i]['name'] ))


if __name__ == '__main__':
    main()

# json library looks throught the json file itslef and read it in, not as a str

