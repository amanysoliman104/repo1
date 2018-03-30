#from __future__ import division, absolute_import, print_function
#from future.builtins import super

import Models
import datetime
import itertools 



#**********************************************************************************
class BaseStore(object):

    def __init__(self , data_provider , last_id):
        self._data_provider = data_provider
        self._last_id  = last_id

    def add(self,item_instance):                     #member is an object of Members class
        item_instance.id = self._last_id                                  
        self._data_provider.append(item_instance)
        self.last_id +=1
        

        
    def get_all(self):
        print("all members")
        return self._data_provider 
    
    
    def get_by_id(self, id) :        # variable inatance was id 
        for item_instance in self._data_provider :
            if item_instance.id == id :
                return  item_instance 
        return None 


    def delete (self , item_instance) :
        self._data_provider.remove(get_by_id(item_instance.id))


    def entity_exists(self, item_instance) :
        if self.get_by_id(item_instance.id) == item_instance :
            return "true"
        else :
            return "false"


    def update(self,item_instance) :
        result = item_instance
        all_objects = self.get_all()
        for index , current_object in enumerate(all_objects):
            if current_object.id == item_instance.id:
                all_objects[index] = item_instance
                break
        return result  


#**********************************************************************************
class Members_stores(BaseStore) :
    members = []                             #list of objects
    last_id = 1
     
    def __init__(self):
        super(Members_stores , self).__init__(Members_stores.members, Members_stores.last_id)
         
      
    def get_by_name(self,name) :
        list_for_names = []
        for count in Members_stores.members :
            if count.name == name :
                list_for_names.append(count)
        return list_for_names
    
    def get_members_with_posts(self , all_posts):
        all_members = self.get_all()
        for  member , post  in itertools.product(all_members , all_posts) :
            if post.member_id == member.id :
                member.posts.append(post)
        for member in all_members:
            yield member    

                     
         

    
    def get_top_two(self, all_posts):
        members_with_posts = list(self.get_members_with_posts(all_posts))

        members_with_posts.sort(key=lambda member: len(member.posts), reverse=True) # to sort member who have most posts 

        yield members_with_posts[0]
        yield members_with_posts[1]





#**************************************************************
class Posts_stores (BaseStore):
    posts = []
    last_id = 1
    def __init__(self):
        super(Posts_stores , self).__init__(Posts_stores.posts, Posts_stores.last_id)


    def get_posts_by_date(self) : 
        
        return self.date




        


#*********************************************************************************
