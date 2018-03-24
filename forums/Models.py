import stores
class Members :

    
    def __init__ (self , name , age ):

        self.name = name
        self.age = age
        self.id = 0 
        self.posts = []

    def __str__ (self):
        return f" name : {self.name} , age : {self.age}"
        

#**********************************************************
class Posts :

    def __init__ (self ,title , content , member_id = 0):

        self.title = title
        self.content = content
        self.id = 0
        self.member_id = member_id
        self.date = datetime.datetime.now()

def __str__ (self) :
    return f"title : {self.title} , content : {self.content}"







#************************************************************   

