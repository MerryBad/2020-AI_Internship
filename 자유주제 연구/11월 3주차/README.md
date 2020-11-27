# 2020-AI_Internship
https://www.kaggle.com/c/urbanchanllange \
저번 방학때 들었던 인공지능교육에서 캐글 챌린지를 개최했다.  
포커 데이터셋으로 5쌍의 모양-숫자 카드를 입력받아서 어떤 패가 나오는지 예측해야 한다.  


----------------------------------------------------------------------------

먼저 poker-hand.names 파일을 읽어보면
   1) S1 �Suit of card #1�
      Ordinal (1-4) representing {Hearts, Spades, Diamonds, Clubs}
   2) C1 �Rank of card #1�
      Numerical (1-13) representing (Ace, 2, 3, ... , Queen, King)  
이런 식으로 모양과 숫자쌍으로 되있는 데이터가 5개 있고 

   11) CLASS �Poker Hand�
      Ordinal (0-9)

      0: Nothing in hand; not a recognized poker hand 
      1: One pair; one pair of equal ranks within five cards
      2: Two pairs; two pairs of equal ranks within five cards
      3: Three of a kind; three equal ranks within five cards
      4: Straight; five cards, sequentially ranked with no gaps
      5: Flush; five cards with the same suit
      6: Full house; pair + different rank three of a kind
      7: Four of a kind; four equal ranks within five cards
      8: Straight flush; straight + flush
      9: Royal flush; {Ace, King, Queen, Jack, Ten} + flush
      
와 같이 마지막에 조합에 따라 숫자를 저장하고 있다.  

------------------------------------------------------------------------

처음 배웠을 때 텐서플로우 1.xx버전으로 공부했던 터라 예전에 작성했던 코드들을 활용하지 못했다.  
~세션이랑 플레이스홀더 돌려줘요~  
2.xx버전에서도 1.xx버전으로 돌릴 수 있다고 해서 시도해봤는데 안 돌아갔다..

-----------------------------------------------------------------
https://www.kaggle.com/merrybad/notebooke61c3d57a2  

먼저 데이터가 어떤식으로 생겼나 확인해본다.  
![1](https://user-images.githubusercontent.com/49221790/100415459-88fb7600-30bf-11eb-85e7-9e17ebaa59cc.PNG)  
제일 첫 열에 Id가 있으므로 학습데이터 구성할 때 빼야겠다.  

![2](https://user-images.githubusercontent.com/49221790/100415694-1c34ab80-30c0-11eb-95bf-8d2a75cc97d0.PNG)  
각 데이터에 결측치가 없고 전부 int64타입임을 확인했다.

![image](https://user-images.githubusercontent.com/49221790/100416191-2d31ec80-30c1-11eb-90d2-e54ff5c09212.png)  
모양과 숫자는 적절하게 섞여있는데 조합(CLASS)는 0,1이 압도적으로 많고 뒤에는 거의 없다시피하다.  
학습데이터에서 학습, 테스트 데이터로 나눌때 잘 못나누면 학습쪽에 몇몇 클래스가 없지 않을까 싶었다.

![image](https://user-images.githubusercontent.com/49221790/100416709-759dda00-30c2-11eb-9165-b7438a0d2169.png)  
클래스는 0~9까지 총 10개가 있어야 하는데 학습데이터에서는 9개밖에 없었다.  
![image](https://user-images.githubusercontent.com/49221790/100417269-e09be080-30c3-11eb-82c7-acebc0276ca8.png)  
학습데이터에 8이 없다!  
![image](https://user-images.githubusercontent.com/49221790/100418103-7edc7600-30c5-11eb-8d6f-cc59575010a4.png)  
정규화를 한 뒤 섞은 후, 8:2비율로 학습과 검증데이터를 나누었다.  
Y값을 분류문제에 맞게 10개의 원핫벡터로 만들었다. 학습데이터에 9개밖에 없으니까 9개로 해야되나?  
![image](https://user-images.githubusercontent.com/49221790/100418922-e0e9ab00-30c6-11eb-8265-737375f3c8ab.png)  
우선 간단하게 3개의 레이어로 10개의 출력을 갖는 소프트맥스 함수가 나오도록 했다.
![image](https://user-images.githubusercontent.com/49221790/100419010-ffe83d00-30c6-11eb-9e05-d65f811b6357.png)  
epochs는 10번으로 batch_size는 32개로 돌려봤는데 어?  
![image](https://user-images.githubusercontent.com/49221790/100420331-99185300-30c9-11eb-9017-5a40dd20d4b3.png)  
몬가..몬가 잘못되었다.. 딥러닝에선 1이 나올수가 없다고 알고있는데..  
![image](https://user-images.githubusercontent.com/49221790/100421107-12647580-30cb-11eb-8c0c-f2d1239c27c3.png)  
테스트 데이터를 넣고 결과값을 구해보았을 때 전부 0으로 출력되었다.  
![image](https://user-images.githubusercontent.com/49221790/100421666-2e1c4b80-30cc-11eb-94c6-d85c5dd0fe1b.png)  
result에서 원핫벡터로 만든거 다시 숫자로 만들어주려고 argmax를 사용했는데 주석처리 하고 해도 결과는 똑같이 0으로만 나왔다. ~버근가?~  
![image](https://user-images.githubusercontent.com/49221790/100425243-2e1f4a00-30d2-11eb-9414-f9c05503b62a.png)  
0만 넣었는데 50%정도 나왔다..

---------------------------------------------------------

1버전과 2버전이 많이 달라서 처음에 삽질을 많이 했다.  
작성 후에는 왜 답이 다 0만 나오게 되었는지 고민되었다.
일단 정규화를 주석처리하고 해보았을 때에는  
![image](https://user-images.githubusercontent.com/49221790/100427686-295c9500-30d6-11eb-81bf-acf28ae093de.png)  
![image](https://user-images.githubusercontent.com/49221790/100427719-36798400-30d6-11eb-9dea-9298322339aa.png)  
이렇게 나와서 정상적으로 되나 싶었는데 
![image](https://user-images.githubusercontent.com/49221790/100429124-3b3f3780-30d8-11eb-8973-3aa30701fd1f.png)  
0.4~0.5사이를 못 벗어났다.  
종료한 뒤 다른 사람들 코드도 확인해봐야겠다..
