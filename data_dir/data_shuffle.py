# -*- coding:utf-8 -*-
# -*- created by: rsh -*-
import numpy as np

'''读取txt文件'''
def txtRead(filePath, encodeType = 'utf-8'):
    listLine = []
    try:
        file = open(filePath, 'r', encoding= encodeType)

        while True:
            line = file.readline()
            if not line:
                break

            listLine.append(line)

        file.close()

    except Exception as e:
        print(str(e))

    finally:
        return listLine

'''读取txt文件'''
def txtWrite(listLine, filePath, type = 'w',encodeType='utf-8'):

    try:
        file = open(filePath, type, encoding=encodeType)
        file.writelines(listLine)
        file.close()

    except Exception as e:
        print(str(e))

def oper_old():
    data_dailrys = txtRead('train_old.csv')
    dailrys = []
    for data_dailry in data_dailrys:
        data_dailry_two =data_dailry.strip().split('\t')
        dailrys.append('0,' + data_dailry_two[0] +  ','+ data_dailry_two[1] + '\n')

    txtWrite(dailrys, 'train.csv', type='a+', encodeType='utf-8')

def shuffle_list(datas):
    np.random.shuffle(datas)
    return datas

def shuffe_gov_20000(path_all, size = 0.95):
    datas_all = txtRead(path_all)
    dai = []
    gov = []
    for datas_one in datas_all:
        data_one_three = datas_one.strip().split(',')
        if len(data_one_three) == 3 and data_one_three[1] == '0.0':
            gov.append('1,' +data_one_three[0].strip().replace(' ', '') + '\n')
        elif len(data_one_three) == 3 and data_one_three[1] == '1.0':
            dai.append('0,' + data_one_three[0].strip().replace(' ', '') + '\n')
        else:
            print('wrong: ' + datas_one)

    #shuffle, 分领域
    gov = shuffle_list(gov)
    dai = shuffle_list(dai)
    len_gov = len(gov)
    len_dai = len(dai)

    gov_train = gov[0: int(len_gov * size)]
    dai_train = dai[0: int(len_dai * size)]
    gov_dev = gov[int(len_gov * size):]
    dai_dev = dai[int(len_dai * size):]

    train_data = shuffle_list(gov_train + dai_train)
    dev_data = shuffle_list(gov_dev + dai_dev)

    txtWrite(train_data, 'class_gov/train.csv', type='a+', encodeType='utf-8')
    txtWrite(dev_data, 'class_gov/dev.csv', type='a+', encodeType='utf-8')

path_all = 'class_gov/train_data_short_error_skill.csv'
shuffe_gov_20000(path_all, size=0.95)

def get_test(path_all):
    datas_all = txtRead(path_all)
    dai = []
    gov = []
    for datas_one in datas_all:
        data_one_three = datas_one.strip().split(',')
        if len(data_one_three) == 3 and data_one_three[1] == '0.0':
            gov.append('1,' +data_one_three[0].strip().replace(' ', '') + '\n')
        elif len(data_one_three) == 3 and data_one_three[1] == '1.0':
            dai.append('0,' + data_one_three[0].strip().replace(' ', '') + '\n')
        else:
            print('wrong: ' + datas_one)
    test_datas = gov + dai
    txtWrite(test_datas, 'class_gov/test.csv', type='a+', encodeType='utf-8')

path = 'class_gov/cut_test_data.csv'
get_test(path)


# file_path = os.path.join(data_dir, 'train.csv')
# with open(file_path, 'r', encoding='utf-8') as f:
#     reader = f.readlines()
# examples_all = []
# labels_all = []
# for index, line in enumerate(reader):
#     guid = 'train-%d' % index
#     split_line = line.strip().split(',')
#     text_a = tokenization.convert_to_unicode(split_line[1])
#     # text_b = tokenization.convert_to_unicode(split_line[2])
#     label = split_line[0]
#
#     labels_all.append(tokenization.convert_to_unicode(split_line[0]))
#     examples_all.append(InputExample(guid=guid, text_a=text_a,
#                                      text_b=None, label=label))
# length = len(labels_all)
# length_train = int(length * 0.95)
# index = [i for i in range(length)]
# np.random.shuffle(index)
# examples = examples_all[index]
# labels = labels_all[index]