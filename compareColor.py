import json
import getColor
import numpy as np
import lipColor


# filename = 'temp.txt'
##write the temp data to file##
def WtoFile(filename, RGB_temp):
    num = len(RGB_temp)
    with open(filename, 'w') as f:
        for i in range(num):
            s = str(RGB_temp[i]).replace('[', '').replace(']', '')
            f.write(s)
            f.write("\n")


# operate the data #
##save the brand&series&color id&color name to sum_list##
##covert the color #D62352 to RGB_array##
##caculate the RGB difference to RGB_temp and write the value to file##
def data_operate():
    with open('color_json/lipstick.json', 'r', encoding='utf-8') as f:
        ret_dic = json.load(f)
        # print(ret_dic['brands'])
        # print(type(ret_dic)) # <class 'dict'>
        # print(ret_dic['brands'][0]['name'])
        b_num = len(ret_dic['brands'])
        # print(b_num)#brands number

        s_list = []
        # series brands#
        for i in range(len(ret_dic['brands'])):
            s_num = len(ret_dic['brands'][i]['series'])
            s_list.append(s_num)
            # print("{0} has {1} series".format((ret_dic['brands'][i]['name']),(s_list[i])))

        # the lipstick color of every brands every series#
        # the first loop calculate the total color numbers
        sum = 0
        for b1 in range(b_num):
            for s1 in range(s_list[b1]):
                brand_name = ret_dic['brands'][b1]['name']
                lip_name = ret_dic['brands'][b1]['series'][s1]['name']
                color_num = len(ret_dic['brands'][b1]['series'][s1]['lipsticks'])
                sum += color_num  # calculate the total color numbers

        # the second loop save the message to a list#
        sum_list = np.zeros((sum, 4), dtype=(str, 8))
        value_array = np.zeros((sum, 6), dtype=int)
        i = 0
        for b2 in range(b_num):
            for s2 in range(s_list[b2]):
                brand_name = ret_dic['brands'][b2]['name']
                # print(type(brand_name))
                lip_name = ret_dic['brands'][b2]['series'][s2]['name']
                color_num = len(ret_dic['brands'][b2]['series'][s2]['lipsticks'])
                for c in range(color_num):
                    color_value = ret_dic['brands'][b2]['series'][s2]['lipsticks'][c]['color']
                    color_name = ret_dic['brands'][b2]['series'][s2]['lipsticks'][c]['name']
                    color_id = ret_dic['brands'][b2]['series'][s2]['lipsticks'][c]['id']
                    # print("{0} series {1} has {2} colors,color {3}：{4}".format(brand_name,lip_name,color_num,c+1,color_name))
                    sum_list[i][0] = brand_name
                    sum_list[i][1] = lip_name
                    sum_list[i][2] = color_id
                    sum_list[i][3] = color_name
                    # value_array[i]=value_array[i][1]
                    # convert "#D62352" to [13  6  2  3  5  2]#
                    for l in range(6):
                        temp = color_value[l + 1]
                        if (temp >= 'A' and temp <= 'F'):
                            temp1 = ord(temp) - ord('A') + 10
                        else:
                            temp1 = ord(temp) - ord('0')
                        value_array[i][l] = temp1
                    i += 1

        # the third loop covert value_array to RGB_array#
        RGB_array = np.zeros((sum, 3), dtype=int)
        for i in range(sum):
            RGB_array[i][0] = value_array[i][0] * 16 + value_array[i][1]
            RGB_array[i][1] = value_array[i][2] * 16 + value_array[i][3]
            RGB_array[i][2] = value_array[i][4] * 16 + value_array[i][5]

        # calculate the similar and save to RGB_temp
        # RGB_temp=np.zeros((sum,1), dtype=int)
        RGB_temp = np.zeros((sum, 1), dtype=float)
        for i in range(sum):
            R = RGB_array[i][0]
            G = RGB_array[i][1]
            B = RGB_array[i][2]
            RGB_temp[i] = abs(get[0] - R) + abs(get[1] * 3 / 4 - G) + abs(get[2] - B)
        RGB_temp.tolist();  # covert array to list
        # print(RGB_temp)
        filename = "temp.txt"
        WtoFile(filename, RGB_temp)
        # sort the RGB_temp#
        result = sorted(range(len(RGB_temp)), key=lambda k: RGB_temp[k])
        # print(result)
        # output the three max prob of the lipsticks#
        print("The first three possible lipstick brand and color id&name are as follows:")
        for i in range(3):
            idex = result[i]
            print(sum_list[idex])
        print("The first three possible lipstick brand RGB value are as follows:")
        for i in range(3):
            idex = result[i]
            R = RGB_array[idex][0]
            G = RGB_array[idex][1]
            B = RGB_array[idex][2]
            tuple = (R, G, B)
            print(tuple)


if __name__ == '__main__':
    # image = getcolor.Image.open(inputpath)
    # image = image.convert('RGB')
    # get=getcolor.get_dominant_color(image)#tuple #get=(231, 213, 211)
    list = []
    color_dir = "images"
    count = lipColor.load_color(color_dir, list)
    get = lipColor.Mean_color(count, list)
    print("the extracted RGB value of the color is {0}".format(get))
    # operate the data#
    data_operate()