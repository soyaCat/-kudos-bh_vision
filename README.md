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
- git clone으로 레포지스토리를 복사하거나 zip파일을 다운받는다.
- darknet폴더에 복사한 내용물을 넣어준다. 겹치는 파일은 덮어쓰기 처리를 해준다.
- ros 메인 폴더로 가서 catkin_make수행
- 오류가 안 났다면 메인폴더/src/darknet으로 가서 아나콘다 가상환경 실행
- python을 입력해서 인터프리터 창에 들어간 후 , import rospy, import cv2, import tensorflow를 차례로 수행해준다.
- 오류가 안났다면 ctrl+z를 눌러서 인터프리터 창을 나간다.
- python darknet_images.py를 입력해서 darknet 작동을 확인
- 여기까지 오류가 안났다면 내 패치에 문제가 없다는 거니까 다행입니다.

- !파이썬이 커스텀 메세지를 임포트하지 못할 때:   
https://answers.ros.org/question/105711/rospy-custom-message-importerror-no-module-named-msg/

https://answers.ros.org/question/271620/importerror-no-module-named-xxxxmsg/

- 나의 경우에는 darknet폴더를 darknetA로 바꾸고
- catkin_make 작업 이후에 source devel/setup.bash를 해주었다.  
- 만약 지속적으로 오류가 발생하는 경우 .bashrc에 source/catkin_ws/devel/setup.bash를 해준다.
