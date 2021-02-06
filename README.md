# -kudos-bh_vision
쿠도스 비전 레포지스토리입니다.
---

공지

---

설명
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
