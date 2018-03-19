import Members

class Members_stores :
	members = []                             #list of objects
	last_id = 0

	def add(self,member):                     #member is an object of Members class
		member.id = Members_stores.last_id    # can i but last_id without members_stores ??????
		members.append(member)
		Members_stores.last_id +=1


		

	def get_all():
		print("all members")
		for count in members :
			print count.name +"  " + count.age + "  " + count.id 

	
	def get_by_id(self , id) :
		for count in members :
			if count.id == id :
				return  count 
				break 
	def delete (self , member) :
		for count in members :
			if count is member :
				members.remove(member)

    def entity_exists(self, member) :
    	if get_by_id(member.id) == member.id :
    		return "true"







#**************************************************************
class Posts_stores :
	posts = []

	def add(post):
		posts.append(post)



	def get_all():
		print("all posts")
		for count in posts :
			print count

	def delete(self , post):
		for count in posts :
			if count is post :
				posts.remove(post)

    '''def entity_exists(self, post) :
    	if get_by_id(post.id) == post.id : # why this function and we do not have id for posts
    		return "true" '''