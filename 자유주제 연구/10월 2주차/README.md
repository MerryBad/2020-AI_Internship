# Supervisely 요구사항
Linux OS Kernel 3.10  
Docker Version 18.0  
GPU CUDA 9.0  
NVIDIA-Docker Version 2.0

-------
VMware Workstation 16 Player\
우분투 20.04\

-------
리눅스 커널 버전 확인\
(캡쳐 넣기)\

-------
Docker Version 설치\
(캡쳐 넣기)\
에러 발생\
(캡쳐 넣기)\
해결방법 참고 \
https://github.com/occidere/TIL/issues/116#issue-509567575
에러 해결 \
(캡쳐 넣기)\

-------
GPU 확인 \
sudo update-pciids
sudo lspci -v | less
\VGA
(캡쳐 넣기)\
호스트 컴퓨터의 그래픽카드 식별 안됨\
autoinstall, apt-get도 안됨..\

--------
결론 : VMware + 우분투 + nvidia(cuda)는 할 수가 없다..
