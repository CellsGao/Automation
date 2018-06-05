# P94 5.6.2
# 重点，setdefault语句，查找字典中有无对应键，有的话返回对应值，无的话返回设定的默认值。
import pprint
inventory = {'rope': 12, 'torch': 1, 'gold': 10, 'dagger': 1, 'arrow': 12}
new_items = ['gold', 'gold', 'ruby', 'dagger']


def add_item(inv, items):
    # 将列表转化为"物品：数量"的字典
    new_inventory = {}
    for item in items:
        new_inventory.setdefault(item, 0)
        new_inventory[item] += 1
    for item in new_inventory:
        inventory.setdefault(item, 0)
        inventory[item] += new_inventory[item]
    pprint.pprint(inventory)


def main():
    add_item(inventory, new_items)


if __name__ == '__main__':
    main()
