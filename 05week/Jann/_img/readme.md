# [5thweek] DB 실습

- join 은 table끼리도, query문끼리도 가능

- join문 옆의 쿼리문 == 서브쿼리 : 항상 이름을 붙여야함 

- group by == 그룹화

- order by == 정렬 

- join한 쿼리에서 조회시 데이터가 없으면 (null인경우) 아예 결과 출력을 안함(null로 처리 안함)  
vs.  
left join 출력함(null로 처리함)

- ?는 실행시 우리가 값 직접 입력 가능케 함

## 과제
> IG 메인화면 쿼리문
```SQL
SELECT u.profileImgUrl, u.nickName, pi.postImgIdx, p.postIdx, p.content, c.commentCount
FROM User as u
    join (SELECT content, postIdx, userIdx
          FROM Post
          WHERE status = 'ACTIVE'
          group by postIdx) p on p.userIdx = u.userIdx
    join PostImgUrl as pi on pi.postIdx = p.postIdx and pi.status = 'ACTIVE'
    join (SELECT COUNT(commentIdx) as commentCount, postIdx
          FROM Comment
          WHERE status = 'ACTIVE'
          group by postIdx) c on c.postIdx = p.postIdx
WHERE u.status = 'ACTIVE' and u.userIdx = ? and p.postIdx = ?
```
** Aqurey 결제건이 아직 등록 안되어 우선 like 제외하고 query 작성 (4/7)


