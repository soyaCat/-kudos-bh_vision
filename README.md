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

1. op3와의 호환성을 위하여 jetson tx2에 jetpack 3.3을 플래싱한다.
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
