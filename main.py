import random
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from operator import indexOf


class RandomPolygons:

    # This Function is used to Binary code the coordinates
    def Binary_Encode(x):
        encode = []
        encode1 = []
        encode = format(x[0], '08b')
        encode1.append(encode)
        encode1.append(format(x[1], '08b'))
        return encode1

    # This Function is used to make the Random Chromosomes
    def randomizing_chromosomes(size):
        Object = RandomPolygons;
        x = []
        y = []
        for _ in range(size):
            x = [random.randint(1, 255) for _ in range(2)]
            y.append(Object.Binary_Encode(x))
        return y

        # Convert Binary to decimal

    def Binary_to_integer(binary):
        number = 0
        for b in binary:
            number = (2 * number) + b
        return number

    def Finding_Cross_Product(x):
        listx_1 = (x[1][0] - x[0][0])
        listy_1 = (x[1][1] - x[0][1])
        listx_2 = (x[2][0] - x[0][0])
        listy_2 = (x[2][1] - x[0][1])
        return (listx_1 * listy_2 - listy_1 * listx_2)

    # Finding the Angle using the Axis
    def Find_Angle(points):
        Object = RandomPolygons;
        N = len(points)
        previous = 0
        current = 0
        for i in range(N):
            temp = [points[i], points[(i + 1) % N],
                    points[(i + 2) % N]]
            current = Object.Finding_Cross_Product(temp)
            if (current != 0):
                if (current * previous < 0):
                    return False
                else:
                    previous = current
        return True

    # Finding the Interection of Polygon
    def Intersection_Polygon(coordinate1, coordinate2):
        i1 = [min(coordinate1[0][0], coordinate1[1][0]), max(coordinate1[0][0], coordinate1[1][0])]
        i2 = [min(coordinate2[0][0], coordinate2[1][0]), max(coordinate2[0][0], coordinate2[1][0])]
        ia = [max(i1[0], i2[0]), min(i1[1], i2[1])]
        slope1 = 0;
        slope2 = 0
        if max(coordinate1[0][0], coordinate1[1][0]) < min(coordinate2[0][0], coordinate2[1][0]):
            return False
        if (coordinate1[1][0] - coordinate1[0][0]) != 0:
            # Finding the Slope1
            slope1 = (coordinate1[1][1] - coordinate1[0][1]) * 1. / (coordinate1[1][0] - coordinate1[0][0]) * 1.
        if (coordinate2[1][0] - coordinate2[0][0]) != 0:
            # Finding the Slope2
            slope2 = (coordinate2[1][1] - coordinate2[0][1]) * 1. / (coordinate2[1][0] - coordinate2[0][0]) * 1.
        # Checking if the slopes are Equal then Return False(No Intersection)
        if slope1 == slope2:
            return False
        b1 = coordinate1[0][1] - slope1 * coordinate1[0][0]
        b2 = coordinate2[0][1] - slope2 * coordinate2[0][0]
        x1 = (b2 - b1) / (slope1 - slope2)
        if (x1 < max(i1[0], i2[0])) or (x1 > min(i1[1], i2[1])):
            return False
        return True

    # Fitness Function to check the intersection, angles and ratio of the Polygons
    def Fitness_Function(x, num, bool_var):
        list0 = []
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        s = []
        res = []
        idx = 0
        Object = RandomPolygons;
        temp_list = []
        for i in range(num):
            temp_list.append(2)
        if (bool_var == 0):
            for y in range(len(x)):
                list0 = x[y]
                list2.clear()
                for i in range(len(list0)):
                    list1 = int(list0[i], 2)
                    list2.append(list1)
                list3.extend(list2)
            for var_len in temp_list:
                res.append(list3[idx: idx + var_len])
                idx += var_len
        elif (bool_var == 1):
            res = x

            # Checking the intersection of the Points
        temp_list1 = [2, 2]
        check = True
        for y in range(num):
            list4 = res[y]
            list6.clear()
            for i in range(len(list4)):
                list5 = list4[i]
                list6.append(list5)
            s = tuple(list6)
            list7.append(s)
        coordinate1 = []
        # Generating all possible combinations
        for i in range(num):
            var = i + 1
            if var == num:
                var = 0
            for j in range(var, var + 1):
                coordinate1.append(list7[i])
                coordinate1.append(list7[j])
        res1 = []
        idx1 = 0
        check = 0
        MaXx_Fitness = num
        cost = num * num - num
        for var_len in temp_list:
            res1.append(coordinate1[idx1: idx1 + var_len])
            idx1 += var_len
        coordinate2 = []
        i = 0
        for i in range(num):
            for j in range(num):
                if i != j:
                    coordinate2.append(res1[i])
                    coordinate2.append(res1[j])
                    if (Object.Intersection_Polygon(res1[i], res1[j]) == True):
                        check = 1
                        cost -= 1
        if check == 0:
            # Checking the Convex Angles
            Object.Find_Angle(res)
            # printing the graphs
            if Object.Find_Angle(res):
                Object.Plot_Polygons(res)
                cost += round((random.uniform(0.5, 1)), 5)
        elif check == 1:
            cost += round((random.uniform(0, 0.5)), 5)

        return res, cost

    # This Function is used to make the draw Chromosomes
    def Plot_Polygons(x):
        coord = x
        coord.append(coord[0])
        xs, ys = zip(*coord)
        plt.figure()
        plt.plot(xs, ys)
        plt.show()

    # This is our Selection Function
    def Selection_Wheel(Best_Fifty):
        print("By Selection Wheel Our Best Popuation is ::\n\n")
        sorted_dict = {}
        sorted_keys = sorted(Best_Fifty, key=Best_Fifty.get)
        count = 0
        for i in sorted_keys:
            if count >= 50:
                sorted_dict[i] = Best_Fifty[i]
            count += 1
        return sorted_dict

    # This is our Mutation Algorithm
    def Mutation(x, num):
        print("This is our Mutation Algorithm")
        propability = 0.6
        count = 0;
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        temp = []

        for i in x:
            default_no = round((random.uniform(0, 1)), 1)
            if default_no > propability:
                choose = random.randint(1, num)
                list2.clear()
                for j in range(len(i)):
                    if (choose == j):
                        a = i[j]
                        list1.clear()
                        for k in range(len(a)):
                            b = format(a[k], '08b')
                            b1 = b.replace('1', 'x')
                            b1 = b1.replace('0', '1')
                            b1 = b1.replace('x', '0')
                            list1.append(int(b1, 2))
                        list2.append(list1)
                    else:
                        list2.append(i[j])
                count += 1
                list3.extend(list2)
            else:
                list4.append(i)

        temp_list = []
        res1 = []
        idx1 = 0
        for i in range(count):
            temp_list.append(num)
        for var_len in temp_list:
            res1.append(list3[idx1: idx1 + var_len])
            idx1 += var_len

        temp = list4
        temp.extend(res1)
        return temp

    # This is our Main Genetic Algorithm
    def Cross_Over(Sorted_Dic, size):
        final = []
        count = 0
        for i in Sorted_Dic.values():
            if count > 1:
                count = 0
            if (count == 0):
                list1 = i[1]
            if (count == 1):
                list2 = i[1]
                list1[0:int(size / 4)], list2[0:int(size / 4)] = list2[0:int(size / 4)], list1[0:int(size / 4)]
                list1[int(3 * size / 2):int(size)], list2[int(3 * size / 2):int(size)] = list2[int(3 * size / 2):int(
                    size)], list1[int(3 * size / 2):int(size)]
                final.append(list1)
                final.append(list2)
            count += 1;
        return final

    # This is our Main Genetic Algorithm
    count = 1

    def Genetic_Algorithm(x, size, bool_var):
        Object = RandomPolygons;
        Cross_Over = []
        Cross_Over.clear()
        Best_Fifty = dict()
        # Checking the Fitness
        for i in range(len(x)):
            res, Fitness = Object.Fitness_Function(x[i], size, bool_var)
            Best_Fifty[str(i)] = [Fitness, res]
            a = size * size - size
            if Fitness > a:
                print('\n\n\nBest Possible Polygons is:')
                print(res, '----', Fitness)
                return True
        print('Answer Not Found')
        print('Generating Generation No ', Object.count + 1)
        # Selecting the Best 50 Chromosomes from selection Function.
        Sorted_Dic = Object.Selection_Wheel(Best_Fifty)

        count1 = 0
        for i in Sorted_Dic.values():
            if (count1 == 49):
                print(i[1], 'Has a Fitness ', i[0])
                Object.Plot_Polygons(i[1])
            count1 += 1

        # Calling the CrossOver for generating the Best 50 Childs
        print("By crossover our Best population is ")
        Cross_Over = Object.Cross_Over(Sorted_Dic, size)
        for i in Sorted_Dic.values():
            Cross_Over.append(i[1])
        print(Cross_Over)
        # Calling the Mutation Function
        print("By Mutation our Best population is ")
        Mutation = Object.Mutation(Cross_Over, size)
        print(Mutation)
        Object.count += 1
        if (Object.count > 150):
            return False
        Object.Genetic_Algorithm(Mutation, size, 1)


[2]
if __name__ == "__main__":
    Object = RandomPolygons;
    pop_chromo = 100
    no_of_points = 0
    # Taking Input Points
    while (no_of_points < 3 or no_of_points > 15):
        no_of_points = int(input("Enter total points "))
        if (no_of_points < 3 or no_of_points > 15):
            print("Invalid Input")
    # Generating the Population
    POPULATION_SIZE = 100
    population = [Object.randomizing_chromosomes(no_of_points) for _ in range(POPULATION_SIZE)]
    # printing the list using loop
    print("\n\nGENERATION 1")
    for x in range(len(population)):
        print(x + 1, '---', population[x])
    # Calling the GA Algorithm
    print(Object.Genetic_Algorithm(population, no_of_points, 0))