# 2020-AI_Internship
https://www.kaggle.com/c/riiid-test-answer-prediction  
학생의 성과 기록과 같은 질문에 대한 다른 학생의 성과, 질문 자체에 대한 메타데이터 등으로
학생이 다음 질문에 올바르게 답할 수 있는지 예측하는 것이 목표.

학습데이터가 5.45GB로 매우 큰 편이고, 시계열 API를 사용해야 한다.  

>**row_id**: (int64) ID code for the row.  
ID 들어있는 열  

>**timestamp**: (int64) the time in milliseconds between this user interaction and the first event completion from that user.  
사용자 인터렉션과 사용자간의 첫번째 이벤트 완료사이의 시간 (밀리초)  

>**user_id**: (int32) ID code for the user.  
사용자의 ID코드  

>**content_id**: (int16) ID code for the user interaction  
사용자 인터렉션의 ID코드   

>**content_type_id**: (int8) 0 if the event was a question being posed to the user, 1 if the event was the user watching a lecture.  
0은 사용자에게 질문하는 이벤트, 1은 사용자가 강의를 시청하는 경우  

>**task_container_id**: (int16) Id code for the batch of questions or lectures. For example, a user might see three questions in a row before seeing the explanations for any of them. Those three would all share a task_container_id.  
질문이나 강의의 일괄처리를 위한 ID코드? 예를 들어, 사용자는 그 중 하나에 대한 설명을 보기 전에 세 개의 질문을 연속으로 볼수있다. 이들 셋은 id를 공유할 것이다?  

>**user_answer**: (int8) the user's answer to the question, if any. Read -1 as null, for lectures.  
질문에 대한 사용자의 대답, 비어있으면 -1로 해놓음. 강의에서  

>**answered_correctly**: (int8) if the user responded correctly. Read -1 as null, for lectures.  
사용자가 맞게 대답한 경우, 비어있으면 -1임. 강의에서  

>**prior_question_elapsed_time**: (float32) The average time in milliseconds it took a user to answer each question in the previous question bundle, ignoring any lectures in between. Is null for a user's first question bundle or lecture. Note that the time is the average time a user took to solve each question in the previous bundle.  
사용자가 이전 질문들의 각 질문에 답하는데 걸리는 평균 시간(밀리초). 사용자가 첫번째 질문이나 강의의 경우에는 null로 되있음. 시간은 사용자가 이전 질문들의 각 문제를 해결하기 위해 걸린 평균 시간란 것을 유의.  

>**prior_question_had_explanation**: (bool) Whether or not the user saw an explanation and the correct response(s) after answering the previous question bundle, ignoring any lectures in between. The value is shared across a single question bundle, and is null for a user's first question bundle or lecture. Typically the first several questions a user sees were part of an onboarding diagnostic test where they did not get any feedback.  
사용자가 이전 질문들에 답한 후 설명과 정확한 답변을 보았는지 여부, 중간 강의는 무시했는지 여부. 이 값은 단일 질문들에 걸쳐 공유되며, 사용자의 첫 번째 질문 번들 또는 강의에 대해서는 null이다.  
일반적으로 사용자가 처음 보는 몇 가지 질문은 피드백을 받지 못하는 탑재형 진단 테스트의 일부.


먼저 학습데이터를 읽어와서 어떻게 생긴 건지 확인하려고 했는데
OOM 때문에 데이터를 불러올수가 없었다..
![image](https://user-images.githubusercontent.com/49221790/102684176-a4b6ef80-4219-11eb-8c12-e0027afa6b5a.png)

-----------------------------------------
https://www.kaggle.com/rohanrao/tutorial-on-reading-large-datasets  
규모가 큰 데이터셋에 접근하는 방법에 대해 찾아보았다.  

## Method: Pandas
Pandas는 아마도 가장 널리 사용되는 데이터 세트 읽기 방법이며 Kaggle의 기본값이기도합니다. 
데이터 읽기 및 처리를위한 많은 옵션, 유연성 및 기능이 있습니다.
대규모 데이터 세트를 읽기 위해 pandas를 사용할 때 발생하는 문제 중 하나는 데이터 세트 열의 데이터 유형을 추론하면서 종종 pandas 데이터 프레임에 불필요한 대용량 메모리 사용을 유발하는 것이 보수적이라는 것입니다.  
사전 지식 또는 샘플 검사를 기반으로 열의 최적 데이터 유형을 미리 정의하고 데이터 세트를 읽는 동안 명시 적으로 제공 할 수 있습니다.

![image](https://user-images.githubusercontent.com/49221790/102684496-7555b200-421c-11eb-93e9-08db500b2d87.png)

생각보다 많이 무거운 얘였다.. 약 9분

## Method: Dask
Dask는 기본적으로 병렬 처리 아키텍처를 사용하여 Pandas 워크 플로를 확장하는 프레임 워크를 제공합니다. 스파크를 사용 해본 분들은 둘 사이에 기이 한 유사점을 발견 할 것입니다.

![image](https://user-images.githubusercontent.com/49221790/102684592-37a55900-421d-11eb-9f43-22c134597597.png)

Pandas를 바탕으로 하는 만큼 여전히 무거웠다.. 약 7분

## Method: Datatable
Datatable (R의 data.table에서 크게 영감을 얻음)은 대규모 데이터 세트를 상당히 빠르게 읽을 수 있으며 종종 Pandas보다 빠릅니다. 특히 속도와 대용량 데이터 지원에 중점을 둔 테이블 형식 데이터 세트의 데이터 처리를위한 것입니다.

![image](https://user-images.githubusercontent.com/49221790/102684628-9bc81d00-421d-11eb-9c82-23d9a5f0cde7.png)

열 데이터 유형 안 적어줘도 시간도 적게들고 표도 이쁘게 나왔다. 약 1분

## Method: Rapids
Rapids는 GPU에서 데이터 처리를 확장 할 수있는 훌륭한 옵션입니다. 많은 기계 학습 모델링이 GPU로 이동함에 따라 Rapids를 사용하면 하나 이상의 GPU에서 엔드 투 엔드 데이터 과학 솔루션을 구축 할 수 있습니다.

![image](https://user-images.githubusercontent.com/49221790/102684746-b058e500-421e-11eb-88a0-3ee1adcdc33f.png)

설치방법이 조금 복잡했다.. GPU를 여러개 사용할때 사용하면 좋은 것 같다.

## File Formats
데이터 세트를 읽기 쉽고 빠르거나 크기가 작은 형식으로 변환하는 것이 일반적입니다. 데이터 세트를 저장할 수있는 다양한 형식이 있지만 모든 패키지를 다른 패키지에서 읽을 수있는 것은 아닙니다. 이러한 데이터 세트를 다른 형식으로 변환하는 방법을 살펴 보겠습니다.

## Format: csv
대부분의 Kaggle 데이터 세트는 csv 형식으로 제공되며 데이터 세트가 공유되는 거의 표준 형식입니다. csv에서 데이터를 읽는 데 거의 모든 방법을 사용할 수 있습니다.

(위의 Pandas와 결과 같음)

## Format: feather
특히 Pandas를 위해 데이터를 feather (이진) 형식으로 저장하는 것이 일반적입니다. 데이터 세트의 읽기 속도를 크게 향상시킵니다.

![image](https://user-images.githubusercontent.com/49221790/102684950-55c08880-4220-11eb-831d-1cb8b99cee3d.png)

단순히 파일을 이진형식으로 저장함으로써 속도가 매우 빨라졌다.

## Format: hdf5
HDF5는 크고 복잡한 데이터를 저장, 관리 및 처리하기위한 고성능 데이터 관리 제품군입니다.

![image](https://user-images.githubusercontent.com/49221790/102685017-b9e34c80-4220-11eb-8951-5c3250b78a31.png)

## Format: jay
Datatable은 .jay (이진) 형식을 사용하여 데이터 세트를 빠르게 읽을 수 있습니다. 여기에서 공유되는 예제 노트북이 아래에 표시되어 있으며 1 초 이내에 전체 데이터 세트를 읽습니다!

![image](https://user-images.githubusercontent.com/49221790/102685088-4857ce00-4221-11eb-8668-581f9be2e803.png)

## Format: parquet
Hadoop 에코 시스템에서 parquet은 테이블 형식 데이터 세트의 기본 파일 형식으로 널리 사용되었으며 이제 Spark에서 광범위하게 사용됩니다. 수년에 걸쳐 더 유용하고 효율적이되었으며 팬더에서도 지원됩니다.

![image](https://user-images.githubusercontent.com/49221790/102685106-6ae9e700-4221-11eb-8f32-b981d400b85d.png)

## Format: pickle
Python 객체는 pickle 파일의 형태로 저장할 수 있으며 pandas에는 데이터 프레임을 pickle 객체로 읽고 쓰는 기능이 내장되어 있습니다.

![image](https://user-images.githubusercontent.com/49221790/102685246-ab963000-4222-11eb-922c-744cc364ba28.png)

압축할 때 pickle을 쓴다고 배운 것 같은데..


------------------------------------------------------


Each method has it's own set of pros and cons. Some examples are:   
* **Pandas** requires a lot more RAM to handle large datasets.
* **Dask** can be slow at times especially with transformations that cannot be parallelized.
* **Datatable** doesn't have a very exhaustive set of data processing functions.
* **Rapids** is not useful if you don't have a GPU.

So it's a good idea to explore various options and finally choose whichever appropriately fits the requirements. I strongly believe in not marrying a technology and continuously adapting to newer ideas, better approaches and ultimately the best possible solutions for building data science pipelines.

Even in my personal experience I've found different approaches working well on different datasets. So don't shy away from experimentation.

> Data Science is blooming under the blessings of open source packages and communities

각 방법에는 고유 한 장단점이 있습니다. 몇 가지 예는 다음과 같습니다.

Pandas는 대규모 데이터 세트를 처리하기 위해 더 많은 RAM이 필요합니다.
Dask는 특히 병렬화 할 수없는 변환의 경우 느려질 수 있습니다.
Datatable에는 매우 철저한 데이터 처리 기능 세트가 없습니다.
GPU가 없으면 Rapids는 유용하지 않습니다.
따라서 다양한 옵션을 탐색하고 마지막으로 요구 사항에 적합한 것을 선택하는 것이 좋습니다. 저는 기술과 결합하지 않고 새로운 아이디어, 더 나은 접근 방식 및 궁극적으로 데이터 과학 파이프 라인을 구축하기위한 최상의 솔루션에 지속적으로 적응한다고 굳게 믿습니다.

제 개인적인 경험에서도 다양한 데이터 세트에서 다른 접근 방식이 잘 작동하는 것을 발견했습니다. 따라서 실험을 주저하지 마십시오.

데이터 과학은 오픈 소스 패키지 및 커뮤니티의 축복 아래 꽃을 피우고 있습니다.

--------------------------------------------

이번 경우에는 Pandas로는 어려울 것 같고, Datatable을 사용해야될 것 같아 찾아봤는데  
Pandas에서 통계량 값을 뽑을 때 메모리를 소비하지만 Datatable은 소비하지 않는다고 한다.  
단순히 이런 점만 봤을 때는 Pandas보다 Datatable이 더 좋아보이는데, 실제 기능은 아직 Pandas보다 떨어진다고 한다. 

다음번엔 시계열 API에 대해서 알아보자..
