# 5주차 챌린지 과제
Notion설명: [Notion](https://cerulean-dew-aac.notion.site/4-996d1d85308c43f285f515277611a0b3)
==============
## 인스타그램 메인화면 쿼리문 짜기

영상에서 나온 인스타그램 메인 화면에 필요한 것들을 생각해봤다.

## [1] 화면에 보이는 것

1. User
    
    사용자의 프로필사진, 사용자의 닉네임, 작성자의 이름, 작성자의 프로필 사진
    
2. Post
    
    컨텐츠, 컨텐츠 사진, 좋아요, 좋아요 여부, 포스트가 작성일자, 좋아요 갯수
    
3. Comment
    
    댓글 내용, 댓글 생성시간
    
    이때 Comment는 제일 최신 댓글 한 개만 출력하면 된다.

<br>
<br>

## [2] 화면에 보이지 않는 것
**여기는 필요한지는 모르겠지만 일단은 적어보았다. 구현은 하지 않았다.**

댓글을 작성했을 때 넘겨주기 위한 유저 닉네임 혹은 ID

팔로우한 글을 추천해서 보여주기 위한 팔로우 목록 
<br>
<br>
 

# 구현

위 [1]을 토대로 보면

User: profileImgUrl, NickName

Post: content, COUNT(PostLike)

PostImgUrl:imgUrl

정도만 보내면 될 듯하다.

쿼리는 가독성을 위해 사용자와 글을 나눠서 보냈다.

### [1] 사용자 쿼리

사용자의 경우는 간단하다. 왜냐하면 단순하게 User의 Id만 알면 Join이나 다른 문법 필요없이 바로 SELECT를 할 수 있기 때문이다.

```sql
SELECT profileImgUrl
FROM User
WHERE userIdx = 1;
```

![Untitled](./img/Untitled%201.png)

### [2] Post 쿼리

Post의 경우는 작성해야할 것이 많다.

```sql
SELECT p.content,u.profileImgUrl, u.nickName,c.content,pi.imgUrl,
       IF(commentCount is NULL, 0, commentCount) as commentCount,
       IF(postLikeCount is NULL, 0, postLikeCount) as postLikeCount
FROM Post as p
    join User u on u.userIdx = p.userIdx
    left join(
        SELECT content, postIdx, Count(commentIdx) as commentCount
        FROM Comment
        where status = 'ACTIVE'
        group by postIdx
        order by createdAt DESC) c on c.postIdx = p.postIdx
    left join(
        SELECT postIdx, COUNT(postLikeIdx) as postLikeCount
        FROM PostLike
        where status = 'ACTIVE'
        group by postIdx) l on l.postIdx = p.postIdx
    left join(
        SELECT postIdx,imgUrl
        FROM PostImgUrl
        where status = 'ACTIVE') pi on pi.postidx = p.postIdx
where p.postIdx = 2;
```

![Untitled](./img/Untitled%202.png)

의도한 대로 나온다. 하지만 imgUrl을 제외하고는 계속 중복되는 데이터를 보내기에 별로 보기 좋지 않아보인다. 그래서 따로 imgUrl만 떼어서 실행해보았다.

```sql
SELECT profileImgUrl
FROM User
WHERE userIdx = 1;

SELECT p.content,u.profileImgUrl, u.nickName,c.content,
       IF(commentCount is NULL, 0, commentCount) as commentCount,
       IF(postLikeCount is NULL, 0, postLikeCount) as postLikeCount
FROM Post as p
    join User u on u.userIdx = p.userIdx
    left join(
        SELECT content, postIdx, Count(commentIdx) as commentCount
        FROM Comment
        where status = 'ACTIVE'
        group by postIdx
        order by createdAt DESC) c on c.postIdx = p.postIdx
    left join(
        SELECT postIdx, COUNT(postLikeIdx) as postLikeCount
        FROM PostLike
        where status = 'ACTIVE'
        group by postIdx) l on l.postIdx = p.postIdx
where p.postIdx = 2;

SELECT imgUrl
FROM PostImgUrl as pi
    join Post p on pi.postidx = p.postIdx
WHERE pi.status = 'ACTIVE' and pi.postidx = 2;
```

![Untitled](./img/Untitled%201.png)

![Untitled](./img/Untitled%203.png)

![Untitled](./img/Untitled%204.png)