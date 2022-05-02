### HTTP 통신

- 클라이언트가 서버에게 웹 페이지를 보여달라고 하는 것은 **요청!**
- 서버가 클라이언트의 요청을 받아서 웹 브라우저를 띄워주는 것은 **응답!**
- 클라이언트와 서버 사이에 요청과 응답이 오갈때 데이터가 존재하는데, 이 데이터는 **패킷!**
    - 패킷은 **헤더(Header)**와 **바디(Body)로 구성되어 있다.**
        - 택배 상자의 주소지가 붙어있는 송장 : 헤더 (데이터의 정보를 나타내는 메타 데이터)
        - 택배 상자 안의 물건 : 바디 (실제 데이터)

- 데이터를 주고 받는 방식 : **GET** / **POST** / **PUT** / **PATCH** / **DELETE → HTTP 메소드들**
    - GET : 조회 / POST : 생성 / PUT : 수정 / PATCH : 일부 수정 / DELETE : 삭제
    - GET 메소드 : 무언가를 조회할 때 사용
        - 클라이언트 : 어떤 정보를 조회할 것인지 서버에게 전달
        - 쿼리스트링 방식 : 주소 뒤에 전달할 데이터를 붙여서 서버에게 전달
    - POST 메소드 : 무언가를 생성할 때 사용 ( EX : 회원가입)
        - 사용하는 데이터 포맷 : XML / **JSON** → JSON 주로 사용
        
        👉 클라이언트와 서버가 데이터를 주고 받을 때 **JSON 형식**으로 주고받는다!
        
        ```java
        // JSON 타입 : Key / Value 형태
        {
        	"name" : "고양이",
        	"age" : 3,
          "weight" : 3.5
        }
        ```
        
        👉 데이터가 간단하고 가볍고 객체 단위 맵핑이 가능해서 유지 보수가 용이하다.
        
    - 많은 사람들의 착각 : GET, POST 메소드가 보안이 더 좋다!
    
    👉 GET과 POST 둘 다 서버에서 보내는 데이터를 클라이언트 측에서 볼 수 있으므로 보안을 생각한다면 둘 다 좋지 않고, 암호화 과정을 거쳐야한다.
    

---

### API : Application Programming Interface

- 클라이언트는 회원가입의 로직을 알 필요가 없고, 그 로직을 가지고 있는 서버에게 회원가입 API를 요청하면 된다.
- 중요한 점 : API 통신을 위해서는 서버와 클라이언트 간의 포맷이 통일돼야 한다.

→ 어떤 식으로 데이터를 보내고, 어떤 식으로 응답을 받을 지에 대한 약속 문서가 필요하다.

→ API 명세서 작성

![image](https://user-images.githubusercontent.com/95729738/166192644-fd53177c-594b-40f9-8f06-50d64dd14e4b.png)

👉 이렇게 API 명세서를 통해 포맷을 정했다고 해도, 누가 개발했는 지에 따라서 개발 스타일이 다르다.

따라서, 가독성이 떨어질 수 있는데 이에 개발자들은 ‘표준’을 만들어서 통일성을 유지하고자 했다.

👉 그 표준 중 하나가 **Restful**한 설계 방법

---

### Restful API

### 1. HTTP 메소드 : 동사 / URI : 명사 (URI에는 복수형을 쓴다)

- EX) 회원가입 API
    - 회원가입은 유저(데이터)를 생성하는 것이므로 POST 메소드 사용
    - URI에는 메소드 행위의 대상이 들어간다 → 회원가입 API에서 유저를 생성하는 POST 메소드 : 행위의 대상이 유저이므로 URI는 유저(USERS)
    - URI는 명사로, Create User가 아니라 USERS
    
- EX) 유저 조회 API
    - 유저 조회이므로 URI는 USERS
    - 조회하는 것이기 때문에 메소드는 GET 메소드 사용
    
    👉 이렇게 설계하면 모든 유저를 조회한다는 의미
    
    만약, 특정 유저만 조회해야하는 상황이라면?
    
    → 어떤 유저를 조회할 것인지 URI에 밝혀줘야 한다.
    
    - path variable : 쿼리스트링과 유사한 기능 → 특정 데이터를 가리키는 데에 사용
        - ex) 100번 유저 조회하고 싶을 때, `users/100` 이런 식으로 표현하는 방식
        
        → URI 명시, 클라이언트에 전달해줄 때는 `users/:userIdx` 이런 식으로 이 자리가 userIdx의 자리라는 것을 명시해줘야 한다.
        
    

### 쿼리 스트링 vs Path Variable

- 쿼리 스트링 : 검색, 필터링, 페이징에서 사용
    - 검색 : 검색 키워드를 쿼리스트링을 통해서 보내준다.
    - 필터링 : 성별이 여성인 유저를 조회하는 API의 URI 예시를 생각해보자.
        - URI 리소스 : 동일하게 users
        - 여성 조건 : `/users?gender=female`
    - 페이징 :
    

### 2. 명사와 명사의 구분자는 하이픈으로 (ex : blocked-users)

### 3. Get과 Delete에는 body 쓰지 않기

### 4. HTTP 메소드는 실제 DB에서 동작하는 기준으로 설정

- EX) 회원 탈퇴 API라고 하더라도, 실제 DB에서는 데이터가 삭제되는 것이 아니라 업데이트 되는 것이므로 회원 탈퇴 API에서 Delete 메소드가 아니라 Patch 메소드를 사용해야한다.

---

### 인스타그램 API 명세서 작성

### 1. 리소스가 users (인스타그램 유저 관련 기능)

- 회원가입 API
    - 회원을 생성하므로 POST 메소드
    - 유저를 생성하므로 URI는 /users
    
- 프로필 수정 API
    - 일부 정보만 수정하므로 PATCH 메소드
    - 행위의 주체(리소스)는 users
    - 특정 유저의 프로필을 수정해야하므로 path variable 사용
    - URI : /users/:userIdx
    
- 유저 피드 조회 API
    - 조회이므로 GET 메소드
    - 유저 리스트를 조회하는 것이 아니라 1명의 특정 유저를 조회하므로 path variable 사용
    - URI : /users/:userIdx
    
- 유저 삭제 API
    - 삭제이지만, DB에서 동작할 때 STATE 값을 변경하는 것을 삭제로 하기 때문에 결국 변경하는 것이므로 PATCH 메소드
    - 특정 유저를 삭제하므로 URI : /users/:userIdx
    

👉 여기서, 프로필 수정 API와 유저 삭제 API의 메소드와 URI가 동일한데, 이러면 문제가 발생한다.

이를 해결하기 위해서 유저 삭제 API를 구체화시킨다.

유저 삭제는 status를 수정하는 것이므로 status를 수정한다는 의미로 URI를 /users/:userIdx/status로 변경한다.

### 2. 리소스가 posts (인스타그램 게시물 관련 기능)

- 게시물 리스트 조회 API
    - 조회이므로 GET 메소드
    - URI는 리스트 조회이므로 특정 게시물을 명시할 필요가 없다.
    - URI : /posts

- 게시물 생성 API
    - 생성이므로 POST 메소드
    - URI : /posts

- 게시물 수정 API
    - 일부 수정이므로 PATCH
    - 특정 게시물을 수정하는 것이므로 path variable 사용
    - URI : posts/:postIdx

- 게시물 삭제 API
    - 삭제이지만, DB에서 동작할 때 STATE 값을 변경하는 것을 삭제로 하기 때문에 결국 변경하는 것이므로 PATCH 메소드
    - 특정 게시물을 수정하는 것이므로 path variable 사용, status 구체화
    - URI : posts/:postIdx/status
    

---

### 프레임워크 구조

### Route ↔ Controller ↔ Provider / Service ↔ Dao

→ 요청

← 응답

- Route
    - 클라이언트의 요청이 왔을 때 처음에 Route로 간다.
    - Routing 해주는 역할
        - 해당 요청을 받아서 그에 맞는 로직을 가진, 해당 URI와 맵핑된 컨트롤러로 요청 연결

- Controller
    - 요청을 받으면 Provider와 Service에게 전달
    - 전달을 해줄때, path variable, 쿼리스트링, body에 있는 데이터들을 가져와서 Provider와 Service의 파라미터 값으로 전달
    
- Provider/Service
    - 비즈니스 로직이 이루어진다.
    - transaction 처리
    - Provider VS Service
        - Provider : 조회에 해당하는 작업을 할 때 사용
        - Service : 조회 이외의 작업을 할 때 사용

- Dao
    - 실질적인 쿼리 작성과 실행이 이루어지는 곳
    - 쿼리 실행문을 실행한 결과를 Provider와 Service에 리턴
    

※ 클라이언트에게 전달되는 리턴 response는 JSON 형식이다.

### Validation (검증) : 형식적 Validation / 의미적 Validation

### ex) 회원가입 하는 상황

- 회원가입할 때 클라이언트에서 서버에게 POST 방식으로 Body에 이메일, ID, PW 등을 담아서 보낸다.
- 이때, 이메일을 입력하지 않고 보낸다면, 회원가입이 되지 않는데 이는 Validation(검증)을 거친것이다.

- 형식적 Validation : Controller에서 수행
    - 빈 값인지, 형식에 맞는지, 정해진 길이에 맞는지 등을 검증 (형식 검증)
    
- 의미적 Validation : Provider/Service에서 수행
    - DB를 거쳐야하는 검증
    - 똑같은 이메일로 여러 계정을 만들 수 없는 것처럼 이메일이 중복이 되는지와 같은 내용을 검증
