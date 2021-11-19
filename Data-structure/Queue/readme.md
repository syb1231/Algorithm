# Queue
## 1. Queue란 무엇인가?

* 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
  * FIFO(First-In, First-Out)  또는 LILO(Last-In, Last-Out) 정책의 구조를 사용하며, 스택과 꺼내는 순서가 반대
  * ex) 실생활 에서는 음식점의 서비스를 기다리는 손님들의 대기열이 이에 해당함
* 

* 큐의 구조

* 실제 응용 분야
  1) 여러 소비자가 리소스를 공유하는 경우. 예로는 CPU 스케줄링 , 디스크 스케줄링이 있습니다. 
  2) 두 프로세스 사이에서 데이터가 비동기적으로 전송되는 경우(데이터가 전송되는 것과 동일한 속도로 수신될 필요는 없음). 예에는 IO 버퍼, 파이프, 파일 IO 등이 포함됩니다. 
  3) 운영 체제에서:
       a) 세마포어
       b) FCFS(선착순) 스케줄링, 예: FIFO 대기열
       c) 프린터에서 스풀링
       d) 키보드와 같은 장치용 버퍼
  4) 네트워크:
       a) 라우터/스위치의  대기열
       b) 메일 대기열
## 2 Queue의 변형
* Deque, Priority Queue, Doubly Ended Priority Queue
## 3. 알아둘 용어 
## 4. 빅(o)
## 5. 파이썬에서의 큐 메서드와 사용법 (코드블럭)
## 6. 실제 응용 분야의 구현 (LRU Cache implement)
* LRU Cache implement 파일 참조
## 
** ref: https://www.geeksforgeeks.org/queue-data-structure/
** https://introcs.cs.princeton.edu/java/43stack/
