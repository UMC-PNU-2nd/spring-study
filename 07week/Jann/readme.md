# 7주차

## 요약

## 이슈
- [AWS] EC2 프리티어 메모리 이슈  
[https://suakang17.github.io/devlife/2022-04-26-AWS-memory-issue/](https://suakang17.github.io/devlife/2022-04-26-AWS-memory-issue/)

- spring boot MYSQL 연동 이슈
    - application.yml이 url설정 전으로 계속 초기화되었었음 (url: # 수정해주세요 username: (공백) pw:(공백) 의 형식으로 파일이 되돌아갔음.)
    - 알고 보니 정말 별 거 아니었던 이슈
    - 원인은 1. 잘못된 경로의 application.yml수정 2. 헷갈리게 지어둔 db 이름 
        - 1. src폴더가 아닌 build 통해 생성된 파일을 수정했음 ~~정말 어이없음~~
        - 2. application.yml의 url 끝에 db이름을 붙여야하는데 인스턴스명과 동일하게 해둔줄 알았는데 mysql이라고 이름지어둔 바람에 이름 찾느라 한참 헤맴 ~~정말 많이 어이없음~~
        
- postman 응답코드 4000 (db연결 오류) 이슈 (미해결)