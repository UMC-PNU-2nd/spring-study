> ## 서버 : 무언가를 제공하는 것!

### 서버의 특징

1. 서버 : 클라이언트 → 1:N의 관계 (서버는 여러 클라이언트에게 서비스를 제공)
2. 서버는 상대적인 역할에 따른 관계! (서버가 클라이언트가 될 수 있음)

### 서버의 구성

1. 클라이언트(Web, 안드로이드, IOS, 게임)  
2. 서버(Apache, Ngnix : 웹서버)
3. 백엔드 언어(php, spring, node.js)
4. DB, DBMS (mySql, oracle, mongodb)

👉 서버는 서버 + 백엔드 언어 + DB로 구성되어 있다.

💡 정리하면, 서버는 클라이언트의 요청(`login.java`)을 받는데, 자바 언어파일이기 때문에 서버는 이해할 수 없어서 백엔드 언어에 전달한다. 백엔드 언어는 자바 파일을 이해해서 DB로 가서 자바 파일의 요청에 맞게 데이터를 가공 후 서버에 전달하고, 서버는 클라이언트에게 전달한다.

### APM : Apache(서버) + Php(백엔드 언어) + Mysql(DB)의 앞 글자를 합친 것!

### 비트나미 : 어플리케이션 솔루션들을 다양한 환경에 쉽게 설치할 수 있게 패키지를 만들어서 배포해주는 회사

[Install WAMP, Download WAMP](https://bitnami.com/stack/wamp/installer)

### 리눅스 : 운영체제 종류 중 하나

사용하는 이유 : 오픈소스 (무료)

서버에 유리한 운영체제

CLI(Command line Interface) 환경으로, CLI환경에 익숙해지는 것이 중요하다.

콘솔 환경을 말한다!

### 패키지 설치 VS 소스 설치

- 패키지 설치 : 패키지 단위로 설치하는 것으로, 설치가 간편하지만 통째로 설치하기 때문에 불필요하게 설치되는 파일들이 있고, 그 파일들이 시스템의 자원을 사용하기 때문에 성능이 좋지 않다. 또, 패키지 단위로 설치되므로 개별 관리 문제가 발생한다.

- 소스 설치 : 직접 수동으로 소스들을 다운받아서 설치하는 것을 말한다. 설치는 일일히 다 소스를 설치해야해서 불편하지만 관리가 편하고 필요한 파일들만 받을 수 있어서 시스템 자원 낭비가 없다.

[[Ubuntu] Ubuntu-20.04에 APM 소스 설치(수동 설치)하기 - 1 (Apache)](https://yeni-days.tistory.com/2)

소스 설치 관련 링크

### 소스 설치 과정

1. 소스파일 내려받기 
2. ./configure로 설정
3. make로 컴파일
4. make install으로 설치
 - ./configure ~~: 소스파일에 대한 환경설정 → 서버 환경에 맞춰 makefile 생성
 - make : 소스를 컴파일
 - make install : make로 컴파일한 설치파일을 설치 → build된 프로그램을 실행할 수 있게 알맞은 위치에 복사해준다

### 소스 파일 다운, 압축 해제 시 사용 명령어들

- mkdir : 디렉토리(폴더) 생성
- wget : 웹 서버로부터 파일 다운로드
- tar xvfz : tar.gz 파일 압축 풀기

### APR(Apache Portable Runtime)

: 아파치 HTTP서버의 휴대용 라이브러리로, 고급 IO 기능에 대한 접근을 포함해서 OS 수준의 기능(난수 생성, 시스템 상태),기본 프로세스 처리 등의 용도로 사용되고 있다.


<br>

---
> ## 가상머신 Ubuntu apm 소스 설치

### **mysql 소스 설치 시 오류**

make로 컴파일하는 과정이 3~4시간 걸려서 컴파일 후에 make install을 해야하는데 make install을 한 줄 알고 그 다음 과정을 실행해서 오류가 났다.

👉 make로 컴파일한 후에는 make install로 설치하기!

- mysql 서버 실행 시  ERROR 2002 : Cant connect to local Mysql server through socket ~ 오류
    
    : 구글링해서 여러 방법 다 시도해봤는데 실패했다.. (심볼릭 링크 생성, ... )
    
    : mysqld, mysqld_safe 프로세스가 실행중이었는데 이 프로세스들을 종료하니 잘 실행됐다.. (허무)
    
    아마 실행중이던 프로그램이 겹쳐서? 충돌이 일어난 것 같다,,
    
    확실히 CLI 환경에서는 처음 명령어를 칠 때 상당히 조심해서 쳐야겠다는 생각을 했다.
    
- mysql 비밀번호 설정 시 Error 1820 ..
    
    : ALTER USER를 사용하라는데 사용해서 친건데 오류가 발생했다..
    
    알고보니 오타였다.. `alter user 'root'@'localhost' ~` 였는데, `'root@localhost'` 이렇게 입력했었다.
    

<br>

### **php 오류**

- php 설치 후 `[http://127.0.1.1/phpinfo.php](http://127.0.1.1/phpinfo.php)` 에 접속을 했는데 찾을 수 없는 주소라고 나왔다.

알고보니, phpinfo.php가 아니라 pipinfo.php 파일을 만들었었다.

이름 변경을 하기 위해 구글링을 했더니 rename 명령어가 나왔는데 써보니 apt install rename으로 설치하여 사용할 수 있었다. 간단하게는 mv를 통해서 할 수 있었다.

### phpinfo 만들기 성공!
![phpinfo](https://user-images.githubusercontent.com/95729738/158929289-d234097f-2de5-48e1-982b-625cd49c40bb.png)

