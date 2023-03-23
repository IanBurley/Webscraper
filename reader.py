with open('output.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        if line.startswith('At time :'):
            print(line)
        elif line.startswith('{'):
            coin_data = eval(line)
            print(coin_data['Symbol'], coin_data['Price (Intraday)'], coin_data['Change'], coin_data['% Change'])
        else:
            continue
        print('')
