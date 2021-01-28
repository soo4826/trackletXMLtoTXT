import os

result_dir = './dst_sort'
src_dir = './dst'
file_list = os.listdir(src_dir)
file_test = './dst/0001.txt'
file_save_test = './dst_sort/0001.txt'
for idx in file_list:
    with open(os.path.join(src_dir,idx), 'r') as open_op:

        data= open_op.readlines()
        data_list = list()
        for data_sp in data:
            data_l = data_sp.split(' ')
            dic = {'key': int(data_l[0]), 'dt': data_l[1:]}
            data_list.append(dic)
        # print(data)
        print(str(idx) + " sorted\n")
        data_sorted = sorted(data_list, key=lambda data_list_: data_list_['key'])
        open_op.close()
    with open(os.path.join(result_dir, idx), 'a') as save_op:
        for jdx in data_sorted:
            rst = str(jdx['key']) + ' ' + str(' '.join(jdx['dt']))
            print(rst)
            save_op.writelines(rst)
        # for idx_ in range(0, len(data_sorted)):
        #     print(data_sorted
        #     # rst = str(data_sorted['key']) + ' ' + data_sorted['dt']
        #     save_op.writeline(rst)
        print(str(idx) + " saved\n")
        save_op.close()


# for idx in file_list:
#     os.open(idx,r)
