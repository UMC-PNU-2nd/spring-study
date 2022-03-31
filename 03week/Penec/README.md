### 서브 도메인

👉 컴퓨터가 아닌 핸드폰으로 네이버를 접속하게 되면 도메인이 `https://m.naver.com` 이다.

이것이 바로 서브 도메인이다!

- 보조 도메인으로, URL을 전송하거나 IP주소, 디렉토리로 포워딩 되는 도메인 이름의 확장자

👉 쉽게 예를 들면, `www.jcwebs.org/abc` 라는 URL을 기억하기 쉽게, 접근하기 쉽게 하기위해

`abc.jcwebs.org` 라는 도메인으로 접속할 수 있게 한다.

**이는, abc라는 서브 도메인을 만든 것이다!**

마찬가지로, `https://cafe.naver.com` / `https://blog.naver.com` 이러한 도메인은 모두 cafe, blog라는 서브 도메인을 만들어서 사용하는 것이다!

### Redirection

- 접속 시 IP는 도메인으로 연결되고, http는 데이터를 주고 받기위해 보안성을 추가한 https로 연결된다.

👉 Redirection 처리가 된 것이다!

ex) http가 들어온다면 https로 보내는 것

ex) IP가 들어오면 도메인으로 보내는 것

---

### 1. 리눅스에 nginx, php, mysql 설치하기

- nginx : apache와 같은 웹서버!

1. `sudo apt update`  : apt 업데이트

1. `sudo apt install nginx` : nginx 설치
    - 설치가 되었는지 확인하려면 `nginx -v` 로 확인 (버전이 뜨면 설치완료된 것)

1. `sudo apt install mysql-server` : mysql 설치
    - `sudo mysql_secure_installation` : mysql 보안 설정 하기
        - 패스워드 설정 후 나머지는 Y, ‘Disallow root login remotely?’ 는 외부 접속을 위해 N
        - 설치가 되면 `sudo mysql -u root -p` 로 mysql에 접속할 수 있다.
        
2. `sudo apt install php-fpm php-mysql` : php 설치
    - 설치가 되었는지 확인하려면 `php -v` 로 확인 (버전이 뜨면 설치완료된 것)

👉 ip로 웹에 접속해보면 Welcome to nginx! 페이지가 뜨게 된다!

![image](https://user-images.githubusercontent.com/95729738/161045775-37a28aa5-6ede-4d6c-88be-d0bbe0f23b25.png)

### 2. nginx와 php 연동하기

- phpinfo 화면 띄우기
1. nginx의 기본 경로는 `/var/www/html` 이므로 cd로 이 경로로 이동
2. `sudo vi phpinfo.php` : phpinfo.php 파일 생성 후 `<?php phpinfo(); ?>` 코드 작성
3. nginx와 php를 연동시키기 위해 nginx의 기본 설정 경로인 `/etc/nginx/sites-available` 로 이동
4. `sudo vi default` 로 default 파일을 열면 서버 설정 블록이 나온다.
    - index 부분 :  접속했을 때 처음 나오는 화면 파일
    - root 부분 :  화면 파일들의 경로
5. PHP 부분의 주석을 화면과 같이 해제해준다.
    - fastcgi_pass 부분의 php 버전을 설치한 php 버전으로 바꿔준다. (7.2.24 버전 → 7.2로 적기)

![image](https://user-images.githubusercontent.com/95729738/161045817-dec8c02e-574b-4d4b-96f1-8f479622c63e.png)

6. `/etc/nginx` 로 이동
7. `sudo vi nginx.conf` 로 nginx.conf 파일 열어서 `server_names_hash_bucket_size 64;` 부분 주석 해제하기

![image](https://user-images.githubusercontent.com/95729738/161045857-181cde2d-778f-497b-94d5-9a4da649ed75.png)

※ nginx의 설정파일을 변경하면 반드시 테스트를 하고 restart를 해야한다!

- 테스트 : `sudo nginx -t` 로, successful이 뜨면 성공이다.
- restart : `sudo service nginx restart`

👉 웹페이지에서 `ip/phpinfo.php` 로 접속하면 phpinfo가 잘 뜬다!

### 3. 도메인 구입하여 적용하기

- 가비아에서 도메인 구입 후 DNS 관리 툴에서 레코드 수정 → 호스트 `@` 과 `www` 로 추가 후 IP 주소 입력, TTL은 3600으로

👉 `@` 은 www를 입력하지 않아도 연결된 ip로 바로 보내준다.

ex) www.naver.com이 아니라 naver.com으로 입력해도 네이버로 들어가진다.

### 4. 서브 도메인 적용하기

- DEV 개발 서버와 PROD 실제 배포 서버로 나누어서 적용
- 도메인의 DNS 레코드 수정에서 레코드 추가
    - 타입 : CNAME / 호스트 : dev, prod /  값,위치 : 도메인 이름. (ex : kshhh.shop.) .을 붙여야 연결이 된다! / TTL : 3600

**이제 도메인과 서버를 연결하려면 서버 설정 파일에서 server name을 추가해줘야 한다!**

1. `/etc/nginx/sites-available` 에서 `sudo vi default` 으로 설정 파일 열기
2. server name 부분에 연결할 url(도메인) 입력

![image](https://user-images.githubusercontent.com/95729738/161045899-d711466a-203d-4599-90d5-015d429de153.png)

3. `sudo nginx -t` 로 테스트 후, `sudo service nginx restart` 로 리스타트

👉 실제 도메인 잘 적용된다!

**서브 도메인 연결하여 각각 다른 페이지 띄워보기**

1. `sudo mkdir dev` / `sudo mkdir prod` : 다른 페이지를 띄워야하므로 nginx 기본 경로(`/var/www/html`)에 dev와 prod 폴더 만들기
2. `cd dev` / `sudo vi index.html` : dev로 이동해서 index.html 만들기 
3. index.html에 `<h1>It Works! dev</h1>` 만들기
4. prod에서도 똑같이 2,3번 진행
5. nginx의 설정파일 경로(`etc/nginx/sites-available`)로 가서 default 파일 열기
6. 아래 사진과 같은 양식으로 도메인, 경로만 바꿔서 server 블록 만들기

![image](https://user-images.githubusercontent.com/95729738/161045934-ae03012e-340b-423d-b55a-38dc5066b270.png)

```java
server {
				listen 80;
				listen [::]:80;  
				server_name dev.kshhh.shop;
			
		    root /var/www/html/dev;
		    index index.html;
		
		    location / {
		            try_files $uri $uri/ =404;
		    }
}

server {
				listen 80;
				listen [::]:80;  
				server_name prod.kshhh.shop;
			
		    root /var/www/html/prod;
		    index index.html;
		
		    location / {
		            try_files $uri $uri/ =404;
		    }
}
```

7. nginx 테스트 후 리스타트

👉 이제 서브도메인인 `dev.kshhh.shop` / `prod.kshhh.shop` 으로 접속해보면 index.html에 입력한 코드들이 잘 작동된다.

### 5. 리다이렉션 적용하기

: IP로 접속했을 때 도메인으로 들어가게 하기!

1. 리다이렉션도 nginx 설정 파일에서 서버 블록 하나만 추가해주면 된다.
    - nginx의 서버 설정파일 경로(`/etc/nginx/sites-available`) 로 들어가서 default 파일 열기
    
    👉 redirection용 서버 블록을 만들고 server_name에는 ip 주소, return 에는 301 도메인$request_uri를 리턴한다.
    
    ```java
    server {
    				listen 80;
    				server_name 13.124.245.169;
    				return 301 http://kshhh.shop$request_uri;
    }
    ```
    
     이렇게 추가하기!
    
2. nginx 테스트 후 리스타트
3. IP 주소로 접속하면 도메인으로 들어가는 것을 확인할 수 있다!

---

### 3주차 Challenge 과제

- HTTPS 도메인과 서브도메인에 적용하기
    - 검색 키워드 : ec2 ubuntu 1804 Let’s Encrypt
    - https를 도메인, 서브 도메인에 적용하고 리다이렉션도 https로 연결되게 하기!

### Let’s Encrypt

: 무료 SSL / TLS 인증서를 얻고 설치할 수 있는 인증 기관이다.

- Certbot이라는 자동화 클라이언트 제공해서 Apache / Nginx에서 인증서 획득, 설치하는 프로세스 자동으로 가능
- 이러한 Certbot을 사용하여 Nginx용 무료 SSL 인증서를 받고 자동으로 갱신하도록 설정
- Nginx의 기본 설정 파일인 default 파일 대신 별도의 Nginx 서버 블록 파일을 사용하여 구축

👉 이는 일반적인 실수를 방지하고, default 파일을 예외 처리 파일로 유지할 수 있으므로 도메인마다 새로운 Nginx 서버 블록 파일을 만드는 것을 권장한다!

### 서버 블록 설정하기

: 블로그 참고!

### Certbot 설치

: apt에서 제공하는 Certbot 패키지는 조금 오래된 버전이기 때문에 최신 버전이 있는Certbot 레포지토리를 가져와서 그 레포지토리에서 설치한다.

`sudo add-apt-repository ppa:certbot/certbot` : 레포지토리 추가

`sudo apt install python-certbot-nginx` : Certbot 설치

### SSL 인증서 가져오기

: 블로그 참고

**※ Let’s Encrypt의 인증서는 설치 완료 이후 90일 동안 유효하다!**

👉 90일이 지나기 전에 certbot을 다시 실행해서 인증서를 갱신해야한다!

### SSL 인증서 90일 전에 자동 갱신

: certbot의 패키지를 설치해서 만료일까지 30일 이내의 모든 인증서를 갱신시킬 수 있다.

`sudo certbot renew --dry-run` : 명령어 실행하면 SSL 인증서 자동 갱신 설정을 할 수 있다.

만약, 자동 갱신 프로세스가 실패하면 등록한 이메일로 경고 메세지가 올 것이다.

**※ SSL 인증서 수동 갱신 : `sudo certbot renew`**

### 참고 블로그

[HTTPS Let's Encrypt 설정하기(EC2에 설정하기)](https://www.sunny-son.space/AWS/HTTPS%20%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0/)

---

### 처음 트러블

- ip/phpinfo.php 를 입력했는데 빈 화면이 출력됨

👉 default 파일 설정에서 주석 해제를 하나 안해서 발생한 문제

- default 파일 대신 별도의 서버 블록 파일을 만들고 nginx 테스트를 했을 때 기존 default 파일의 도메인과 이름이 같아서? 충돌이 발생했다.

👉 따라서, 기존 default 파일의 server_name 부분을 `server_name _;` 으로 바꾸고 진행

👉 계속 진행했는데 502 bad gateway 오류 해결 방법을 못 찾아서 그냥 서버 블록 파일을 따로 만들지 않고 default 설정 파일에 추가하는 방식으로 했다.

### 참고 블로그

[2-6 AWS에 Let's Encrypt로 HTTPS 적용하기](https://luminitworld.tistory.com/85)

- 블로그의 진행대로 했는데 도메인에 제대로 들어가지지 않았다.

도메인이 잘 작동하는지 테스트하는 페이지에서 오류가 발생했다.

[SSL Server Test](https://www.ssllabs.com/ssltest)

👉 SSL이 사용하는 HTTPS에 대한 포트 포워딩을 안 해주었기 때문에 오류 발생! 

HTTPS의 포트번호는 443번으로, AWS 보안 설정으로 들어가서 443에 대한 포트를 열어줘야 한다!

(인바운드 규칙 추가)

![image](https://user-images.githubusercontent.com/95729738/161046001-f324e1ef-13fb-46f2-86e6-3a4c356241a7.png)
