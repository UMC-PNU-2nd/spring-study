# 6주차

## 요약

- client -> server : request
- server -> client : response

	이 때, data가 오고가는데 이를 packet이라 함

- data의 구성 : header(목적성 가지는 metadata) + body(실 data) 
- data를 주고 받는 방식(http method)
	- Get: 조회시 사용
		- querystring: 주소 바로 뒤에 데이터 붙여 전달하는 방식으로 검색, 필터링, 페이징에서 사용
		- query: key/value 형식
	- Post: 생성시 사용
		- xml, json format
	- Put, Patch: 수정시 사용
	- Delete: 삭제시 사용

- API(Application Programming Interface)
	- Restful API
		1. method: 동사/ uri: 명사
			- ex. Post / users
				  Get / users > '특정 데이터' 조회시 path variable사용 > Get / users / 100 (100번 유저) 형태로 사용 가능
		2. 명사간의 구분자 == 하이픈
			- ex. blocked-users
		3. Get, Delete에는 body 쓰지 않기
		4. HTTP method는 실제 DB에서 동작하는 기준으로 설정하기

- framework 구조
	Route <-> Controller <-> Provider/Service <-> Dao
	- Route: 라우팅(springboot의 경우 route기능을 controller가 처리)
	- Controller: Querystring, pathvariable, body 등의 데이터 provider/service로 넘김, 형식적 validation 처리
	- Provider/Service: 비즈니스로직, transaction, 의미적 validation 처리(DB 거치는 검증 ex. 중복되는 이메일인지 등)
		- Provider: 조회 작업 수행시(작업 중 조회의 비중이 높음)
		- Service: 그 외의 작업 수행시
	- Dao: Query작성, 실행


## 이슈
- [winSCP] 네트워크 오류 - 접속시간 초과  
[https://suakang17.github.io/devlife/2022-04-20-winscp-network-error/](https://suakang17.github.io/devlife/2022-04-20-winscp-network-error/)