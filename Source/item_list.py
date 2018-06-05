# P93 5.6.1

inventory = {'rope': 12, 'torch': 1, 'gold': 10, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print('inventory')
    number = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        number += v
    print('total number items ' + str(number))


def main():
    display_inventory(inventory)

if __name__ == '__main__':
    main()
