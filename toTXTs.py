# for label
import os
from parseTrackletXML import parseXML as pa


# dirs = os.path.join(os.path.join(path, date), '2011_09_26_drive_' + str(i).zfill(4) + '_sync')
dirs = "./2011_09_26"
save_label_dir = "./dst"

if os.path.exists(dirs):
    # check if the dir exists:
    # save_label_dir = os.path.join(os.path.join(label_save_path, date), '2011_09_26_drive_' + str(i).zfill(4) + '_sync')
    if os.path.exists(save_label_dir):
        raise RuntimeError('Dir exists!')
    else:
        os.makedirs(save_label_dir)

    # 폴더 읽어오기    
    folder_list = os.listdir(dirs)
    print(len(folder_list))
    
    label_vaild = ['Car', 'Pedestrian', 'Cyclist']
    flag = False
    for idx in folder_list:
        track_id = 1
        idx_path = idx.split('_')[4]
        file_path = os.path.join(dirs, idx, 'tracklet_labels.xml' )
        labels = pa(file_path)

        for label in labels:
            for j in range(label.nFrames):

                each_frame = label.firstFrame+j
                save_file = os.path.join('./dst', idx_path +'.txt')
                with open(save_file, 'a') as save_op:
                    assert(label.rots[j][0] == label.rots[j][1] == 0)
                    if label.objectType in label_vaild:
                        save_str = str(each_frame) + ' ' + str(track_id) + ' ' + str(label.objectType) + ' ' + '0 0 0 0 0 0 0 ' \
                                + str(label.size[1]) + ' ' + str(label.size[0]) + ' ' + str(label.size[2]) \
                                + ' ' + str(label.trans[j][0]) + ' ' + str(label.trans[j][1]) + ' ' + str(label.trans[j][2]) \
                                + ' ' + str(label.rots[j][2]) + '\n'
                        save_op.write(save_str)
                        flag = True
            if flag:
                track_id+=1
                flag = False




    # label_file = os.path.join(dirs, 'tracklet_labels.xml')
    # labels = pa(label_file)
    

    # track_id = 1
    # # 154개씩 파일 저장!
    # i = 0
    # label_vaild = ['Car', 'Pedestrian', 'Cyclist']
    # flag = False
    # # for i in range(0, 18):
    # #     save_label_dir_tmp= os.path.join(save_label_dir, )
    # #     print(save_label_dir_tmp)
    # for label in labels:
    #     for j in range(label.nFrames):

    #         each_frame = label.firstFrame+j
    #         save_file = os.path.join(save_label_dir, ''.zfill(4)+'.txt')
    #         with open(save_file, 'a') as save_op:
    #             assert(label.rots[j][0] == label.rots[j][1] == 0)
    #             # x,y,z,h,w,l,theta
    #             # To [frame, track_id, obj_type, truncation, occlusion, obs_angel, [pixel_data], h, w, l, X, Y, Z, yaw]
    #             # label.frameIdx ? label.objectType label.truncs[frameIdx], label.states[frameIdx, 0] ? (hwl, xyz:

    #             # str_to_srite = '%d %d %s 0 0 %f %f %f %f %f %f %f %f %f %f %f %f %f\n' % (frame, id_tmp,
    #             # type_tmp, ori_tmp, bbox2d_tmp_trk[0], bbox2d_tmp_trk[1], bbox2d_tmp_trk[2], bbox2d_tmp_trk[3],
    #             # bbox3d_tmp[0], bbox3d_tmp[1], bbox3d_tmp[2], bbox3d_tmp[3], bbox3d_tmp[4], bbox3d_tmp[5], bbox3d_tmp[6],
    #             # conf_tmp)
    #             # frame, track_id, obj_type, 0, 0, 0, 0, 0, 0, 0 h, w, l, x, y, z, rot_y(rz), alpha
    #             # w h l
    #             # yzx
    #             if label.objectType in label_vaild:
    #                 save_str = str(each_frame) + ' ' + str(track_id) + ' ' + str(label.objectType) + ' ' + '0 0 0 0 0 0 0 ' \
    #                          + str(label.size[1]) + ' ' + str(label.size[0]) + ' ' + str(label.size[2]) \
    #                          + ' ' + str(label.trans[j][0]) + ' ' + str(label.trans[j][1]) + ' ' + str(label.trans[j][2]) \
    #                          + ' ' + str(label.rots[j][2]) + '\n'
    #                 save_op.write(save_str)
    #                 flag = True
    #             """
    #             OLD
    #             save_str = str(each_frame) + ' ' + str(track_id) + ' ' + str(label.objectType) + ' ' + str(0)+ ' ' + str(int(label.occs[j][0]))+' ' + "0" + ' ' + "1 1 1 1" + ' '\
    #                     +  str(label.size[0]) + ' ' + str(label.size[1]) + ' ' + str(label.size[2]) \
    #                     + ' ' + str(label.trans[j][0]) + ' ' + str(label.trans[j][1]) + ' ' + str(label.trans[j][2]) \
    #                     + ' ' + str(label.rots[j][2])  + ' ' + str(1) + '\n'
    #             """

    #             # save_str = label.objectType + ' ' + str(label.trans[j][0]) + ' ' + str(label.trans[j][1]) + ' ' + str(label.trans[j][2]) + \
    #             #          ' ' + str(label.size[0]) + ' ' + str(label.size[1]) + ' ' + str(label.size[2]) + ' ' +str(label.rots[j][2]) + '\n'
    #             # save_op.write(save_str)
    #     if flag:
    #         track_id+=1
    #         flag = False

