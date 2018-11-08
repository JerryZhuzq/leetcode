from copy import deepcopy

def sort_goods(Goods):
    Goods.sort(key=lambda x:x[2]/x[1], reverse=True)
    return Goods

def addto_bags(Goods,bags):
    for i in bags:
        for j in goods:
            if  j[1]<=i[1] and j[3] == 0:
                i[1] = i[1] - j[1]
                j[3] = i[0]
                i[2] += j[2]
            else:
                continue
    Goods.sort(key=lambda x:x[0])
    return Goods,bags

def addoneto_bags(good,bag):
    good[3] = bag[0]
    bag[1] -= good[1]
    bag[2] += good[2]
    return good,bag

def removefrom_bags(good,bag):
    good[3] = 0
    bag[1] += good[1]
    bag[2] -= good[2]
    return good,bag

def sum_value(bags):
    value = 0
    for i in bags:
        value += i[2]
    return value



def neighbor_search(goods,bags):
    better_result = []
    empty_goods = []
    store_bag = []
    for i in goods:
        store_bag.append([i[0],i[3]])
        if i[3] == 0:
            empty_goods.append(i)
    print("Current position of goods: %s.  Value: %d ([#number of goods,#number of knapsack])" % (store_bag,sum_value(bags)))
    for i in goods:
        bag_num = i[3]
        for j in bags :
            x = goods.index(i)
            y = bags.index(j)
            if bag_num == 0 and i[1] <= j[1]:    #若在背包外的货物能放入其中一个背包，将该结果计入邻域
                addoneto_bags(i,j)
                temp1_goods,temp1_bags = deepcopy(goods),deepcopy(bags)
                better_result.append([temp1_goods,temp1_bags,sum_value(bags)])
                print("add goods %s into bag %d." %(i[0],j[0]))
                removefrom_bags(i,j)
                break
            elif bag_num == 0 and i[1] > j[1]:
                store_bag[x][1],temp = bags[y][0],store_bag[x][1]
                print("-----------------Neighbor: %s.  This situation is out ot weight!" % (store_bag))
                store_bag[x][1] = temp
            elif bag_num != 0 and bag_num != j[0]:          #若该货物在背包中
                removefrom_bags(i,bags[bag_num-1])
                print("remove goods %s from bag %d." % (i[0],bag_num))
                store_bag[x][1], temp = bags[y][0], store_bag[x][1]
                print("-----------------Neighbor: %s.  Value: %d" % (store_bag,sum_value(bags)))
                store_bag[x][1] = temp
                for k in empty_goods:
                    if k[1] <= bags[bag_num-1][1] and k[2] > i[2]:  #判断将该货物从背包中拿出后，未放在背包中的货物是否能加入该背包并且value增加
                        if i[1] <= j[1]:
                            addoneto_bags(i, j)
                            addoneto_bags(k, bags[bag_num-1])
                            print("add goods %s into bag %d and add goods %f into bag %g." %(i[0],j[0],k[0],bags[bag_num-1][0]))
                            temp2_goods,temp2_bags = deepcopy(goods),deepcopy(bags)
                            better_result.append([temp2_goods, temp2_bags, sum_value(bags)])
                            removefrom_bags(k, bags[bag_num-1])
                            removefrom_bags(i, j)
                        else:
                            addoneto_bags(k, bags[bag_num-1])
                            print("add goods %s into bag %d." %(k[0],bags[bag_num-1][0]))
                            temp3_goods, temp3_bags = deepcopy(goods), deepcopy(bags)
                            better_result.append([temp3_goods, temp3_bags, sum_value(bags)])
                            removefrom_bags(k, bags[bag_num-1])
                addoneto_bags(i,bags[bag_num-1])
    better_result.sort(key=lambda x:x[2], reverse=True)
    if better_result:
        best_result = better_result[0]
        cur_goods, cur_bags, cur_value = best_result[0:3]
        return cur_goods, cur_bags, cur_value
    else:
        print("Current situation is the best solution!")
        return 0
    # neighbor_search(better_result[0],better_result[1])




def main(goods, bags):
    print("There are %s goods and %d knapsacks." % (len(goods), len(bags)))
    for i in goods:
        print("No.%s goods weight: %d value: %s" % (i[0], i[1], i[2]))
    goods = sort_goods(goods)
    result_goods,result_bags = addto_bags(goods,bags)
    neighbor_search(result_goods, result_bags)





goods=[[1,8,5,0],[2,6,10,0],[3,7,7,0],[4,10,21,0],[5,12,18,0],[6,2,6,0],[7,1,4,0],[8,10,12,0],[9,9,15,0],[10,4,10,0]] #[goods number, weight, value, which bag to add]
bags = [[1,25,0],[2,30,0]]                   #[bags number, weight, value]
main(goods,bags)