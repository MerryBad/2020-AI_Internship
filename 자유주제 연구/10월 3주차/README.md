# 재설치 시도

-----------------------------
~도르마무! 거래를 하러 왔다!~ \
구글링을 통해 수십번을 재부팅과 재설치를 한 것 같은데 아무 것도 해결해주지 못했다..
멀티부팅하려면 USB도 사야되고 ..

https://superuser.com/questions/1472124/gpu-passthrough-from-windows-10-to-ubuntu-on-vmware-player \
(GPU 기능은 사서 쓰세요) \
https://bladewalker.tistory.com/647 \
(멀티부팅 하시라구요) 

꼬리를 흔들거나 발로 귀를 긁는 등의 행동을 파악하기 위해 \
스켈레톤 기반 정보로 라벨링 할려고 Supervisely를 사용할려는 것인데 \
다른 방법이 없을까? 하다가 재미있어보이는 논문을 발견했다.

# 새로운 툴킷 발견
https://www.biorxiv.org/content/10.1101/620245v2.full \
Fast and robust animal pose estimation 이라는 논문인데,\
동물 자세를 자동으로 측정해주는 DeepPoseKit라는 툴킷을 공개하였다.\
https://github.com/jgraving/DeepPoseKit \
예시로 파리와 메뚜기 ~왜 동물이 아니지?~ 와 얼룩말을 볼 수 있었는데\
설치도 어렵지 않고 구글코랩에서도 사용할 수 있는 것 같아 한번 사용해봐야겠다.\
논문 자체도 배울 점이 많은 것 같아 공부해보아야겠다. ~32페이지..~\

robust가 건장하다는 뜻으로 알고 있는데, 통계학에서는 이상치/에러값으로 부터 영향을 크게 받지 않는 (건장한) 통계량이라고 한다.

## 결론
- VMware + 우분투 + GPU(ndivia, cuda)는 안된다.. ~삭제~ \
- 새로운 툴킷을 활용해보자
       
