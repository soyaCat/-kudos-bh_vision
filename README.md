# -kudos-bh_vision
쿠도스 비전 레포지스토리입니다.
---

# 공지
 - 버그, 문제 발생, 개선점 제안은 issues에 제안 부탁드립니다.

---

# 설명
- 환경세팅에 관하여(SETUP ENV)
  >환경 세팅은 한줄씩 천천히 하세요  
  >환경 세팅은 오래 걸립니다. 여유를 가지고 진행하세요  

- op3_ini_env 폴더
  >빌드가 되는 것을 확인한 op3에 관련된 것만 있는 폴더입니다.
  >op3 빌드 중 문제가 발생시 문제가 되는 파일을 op3_ini_env 폴더 내부의 파일로 교체하세요

---

# 최신 비전으로 패치방법
- catkin_ws/src/darknet 폴더를 darknetA로 이름을 바꾼다.
- git clone으로 레포지스토리를 복사하거나 zip파일을 다운받는다.
- darknetA폴더에 복사한 내용물을 넣어준다. 겹치는 파일은 덮어쓰기 처리를 해준다.
- catkin_ws 폴더로 가서 catkin_make수행
- 오류가 안 났다면 메인폴더/src/darknetA로 가서 아나콘다 가상환경 실행
- python Kudos_test.py를 실행해본다.
- rosrun darknetA topic_subscriber를 실행해본다.
- python darknet_images.py를 입력해서 darknet 작동을 확인
- 여기까지 동작하면 패치 성공입니다.

- !파이썬이 커스텀 메세지를 임포트하지 못할 때:   
    >참고문서: https://answers.ros.org/question/105711/rospy-custom-message-importerror-no-module-named-msg/  
    >참고문서: https://answers.ros.org/question/271620/importerror-no-module-named-xxxxmsg/
    >- catkin_make 작업 이후에 source devel/setup.bash를 해주었다.  
    >- 만약 지속적으로 오류가 발생하는 경우 .bashrc에 source/catkin_ws/devel/setup.bash를 해준다.
    
    
   ---
   
   # 비전 실행 방법
    - 터미널상에서 cd catkin_ws/src/darknetA로 간다.
    - 아나콘다 가상환경을 활성화해준다. source activate tensor27
    - python kudos_vision.py로 비전프로그램을 실행시켜준다.
    - 비전 결과는 message로 전송되는데 darknetA/position.msg파일을 임포트해주면 메세지를 읽을 수 있다.
    >팁  
    >우분투 메인폴더에서 ctrl+h를 누르면 숨겨진 파일들이 보이는데 .bashrc를 gedit으로 열어서 맨 밑에  
    >cd catkin_ws/src/darknetA  
    >source activate tensor27  
    >를 추가해주면 터미널을 열 때마다 darknetA폴더에서 tensor27가상환경이 활성화 되어있는 상태로 터미널을 열 수 있다.
