def make_shirt(size='Large', text='I love python.'):
    print(f'Size:\t{size}\nText:\t{text}')

make_shirt('Medium')
make_shirt(text="you're a small boi", size='Tiny')

def describe_city(city, country='default'):
    print(f'{city} is in {country}')

describe_city('Dan')
describe_city('JHB', 'SA')