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
    
    

    
    def get_by_id(self, id) :
        for count in Members_stores.members :
            if count.id == id :
                return  count 
        return None 


    def delete (self , member) :
        Members_stores.members.remove(get_by_id(member.id))


    def entity_exists(self, member) :
        if self.get_by_id(member.id) == member :
            return "true"
        else :
            return "false"

    def update(self,member) :
        result = member
        all_members = self.get_all()
        for index , current_member in enumerate(all_members):
            if current_member.id == member.id:
                all_members[index] = member
                break
        return result        

    def get_by_name(self,name):
        list_for_names = []
        for count in Members_stores.members :
            if count.name == name :
                list_for_names.append(count)
        return list_for_names
    '''def  get_by_name(self,name):

        all_members = self.get_all()
        for member in all_members:
            if member.name == member_name:
                yield member'''
    def get_members_with_posts(self , all_posts):
        all_members = self.get_all()
        for current_member in all_members :
            for current_post in all_posts :
                if current_member.id == current_post.id :
                    current_member.posts.append(current_post)

                    


            

    






#**************************************************************
class Posts_stores:
    posts = []
    last_id = 1

    def add(self, post):
        post.id = Posts_stores.last_id
        Posts_stores.posts.append(post)
        Posts_stores.last_id +=1



    def get_all(self):
        print("all posts")
        return Posts_stores.posts 
    
    def get_by_id(self, id) :   #static becouse when i call it in entity_exists methoud it tell me unbounded methoud and must called with member store class instance  
        for count in Posts_stores.posts :
            if count.id == id :
                return  count 
        return None 



    def delete(self , post):
        Posts_stores.posts.remove(get_by_id(post.id))


    def entity_exists(self, post) :
        if self.get_by_id(post.id) == post : 
            return "true" 
        else :
            return "false"

    def update(self,post) :
        result = post
        all_posts = self.get_all()
        for index , current_post in enumerate(all_posts):
            if current_post.id == post.id:
                all_posts[index] = post
                break
        return result        

      