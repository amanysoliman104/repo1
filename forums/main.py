import Models

member1 = Models.members("amany", 24)
member2 = Models.members("anas", 20)
post1   = Models.Posts("lesson1","undarstand this lesson ")
post2   = Models.Posts("lesson2"," not undarstand this lesson")
post3   =Models.Posts("lesson3","very nice lesson")
member_store = Models.Member_stores()
member_store.add(member1)
member_store.add(member2)
post_store  = Models.Post_stores()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)