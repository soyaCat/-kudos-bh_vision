# -kudos-bh_vision
쿠도스 비전 레포지스토리입니다.
---

# 공지

---

# 설명
- 환경세팅에 관하여
  >환경 세팅은 한줄씩 천천히 하세요

- op3_ini_env 폴더
  >빌드가 되는 것을 확인한 op3에 관련된 것만 있는 폴더입니다.
  >op3 빌드 중 문제가 발생시 문제가 되는 파일을 op3_ini_env 폴더 내부의 파일로 교체하세요

---

# 환경 세팅

1. op3와의 호환성을 위하여 jetson tx2에 jetpack 3.3을 설치한다
>jetpack3.3은 우분투 16.04를 지원하는 가장 최신 버전의 jetson os 이미지이다.  
>op3가 ROS melodic을 지원하지 않는 이상 jetpack 3.3 사용이 최선


2. 우분투 패키지를 업데이트 한다.  
```
sudo apt-get upgrade
sudo apt-get update
```

3. ROS kinetict 설치
>참고링크:https://robertchoi.gitbook.io/ros/install
```
wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_kinetic.sh && chmod 755 ./install_ros_kinetic.sh && bash ./install_ros_kinetic.sh
```

```
sudo apt-get install -y chrony ntpdate

sudo ntpdate -q ntp.ubuntu.com

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

sudo apt-get update && sudo apt-get upgrade -y

sudo apt-get install ros-kinetic-desktop-full

sudo apt-get install ros-kinetic-rqt*

sudo rosdep init

rosdep update

sudo apt-get install python-rosinstall

source /opt/ros/kinetic/setup.bash

mkdir -p ~/catkin_ws/src

cd ~/catkin_ws/src

catkin_init_workspace

cd ~/catkin_ws/

catkin_make

source ~/catkin_ws/devel/setup.bash
```
> test시에 다음 명령어를 입력하여 작동을 확인
```
roscore
```
>다음으로 ROS환경설정을 한다
```
gedit ~/.bashrc
```
>>다음 내용이 삽입되어있는지 확인 후 없으면 넣는다.
```
alias eb =‘nano ~/.bashrc'
alias sb ='source ~/.bashrc'
alias cw ='cd ~/catkin_ws'
alias cs ='cd ~/catkin_ws/src'
alias cm ='cd ~/catkin_ws && catkin_make'
source /opt/ros/kinetic/setup.bash
source ~/catkin_ws/devel/setup.bash
export ROS_MASTER_URI=http://localhost:11311
export ROS_HOSTNAME=localhost
```

4. op3 설치
>참고 링크:https://emanual.robotis.com/docs/en/platform/op3/recovery/#recovery-of-robotis-op3  
>추가 로보티즈 ROS패키지를 설치한다.
```
sudo apt install libncurses5-dev v4l-utils

sudo apt install madplay mpg321

sudo apt install g++ git
```
>op3를 위한 ROS패키지를 설치한다.
```
cd ~/catkin_ws/src

git clone https://github.com/ROBOTIS-GIT/face_detection.git

cd ~/catkin_ws

sudo apt install ros-kinetic-robot-upstart

cd ~/catkin_ws/src

git clone https://github.com/bosch-ros-pkg/usb_cam.git

cd ~/catkin_ws

catkin_make

sudo apt install v4l-utils

sudo apt install ros-kinetic-qt-ros
```
>humanoid navigation을 설치한다.
```
sudo apt-get install ros-kinetic-map-server

sudo apt-get install ros-kinetic-humanoid-nav-msgs

sudo apt-get install ros-kinetic-nav-msgs

sudo apt-get install ros-kinetic-octomap

sudo apt-get install ros-kinetic-octomap-ros

sudo apt-get install ros-kinetic-octomap-server
```
>sbpl을 설치한다.
```
cd ~/catkin_ws/src

git clone https://github.com/sbpl/sbpl.git

cd sbpl

mkdir build

cd build

cmake ..

make

sudo make install
```
>humanoid navigation을 마저 설치한다.
>> ! catkin_make 중 humanoid_localization.cpp build에서 pcl/filters/uniform_sampling.h: No such file or directory 애러가 발생할수도 있는데 이는 op3가 pcl의 옛날 uniform_sampling의 패키지의 위치를 참조하기 때문에 발생하는 일임.  
>> ! catkin_ws/src/humanoid_navigation/humanoid_localization/src/HumanoidLocalization.cpp를 gedit으로 열고 #include <pcl/filters/uniform_sampling.h>을 #include <pcl/keypoints/uniform_sampling.h>로 고치자
```
cd ~/catkin_ws/src

git clone https://github.com/ROBOTIS-GIT/humanoid_navigation.git

cd ~/catkin_ws

catkin_make
```
>web_setting tools를 위한 패키지를 설치한다.
```
sudo apt install ros-kinetic-rosbridge-server ros-kinetic-web-video-server
```
>Robotis op3 Robotpackages를 설치하자
>> !catkin_make 중 Robotis-OP3-Tools에서 action_editor 빌드 오류가 날 수도 있는데 깔끔하게 이 레포지스토리에 있는 ROBOTIS-OP3-Tools로 교체하면 해결된다.
```
cd ~/catkin_ws/src

git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git

git clone https://github.com/ROBOTIS-GIT/ROBOTIS-Framework.git

git clone https://github.com/ROBOTIS-GIT/ROBOTIS-Framework-msgs.git

git clone https://github.com/ROBOTIS-GIT/ROBOTIS-Math.git

git clone https://github.com/ROBOTIS-GIT/ROBOTIS-OP3.git

git clone https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Demo.git

git clone https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-msgs.git

git clone https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Tools.git

git clone https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common.git

git clone https://github.com/ROBOTIS-GIT/ROBOTIS-Utility.git

cd ~/catkin_ws

catkin_make
```

5. miniconda 설치
>참고링크: https://kynk94.github.io/devlog/post/jetson-nano-conda  
> - https://github.com/conda-forge/miniforge/releases에 접속하여 Miniforge3-Linux-aarch64.sh 또는 Miniforge3-x.x.x-Linux-aarch64.sh를 다운  
>다운 받은 bash 파일 실행(Miniforge3-Linux-aarch64.sh 자리에 다운 받은 파일 이름을 써야함!)
```
chmod +x Miniforge3-Linux-aarch64.sh
./Miniforge3-Linux-aarch64.sh
```
>터미널 껐다 키기
>가상환경을 만들어주기 위해 다음 명령어를 입력
```
conda create -n tensor27 python=2.7
```
>다음 명령어로 가상환경에 접속
```
conda activate tensor27
```
>ROS 패키지 설치
```
pip install -U rospkg
```

6. tensorflow 설치
>참고주소:https://kynk94.github.io/devlog/post/jetson-nano-conda  
>환경세팅  
>! h5py 설치중 에러가 날 경우 다음을 차근차근 입력  
>! pip install Cython  
>! pip install h5py  
```
conda activate tensor27

sudo apt-get update

sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran

pip install testresources setuptools

pip install numpy future mock h5py keras-preprocessing keras-applications futures protobuf pybind11
```
> 텐서플로우 설치
```
pip install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v33 tensorflow-gpu
```
> 텐서플로우 설치 확인
```
python

import tensorflow
```
