### 7주차 강의 정리 : https://ksh-coding.tistory.com/24

## 7주차 추가 스터디
### 1. Proxy Server / Forward Proxy / Reverse Proxy : https://ksh-coding.tistory.com/25
### 2. @RequestMapping : https://ksh-coding.tistory.com/26
### 3. 동기(Sync) VS 비동기(ASync) 통신 : https://ksh-coding.tistory.com/27
### 4. @RequestBody / @ResponseBody : https://ksh-coding.tistory.com/28
### 5. JdbcTemplate 메소드 : https://ksh-coding.tistory.com/29

---
### 7주차 챌린지 과제 : 유저 삭제 API 구현
### UserController

```java
 /**
 * 유저 삭제 API
 * [PATCH] /users/:userIdx/status
 * @return BaseResponse<String>
 */

@ResponseBody
@PatchMapping("/{userIdx}/status") // (PATCH) 127.0.0.1:9000/users/:userIdx/status
public BaseResponse<String> deleteUser(@PathVariable("userIdx") int userIdx){
    try {
        DeleteUserReq deleteUserReq = new DeleteUserReq(userIdx);
        userService.deleteUser(deleteUserReq);

        String result = "";
        return new BaseResponse<>(result);
    } catch (BaseException exception) {
        return new BaseResponse<>(exception.getStatus());
    }
}
```

### UserService

```java
public void deleteUser(DeleteUserReq deleteUserReq) throws BaseException {
    try{
        int result = userDao.deleteUser(deleteUserReq);
        if(result == 0){
            throw new BaseException(DELETE_USER_FAIL);
        }
    } catch(Exception exception){
        throw new BaseException(DATABASE_ERROR);
    }
}
```

### UserDao

```java
public int deleteUser(DeleteUserReq deleteUserReq){
        String deleteUserQuery = "update User set status = 'DELETED' where userIdx = ? ";
        int deleteUserParams = deleteUserReq.getUserIdx();

        return this.jdbcTemplate.update(deleteUserQuery,deleteUserParams);
    }
```

### BaseResponseStatus

```java
// isSuccess : false / code : 4016 / message : "유저 삭제 실패"
DELETE_USER_FAIL(false, 4016, "유저 삭제 실패");
```

### 로컬 Postman

![image](https://user-images.githubusercontent.com/95729738/166855468-10e03adb-8d83-475e-9424-579e81d07561.png)

### 로컬 수정된 DB

![image](https://user-images.githubusercontent.com/95729738/166855472-c6c8f7f3-9b64-4666-afae-3cea70576a84.png)

### EC2 서버 배포 Postman
![image](https://user-images.githubusercontent.com/95729738/166855528-6d85df50-b4b9-40be-949d-d7a10966ceb8.png)

### EC2 서버 배포 후 DB
![image](https://user-images.githubusercontent.com/95729738/166855544-7193ee0d-d2dc-46c3-a956-7b81894754e3.png)

---
## 트러블 슈팅

### 1. build와 java는 실행이 되는데, URL을 넣었을 때 DB 연결이 실패했다.
![image](https://user-images.githubusercontent.com/95729738/166855629-4d511ebc-3c8e-4947-8584-f28d1d54c74a.png)

1. url 부분에 RDS 엔드포인트를 적고 그 뒤에 /스키마 이름을 적어야하는데 적지 않고 계속 했었다.

![image](https://user-images.githubusercontent.com/95729738/166855636-431cd40b-7ddc-4436-9e04-e1bf56a48b0c.png)

![image](https://user-images.githubusercontent.com/95729738/166855659-ccfafed2-105e-400a-b1a8-229c06f224ce.png)

2. DB 부분에서 컬럼 명을 대문자로 시작하게 해야했다.
- 서버의 UserDao 단을 바꿔도 될 것 같았지만 그냥 DB 컬럼명을 바꿨다.
- user → User로 바꿨더니 동작했다.


![image](https://user-images.githubusercontent.com/95729738/166855740-6efa2148-a349-4e64-96f3-d8f874c87bd9.png)

### 2. 유저 삭제 API를 추가한 파일을 git clone 말고 winSCP GUI 환경에서 로컬 -> 서버로 폴더를 옮겼더니 winSCP 권한 오류가 발생했다.
- /etc/ssh/sshd_config 파일 수정
- sudo chown ubuntu:ubuntu /var/www -R을 통해 폴더 권한 주기
- 이 2가지를 통해 해결했다.
- 참고한 블로그 : [https://choidr.tistory.com/entry/WinSCP-SFTP-Permission-Denied-ErrorAWS](https://choidr.tistory.com/entry/WinSCP-SFTP-Permission-Denied-ErrorAWS)

- 또, gradlew build 시 permission denided가 발생했다.
  - 권한 주는 명령어인 chmod를 사용하여 `chmod +x gradlew`를 사용하여 해결했다.

### 3. 서버 배포 후 프록시 패스를 한 상황인데 포트없이 하면 405 에러가 발생했다.
![image](https://user-images.githubusercontent.com/95729738/166856000-dff4df07-d61c-416e-b5df-7f6e3a8675bc.png)

* 해결하지 못했다..

---
### 궁금한 점
* 프록시 패스 정확하게 뭔지?
* BaseResponse 클래스 이해 X
