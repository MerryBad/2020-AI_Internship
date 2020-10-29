# Supervisely 요구사항
Linux OS Kernel 3.10  
Docker Version 18.0  
GPU CUDA 9.0  
NVIDIA-Docker Version 2.0

-------
VMware Workstation 16 Player\
우분투 20.04

-------
리눅스 커널 버전 확인\
![우분투 리눅스버전](https://user-images.githubusercontent.com/49221790/97604226-9980e800-1a50-11eb-8108-ffcc98f30c39.PNG)

-------
Docker 설치\
에러 발생\
![우분투 도커 서버 에러](https://user-images.githubusercontent.com/49221790/97604356-b9181080-1a50-11eb-8d42-3697070c8bad.PNG)

해결방법 참고 \
https://github.com/occidere/TIL/issues/116#issue-509567575 \

에러 해결 \
![우분투 도커 서버 해결](https://user-images.githubusercontent.com/49221790/97604368-c03f1e80-1a50-11eb-99b7-743c612fb74c.PNG)

-------
GPU 확인 \
sudo update-pciids \
sudo lspci -v | less \
\VGA
![리눅스 GPU 확인안댐](https://user-images.githubusercontent.com/49221790/97604389-c634ff80-1a50-11eb-91dd-0cff64376286.PNG)

호스트 컴퓨터의 그래픽카드 식별 안됨\
autoinstall, apt-get도 안 된다..
