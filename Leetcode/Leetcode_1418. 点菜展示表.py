# 1418. 点菜展示表
# 给你一个数组 orders，表示客户在餐厅中完成的订单，确切地说， orders[i]=[customerNamei,tableNumberi,foodItemi] ，
# 其中 customerNamei 是客户的姓名，tableNumberi 是客户所在餐桌的桌号，而 foodItemi 是客户点的餐品名称。
# 请你返回该餐厅的 点菜展示表 。在这张表中，表中第一行为标题，其第一列为餐桌桌号 “Table” ，后面每一列都是按字母顺序排列的餐品名称。
# 接下来每一行中的项则表示每张餐桌订购的相应餐品数量，第一列应当填对应的桌号，后面依次填写下单的餐品数量。
# 注意：客户姓名不是点菜展示表的一部分。此外，表中的数据行应该按餐桌桌号升序排列。
def displayTable(orders: [[str]]) -> [[str]]:
    foodItem = set()
    tableDict = {}
    for order in orders:
        if order[1] not in tableDict:
            tableDict[order[1]] = {order[2]: 1}
        else:
            tableDict[order[1]][order[2]] = tableDict[order[1]].setdefault(order[2], 0) + 1
        if order[2] not in foodItem:
            foodItem.add(order[2])
    result = [['Table']]
    foodItem = list(foodItem)
    foodItem.sort()
    result[0].extend(foodItem)
    tables = list(tableDict.keys())
    tables.sort(key=lambda x: int(x))
    for table in tables:
        result.append([str(table)])
        for food in foodItem:
            result[-1].append(str(tableDict[table].setdefault(food, 0)))
    return result


orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
displayTable(orders)


