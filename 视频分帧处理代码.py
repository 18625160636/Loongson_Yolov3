def cut(video_file, target_dir):
    '''
    切分所有的文件
    :param all_file: 所有的文件列表
    :param target_dir: 图片存放文件夹
    :return: 无返回
    '''

    cap = cv2.VideoCapture(video_file)
    isOpened = cap.isOpened 
    temp = os.path.split(video_file)[-1]
    dir_name = temp.split('.')[0]

    single_pic_store_dir = os.path.join(target_dir, dir_name)
    if not os.path.exists(single_pic_store_dir):
        os.mkdir(single_pic_store_dir)


    i = 0
    while isOpened:


        (flag, frame) = cap.read()  # 读取一张图像

        fileName = 'image' + str(i) + ".jpg"

        if (flag == True):         
            #frame = np.rot90(frame, -1)
            #print(fileName)
            save_path = os.path.join(single_pic_store_dir, fileName)
            #print(save_path)
            if i % 50 == 1:
                res = cv2.imwrite(save_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
                #print(res)
            i+=1

        else:
            break

    return single_pic_store_dir

if __name__ == '__main__':
    video_file = 'G3142.mp4'
    cut(video_file, 'target_pic')