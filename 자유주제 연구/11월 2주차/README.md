# Optical Flow
Optical Flow(광학 흐름)은 카메라 또는 물체의 이동에 의해 생기는 연속된 2개의 이미지 간의 어떤 이동에 대한 패턴이다. 
영상은 시간순으로 나열된 2차원 이미지들의 조합인데, 연속된 2개의 이미지 차이를 통해 영상에 존재하는 물체의 움직임을 추정할 수 있다.

Optical Flow를 적용하기 위해서는 
"영상에서 연속하는 두 프레임 간의 관심 픽셀의 밝기값은 변함이 없다." 
라는 전제가 필요하다. 

위 전제가 만족한다면, 영상에서 특정 t프레임의 관심 픽셀(x,y)의 밝기값 I(x,y,t)는 연속하는 다음 프레임에서 위치만 변하고, 
밝기값은 그대로 유지될 것이다. 따라서 다음과 같은 식이 성립한다. 

![image](https://user-images.githubusercontent.com/49221790/99050701-87b84c80-25db-11eb-8830-53a136f91ba9.png)

(1) 식의 우항을 전개하면,

![image](https://user-images.githubusercontent.com/49221790/99050962-9acb1c80-25db-11eb-9309-50225372bccc.png)


가 된다. 이 때, (1)과 (2)를 합치면, 다음과 같은 식이 성립한다.

![image](https://user-images.githubusercontent.com/49221790/99051113-a61e4800-25db-11eb-8226-9242f3ba48af.png)

식 (3)을 다시 정리하면 아래와 같다.

![image](https://user-images.githubusercontent.com/49221790/99051277-b2a2a080-25db-11eb-8c1a-e59a63857b98.png)

와 는 결국, x와 y방향으로의 각각 움직임의 속도를 가리킵니다. 마지막으로, 식(4)를 간추리면
다음과 같이 쓸 수 있다.

![image](https://user-images.githubusercontent.com/49221790/99051428-bfbf8f80-25db-11eb-9bae-d3872c2e6834.png)

영상에서 관심 픽셀들을 설정하고, 각 관심 점들을 중심으로 하는 블록을 설정한다. 그 블록 단위로 저 위의 식을 적용해서 Motion Vector를 구하면 된다. 
OpenCV에서 Lucas-Kanade 라는 API로 제공하고 있다.
