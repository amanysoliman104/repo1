import Models

class Members_stores :
    members = []                             #list of objects
    last_id = 1

        
        

    def add(self,member):                     #member is an object of Members class
        member.id = Members_stores.last_id                                  
        Members_stores.members.append(member)
        Members_stores.last_id +=1
        

        


        

    def get_all(self):
        print("all members")
        return Members_stores.members 
    
    

    
    def get_by_id(self , id) :
        for count in Members_stores.members :
            if count.id == id :
                return  count 
        return None 


    def delete (self , member) :
        Members_stores.members.remove(get_by_id(member.id))


    def entity_exists(self, member) :
        if Members_stores.get_by_id(member.id) == member :
            return "true"
        else :
            return "false"






#**************************************************************
class Posts_stores : 
    posts = []
    last_id = 1

    def add(self, post):
        post.id = Posts_stores.last_id
        Posts_stores.posts.append(post)
        Posts_stores.last_id +=1



    def get_all(self):
        print("all posts")
        return Posts_stores.posts 
    
    def get_by_id(self , id) :
        for count in Posts_stores.posts :
            if count.id == id :
                return  count 
        return None 



    def delete(self , post):
        Posts_stores.posts.remove(get_by_id(post.id))


    def entity_exists(self, post) :
        if Posts_stores.get_by_id(post.id) == post : 
            return "true" 
        else :
            return "false"
            