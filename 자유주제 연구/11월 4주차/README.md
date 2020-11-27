# 2020-AI_Internship
저번 캐글 챌린지에서 시간이 종료됨에 따라 다른 사람들이 코드를 공개했는데,  
딥러닝보다는 그냥 포커의 규칙에 넣은 경우도 꽤 보였다.  
https://www.kaggle.com/smashh712/pokerhand  
![image](https://user-images.githubusercontent.com/49221790/100432109-77749700-30dc-11eb-95e8-905551515a1a.png)  
이 분은 데이터 전처리로 카드번호를 정렬하고 일치하는 모양의 갯수와 각 카드값들의 차를 특징으로 삼았다.  
![image](https://user-images.githubusercontent.com/49221790/100432894-99bae480-30dd-11eb-9e42-6c42545ca8d0.png)  
이런식으로 기존의 10개의 피처 외에 5개의 피처를 추가하였다.  
![image](https://user-images.githubusercontent.com/49221790/100433115-f1595000-30dd-11eb-910c-87315f165066.png)  
결정트리분류기를 이용하여 fit하였는데 지니 인덱스를 사용하였다. ~지니인덱스가 뭐엿지~  
이렇게 해서 나온 결과는 약 0.99로 나왔다. ~성능 확실하구만!~  



이 경우에는 포커라는 것을 모르고 그냥 데이터셋만 주었을 때 

