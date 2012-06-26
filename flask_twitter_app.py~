import flask,flask.views
import twitter
app=flask.Flask(__name__)

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template("login.html")
    def post(self):
        username=flask.request.form["name"]
        api = twitter.Api()
	sts = api.GetUserTimeline(username)
	str1='none'
        for user2 in sts:
    	    user_name=user2.user.name
            user_follower=user2.user.followers_count
            user_friend=user2.user.friends_count
            user_status=user2.user.statuses_count
            user_date=user2.created_at   
            relative_date=user2.relative_created_at
            break
         
        #str1="NAME OF USER::" +repr()+" TOTAL NUM OF FRIENDS ARE::" +repr( %d  TOTAL FOLLOWER:: %d TOTAL MESSAGE:: %d 
        #return str1
        return "NAME OF USER::%s TOTAL NUM OF FRIENDS ARE:: %d  TOTAL FOLLOWER:: %d TOTAL MESSAGE:: %d TOTAL NUM OF STATUS:: %s" %(str(user_name),user_friend,user_follower,user_status,str(user_date)) 

         
app.add_url_rule("/",view_func=View.as_view("main"), methods=['GET','POST'])
app.debug = True
app.run()
