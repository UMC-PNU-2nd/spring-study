

## Protocol

: 클라이언트가 서버에게 요청을 하는 방식 (통신 규약)

- 종류
    - http : 서버와 클라이언트가 인터넷 상에서 데이터를 주고 받기 위한 프로토콜
    - https : http에서 보안 기능이 들어간 프로토콜
    - mysql : mysql 사용 시 클라이언트와 서버의 통신 프로토콜
    - ssh : 네트워크 상의 다른 컴퓨터에 로그인하거나 원격 시스템에서 사용하는 프로토콜
    - ftp : 파일 전송 프로토콜
    - sftp : ftp에서 보안 기능이 들어간 프로토콜 (보안이 중요한 파일을 전송할 때 사용)

**프로토콜마다 주고 받는 데이터 형식이 다르다!**

- http : `packet` 이라는 데이터 형식을 사용! packet은 header와 body로 이루어져 있다.

---

### IP & Port

ex) 어떤 장소를 찾아갈 때

1. 도로명 주소를 찾아 간다. 

도로명 주소 → 위도, 경도를 알기 쉽게 표현한 것

이때 `IP` : 위도, 경도

`도메인` : 도로명 주소

 ex) 223.130.200.104 → www.naver.com

1. 장소를 찾았으면 문을 열어야 하는데, 고객용 문과 직원용 문이 분리되어 있다.

이때, 문을 Port라고 한다.

Port마다 번호가 있고, 알맞는 Port 번호를 통해 장소에 진입해야한다.

Port 관리는 서버 관리자가 수행한다.

이때, 프로토콜에 따라서 Port 번호가 관례적으로 정해져있다.

관례적으로 정해져 있는 것이기 때문에 임의로 바꿀 수도 있다.

- http : `80`
- https : `443`
- ssh : `22`
- ftp : `21`
- sftp : `22`
- mysql : `3306`

이때, ssh와 sftp의 Port번호가 같은 이유는 sftp가 ssh에 있는 부가적인 기능이기 떄문이다.

sftp : ssh의 파일 전송 기능

### 클라이언트가 요청(Request) 시 필요한 정보

- 서버와 어떤 프로토콜으로 통신을 할지?
- 어떤 ip 주소로 보내야하는지?
- 어떤 Port 번호로 보내야하는지?

---

## 포트 포워딩(Port Forwarding)

: 외부 IP를 통해 접속한 클라이언트가 특정 포트를 통해 요청을 하면 내부 IP로 보내서 처리를 하는 것이다.

- 현재 내 노트북에 구축된 서버로 다른 사람이 접근할 수 없는데, 이때 포트 포워딩을 사용하면 다른 사람이 접근할 수 있다!

EX) 공유기에는 핸드폰, 노트북, TV 등이 연결되어 있다.

- 공유기에 길을 만들고 이정표를 달아주는 것 : 포트 포워딩

외부 IP : 공유기가 가지고 있는 네트워크 주소

휴대폰, 노트북, TV는 동일한 외부 IP를 가지고 있다.

내부 IP는 공유기에 연결된 클라이언트들이 서로를 식별하기 위해 가지는 IP이다.

👉 이때 포트 포워딩은 `외부IP:80` 으로 접속하면 `내부IP:80` 으로 접속하게 해서 외부에서 접속했지만 내부에서 접속한 것처럼 접속이 되게 하는 것을 말한다.

---

### AWS (Amazon web service) ec2 - AWS에서 제공하는 클라우드 컴퓨팅 서비스

- 내 컴퓨터에서 서버를 구동하기 부담스러울 때 사용
- 매번 서버 구축 시 포트 포워딩 등의 환경설정을 직접 하는 번거로움을 덜어준다.
- 서비스가 매우 안정적이다.

## AWS 실습

### 1. 인스턴스 생성

1. Amazon Machine Image(AMI) 선택 : 운영체제
2. 인스턴스 유형 선택 : 프리티어에서 사용 가능한 인스턴스 유형 선택
3. 인스턴스 시작 검토에서 스토리지 수정 : 프리티어의 최대 크기인 30GB로 변경
4. 보안 구성 : SSH - 내 IP로 지정 (이후에 수정)
5. 시작 후 키페어 생성
    1. 키 페어 : 인스턴스 접속을 위해 사용되는 PW 같은 느낌으로 잃어버리면 안 된다.
6. 인스턴스 시작

### 2. 인스턴스 보안 그룹 수정

: 보안 그룹의 종류에는 인바운드 규칙 / 아웃바운드 규칙이 있다.

- 인바운드 규칙 : 서버로 접속할 때의 규칙
- 아웃바운드 규칙 :  서버에서 데이터가 나갈 때의 규칙

👉 서버에서 데이터가 나갈 때는 우리가 관리하지 않아도 되므로 인바운드만 수정

1. 인바운드 규칙 편집 (현재 SSH는 사용자 IP만 접속할 수 있도록 설정해놓음)

👉 SSH는 원격 접속을 하는 서버 관리자용 문이므로 내 IP만 허용

1. HTTP 규칙 모든 사람이 들어올 수 있도록 허용하기

👉 HTTP 2개를 추가하고 각각 소스에 Anywhere-IPv4, Anywhere-IPv6 추가

### 3. 탄력적 IP 설정

: 퍼블릭 IP 주소는 고정 IP가 아니라 유동 IP라서 인스턴스를 중지하고 다시 실행하면 IP가 변하게 된다.

따라서, 탄력적 IP를 할당받아서 고정 IP주소를 사용한다.

1. 탄력적 IP 탭에서 탄력적 IP 할당받기!
2. 할당 받은 후 인스턴스와 탄력적 IP 주소 연결하기!

### 4. 인스턴스에 연결하기 (Windows)

: window는 Mac과 다르게 터미널에서 ssh 클라이언트가 지원되지 않아서 ssh 클라이언트를 별도로 설치해줘야 한다.

`WinSCP` 프로그램 사용

1. WinSCP의 새로운 세션 → 새 사이트에 호스트이름에 IP주소 입력, 파일 프로토콜은 SFTP, 포트번호는 22로 설정, 사용자 이름은 EC2 연결 페이지에 있는 사용자 이름 입력(Default : ubuntu)
2. 고급 → SSH → 인증 탭에서 저장했던 Keypair 파일 불러오기
3. 세션 저장 → 다음에 세션 저장에서 이름 설정
4. 로그인

👉 내 인스턴스 EC2 컴퓨터에 접속 완료

- WinSCP에서 서버 관리 시 터미널과 같은 역할을 하는 PuTTY라는 것을 실행해서 관리한다.
