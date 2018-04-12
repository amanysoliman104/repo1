import Models
import stores
import time 



member1 = Models.Members("amany", 24)
member2 = Models.Members("anas", 20)
member3 = Models.Members("amany", 6)
post1   = Models.Posts("lesson1","undarstand this lesson ")
time.sleep(5)
post2   = Models.Posts("lesson2"," not undarstand this lesson" , member1.id)
post3   = Models.Posts("lesson3","very nice lesson" , member1.id)
member_store = stores.Members_stores()
member_store.add(member1)
member_store.add(member2)
member_store.add(member3)
post_store  = stores.Posts_stores()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
print member_store.entity_exists(member1)
lists = member_store.get_by_name(member1.name)
print lists[0].id
member_store.get_members_with_posts([post1,post2,post3])
print member1.show()
print post_store.get_posts_by_date()


######################################################
'''def create_members():

    member1 = models.Members("Mohammed", 20)
    member2 = models.Members("Omar", 22)
    member3 = models.Members("Abdo", 25)
    print(member1)
    print(member2)
    print(member3)
    print("=" * 30)

    return member1, member2, member3


def store_should_add_models(members_instances, member_store):

    for member in members_instances:
        member_store.add(member)

def stores_should_be_similar():

    member_store1 = stores.Members_store()
    member_store2 = stores.Members_store()
    if member_store1.get_all() is member_store2.get_all():
        print("Same stores elements !")


def print_all_members(member_store):
    print("=" * 30)

    for member in member_store.get_all():
        print(member)

    print("=" * 30)

def get_by_id_should_retrieve_same_object(member_store, member2):
    member2_retrieved = member_store.get_by_id(member2.id)

    if member2 is member2_retrieved:
        print("member2 and member2_retrieved are matching !")


def update_should_modify_object(member_store, member3):
    member3_copy = Models.Members(member3.name, member3.age)
    member3_copy.id = 3

    if member3_copy is not member3:
        print("member3 and member3_copy are not the same !")

    print(member3_copy)
    member3_copy.name = "john"
    member_store.update(member3_copy)
    print(member_store.get_by_id(member3.id))


def catch_exception_when_deleting():
    try:
        member_store.delete(5)
    except ValueError:
        print("It should be an existence entity before deleting !")


members_instances = create_members()
member1, member2, member3 = members_instances

member_store = stores.Members_store()

store_should_add_models(members_instances, member_store)

#stores_should_be_similar()

print_all_members(member_store)

get_by_id_should_retrieve_same_object(member_store, member2)

#update_should_modify_object(member_store, member3)

catch_exception_when_deleting()'''



 
