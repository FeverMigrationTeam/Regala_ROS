# Regala_ROS

## Install Guide
### Prerequistion 
1. ROS
2. usb cam
    - avframe_camera_size_ = avpicture_get_size(AV_PIX_FMT_YUV420P, image_width, image_height); 
3. Camera Info Manager 
4. v4l2-ctl
 - sudo apt-get install v4l-utils
 - v4l-utils v4l2-ctl --list-devices

5. opencv python install
 - sudo python3 -m pip install opencv-python opencv-contrib-python

6. scikit-learn install 

## Code
### Core Code
1. rtsp_test.py  : 카메라 ON / OFF
2. video_stitcher.py : 이미지 스티칭
3. video_recorder.py : 녹화
4. google_drive_test.py : 구글 드라이브 업로드
