# 5주차

- 실습
    
    ### DB설계 변경
    
    1. AqueryTool이 단순해서 좋긴하나, table이 5개라는 제약 때문에 [sqlDBM](https://app.sqldbm.com/)으로 진행했다.
    2. 영상에서 진행한 Follow Table이 마음에 들지 않는다. FK로 사용한 FollowerIdx와 FolloweeIdx 가 PK가 될 수 있기 때문에 FollowIdx는 필요가 없어진다.
    또한, status attr 역시 별로 마음에 들지 않는다. Table에 계속 insert delete하는 것 보단 flag로 나타내는 것이 성능이 더 좋아질 수도 있지만, Table이 비대해지기 때문에 경우에따라 더 Query시간이 오래 걸릴 수 도 있다. 
    
    ![Untitled](.img/Untitled.png)
    

### 쿼리문 실습

Mockaroo로 어느정도 더미데이터를 넣어준 뒤 진행했다. 

Post Table엔 500개, User Table엔 3개, Follow Table에도 3개를 넣고 진행했다.

1. Follow 정보 가져오기

```sql
SELECT nickname, name, profileUrl, websiteUrl, introduce,
       if(post.postCount is null, 0, post.postCount) as postCount,
       if(follow1.followCount is null, 0, follow1.followCount) as followCount,
       if(follow2.followerCount is null, 0, follow2.followerCount) as followerCount
From User
    left join (
        SELECT userIdx,  COUNT(postIdx) as postCount
        FROM Post
        WHERE status = 'ACTIVE'
        GROUP BY userIdx
    ) post on post.userIdx = User.userIdx
    left join (
        SELECT followerIdx, COUNT(followIdx) as followCount
        FROM Follow
        GROUP BY followerIdx
    ) follow1 on follow1.followerIdx = User.userIdx
    left join(
        SELECT followIdx, COUNT(followerIdx) as followerCount
        FROM Follow
        GROUP BY followIdx
    ) follow2 on follow2.followIDx = User.userIdx
WHERE User.userIdx = 1;
```

![Untitled](.img/Untitled%201.png)

1. 게시글 정보 가져오기

```sql
SELECT p.postIdx, pi.imgUrl
FROM Post as p
    join User as u  on p.userIdx = u.userIdx
    join PostImgUrl pi on p.postIdx = pi.postIdx and pi.status = 'ACTIVE'
WHERE p.status = 'ACTIVE' and u.userIdx = ?
GROUP BY p.postIdx
ORDER BY p.createdAt DESC;
```

역시 잘 동작 한다.

## **🔥**챌린지 과제: 인스타그램 메인화면 쿼리문 짜기

필요한 정보 :

[User] nickName, profileUrl

[post] content, createdAt

[postImgUrl]

[postLike] 

[Comment]

```sql
SELECT p.content, p.createdAt, u.nickname, u.profileUrl, imgUrl,
       if(pl.likeCount is null, 0, pl.likeCount) as likeCount,
       if(co.commentCount is null, 0, co.commentCount) as commentCount
FROM Post as p
    join User as u on p.userIdx = u.userIdx
    left join (SELECT postIdx, imgurl
        FROM PostImgUrl
        ) as imgUrl on imgUrl.postIdx = p.postIdx
    left join (SELECT postIdx, COUNT(userIdx) as likeCount
        FROM PostLike
        GROUP BY postIdx
        ) as pl on pl.postIdx = p.postIdx
    left join (SELECT postIdx, COUNT(userIdx) as commentCount
        FROM Comment
        ) as co on co.postIdx = p.postIdx
WHERE p.postIdx = ?;
```

처음엔 naive하게 이렇게 짰는데, 아무리 생각해도 좀 아닌 것 같아서 쿼리를 2개로 나눴다.

```sql
SELECT p.content, p.createdAt, u.nickname, u.profileUrl,
       if(pl.likeCount is null, 0, pl.likeCount) as likeCount,
       if(co.commentCount is null, 0, co.commentCount) as commentCount
FROM Post as p
    join User as u on p.userIdx = u.userIdx
    left join (SELECT postIdx, COUNT(userIdx) as likeCount
        FROM PostLike
        GROUP BY postIdx
        ) as pl on pl.postIdx = p.postIdx
    left join (SELECT postIdx, COUNT(userIdx) as commentCount
        FROM Comment
        ) as co on co.postIdx = p.postIdx
WHERE p.postIdx = ?;
```

```sql
SELECT PostImgUrl.imgUrl
FROM Post
    join PostImgUrl on Post.postIdx = PostImgUrl.postIdx
WHERE PostImgUrl.status = 'ACTIVE' and Post.postIdx = 10;
```

![Untitled](.img/Untitled%202.png)

![Untitled](.img/Untitled%203.png)