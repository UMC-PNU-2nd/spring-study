# 2주차 - 포트포워딩과   AWS

# Port Forwarding (포트포워딩)


> **포트포워딩?**
외부 IP를 통해 접속한 client가 특정 port를 통해 request를 하면 내부 IP로 보내 처리함
(local에 구축된 서버에 접속하기 위해서 하는 작업)
> 

ex) 공유기에 길을 만들어주고, 이정표를 달아주는 작업

- 외부 IP : 공유기의 네트워크 주소
- 단말기 : 공유기에 연결되면 동일한 외부 IP가짐
- 내부 IP : 단말기끼리 구분하기 위해 사용함
- 이정표 : 외부IP 80번으로 들어가면, 내부IP 80번으로 접속해라

<aside>
💡 **사전지식** 

- Protocol (프로토콜) - http
- IP & Port
- 도메인
</aside>

## Protocol(프로토콜)

> **프로토콜?** 
각각의 컴퓨터가 통신하는 방식
> 

### Protocol 종류

- **http : 서버와 클라이언트가 데이터를 주고 받기 위한 프로토콜**
- https : http + secure(보안 )
- mysql :
- ssh : 네트워크에 다른 컴퓨터로 로그인, 원격시스템에서 사용함
- ftp : 파일 전송 프로토콜
- sftp : secure(보안) + ftp

### http의 구성

packet(데이터형식) = header + body

## IP & Port

> **IP?**
 인터넷상의 위치 표시
> 

ex) 도로명 주소(도메인) → 위도,경도(IP)

 www.naver.com → 223.130.200.104

> **Port?**
 IP에 접근하기 위한 통로
> 

ex) 매장을 들어가는 문 (포트)

### 각 프로토콜의 포트번호

- http: 80 → default
- https: 443
- ssh : 22
- ftp : 21
- sftp : 22
- myssql :3306

포트번호 22번이 중복되는 이유? sftp는 ssh의 부가기능이기 때문

---

# 포트포워딩 실습

<aside>
💡 **과정**

1. 공유기 주소로 접속 → 로그인
2. 포트포워딩 설정 → 내부 IP주소, 포트번호(아파치)설정

</aside>

---

# AWS(Amazon Web Service) - EC2

> **EC2?**
AWS에서 제공하는 클라우드 컴퓨팅 서비스
> 

## EC2 특징

- 내 컴퓨터에서 서버를 돌리기 부담스러울 때 사용함
- 서버 구축시, 포트 포워딩 같은 환경설정 과정을 없애줌
- 서비스가 안정적임
- 프리티어 - 1년 무료 사용 권한

---

# AWS -EC2 실습

<aside>
💡 **EC2 인스턴스 생성과정**
1. AWS에서 프리티어로 계정 생성 - 지역 변경
2. AMI(Amazon Machine Image) 선택 
3. 인스턴스 유형 선택
4. 스토리지 추가 - 30GB(프리티어 최대)
5. 보안 그룹 구성 - ssh를 내IP로 설정
6. 인스턴스 시작 - 키 페어 생성(인스턴스 접속용)

</aside>

주의) 인스턴스 2개 이상 생성시 과금 발생 우려!

월 750시간 초과 - 과금 발생함 (인스턴스 1개만 운영하면 괜찮다)

### 보안그룹 규칙

- 인바운드 규칙 - 서버에서 접속할 때의 규칙 →중요
- 아웃바운드 규칙 - 서버에서 데이터가 나갈 때의 규칙(관리하지 않아도 된다)

### 퍼블릭 IP주소

- 유동 IP → 탄력적 IP

### PEM

다운받은 키페어의 확장자 이름 .pem

# 인스턴스 연결1 - MAC

1. 다운받아놓은 키페어(.pem)이 있는 곳으로 cd 명령어를 통해 이동
2. ssh -i "udemy_server.pem" [ubuntu@ec2-3-36-173-82.ap-northeast-2.compute.amazonaws.com](mailto:ubuntu@ec2-3-36-173-82.ap-northeast-2.compute.amazonaws.com) 입력
3. ssh로 처음 접속을 할 때, 아래와 같이 신뢰할 수 있는지 물어봄 (출처: [https://blueyikim.tistory.com/1792](https://blueyikim.tistory.com/1792))
⇒ yes
4. 연결 완료


# 인스턴스 연결2 - Window

1. winscp 사용 - 호스트 이름: 3.36.173.82

## AWS 실습 의문점

[강의 중 의문점 정리](https://www.notion.so/33bb98d2034742aeba0fa85305744ae2)