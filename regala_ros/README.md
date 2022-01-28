# RegalaX ROS Package

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

> This is requirements to run app.py
7. pip install flask
8. pip install sqlalchemy
9. pip install mysql-connector-python

### API
1. recordRegala
    * url: /recordRegala
    * method: POST
    * request:
```json
{
    "user_id": 1,
    "equipment_id": "equipment_id"
}
```
