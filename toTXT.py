
import os
from parseTrackletXML import parseXML as pa


# dirs = os.path.join(os.path.join(path, date), '2011_09_26_drive_' + str(i).zfill(4) + '_sync')
dirs = "./"
save_label_dir = "./dst" # save file directory

if os.path.exists(dirs):
    # check if the dir exists:
    # save_label_dir = os.path.join(os.path.join(label_save_path, date), '2011_09_26_drive_' + str(i).zfill(4) + '_sync')
    if os.path.exists(save_label_dir):
        raise RuntimeError('Dir exists!')
    else:
        os.makedirs(save_label_dir)

    label_file = os.path.join(dirs, 'tracklet_labels.xml')
    labels = pa(label_file)

    track_id = 1 # track_id starts 1
    i = 0
    label_vaild = ['Car', 'Pedestrian', 'Cyclist'] # select valid labels
    flag = False

    for label in labels:
        for j in range(label.nFrames):

            each_frame = label.firstFrame+j
            save_file = os.path.join(save_label_dir, ''.zfill(4)+'.txt')
            with open(save_file, 'a') as save_op:
                assert(label.rots[j][0] == label.rots[j][1] == 0)
                # save data format
                # frame, track_id, obj_type, 0, 0, 0, 0, 0, 0, 0 h, w, l, x, y, z, rot_y(rz), alpha
                if label.objectType in label_vaild:
                    save_str = str(each_frame) + ' ' + str(track_id) + ' ' + str(label.objectType) + ' ' + '0 0 0 0 0 0 0 ' \
                             + str(label.size[0]) + ' ' + str(label.size[1]) + ' ' + str(label.size[2]) \
                             + ' ' + str(label.trans[j][0]) + ' ' + str(label.trans[j][1]) + ' ' + str(label.trans[j][2]) \
                             + ' ' + str(label.rots[j][2]) + '\n'
                    save_op.write(save_str)
        if flag:
            track_id+=1
            flag = False

