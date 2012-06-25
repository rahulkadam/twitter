import flask,flask.views
import twitter
app=flask.Flask(__name__)
i=0
api=twitter.Api          (consumer_key='QmnaT4d2f2u6VXTjzkElw',consumer_secret='wZb0CGESCSv1EO5Fc42d7hevNPo7yAFdcs0XZaAe5bE',access_token_key='97845768-fc1dF4oieEknwZFR9YHyA9jklLAdVKO2spdbAQJ3M',access_token_secret='ZSvuI5eyzZLMkCFrfiiEwbpE2kR1WzEazaxdHiJyDxI')
#*****************************************************************
def Cal_Friends():
    global i
    global api
    sts=api.GetFriends()
    for user in sts:
        i=i+1
    return i
#*****************************************************************
def Cal_Followers():
    global api
    sts1=api.GetFollowers()
    j=0
    for user1 in sts1:
        j=j+1;
    return j    
#***************************************************************
def Cal_Messages():
    global api
    sts2=api.GetReplies()
    k=0
    for user2 in sts2:
        k=k+1;
    return k
#*****************************************************************
def display():
    friends=Cal_Friends()
    followers=Cal_Followers()
    msg=Cal_Messages() 
    return "TOTAL NUM OF FRIENDS ARE:: %d  TOTAL FOLLOWER:: %d TOTAL MESSAGE:: %d" %(friends,followers,msg) 

#*****************************************************************

#*****************************************************************
class View(flask.views.MethodView):
    def get(self, page="home"):
        page+=".html"
        return flask.render_template(page)
    def post(self):
        return str(flask.request.form["name"])+str(flask.request.form["name1"])

class log(flask.views.MethodView):
    def get(self):
        return flask.render_template("login.html")

    def post(self,page1="loginhgjfdj"):
        
        return display()
#        return flask.render_template("rating.html")
class rating(flask.views.MethodView):
    def get(self):
        return flask.render_template("rating.html")
    def post(self):
        return 'hiiiiiiiiiii'

app.add_url_rule("/",view_func=View.as_view("main"), methods=['GET','POST'])
app.add_url_rule("/<page>/",view_func=View.as_view("main"), methods=['GET','POST'])
app.add_url_rule("/<page1>/",view_func=log.as_view("main"), methods=['GET','POST'])
app.add_url_rule("/login",view_func=log.as_view("login"), methods=['GET','POST'])
app.add_url_rule("/rating",view_func=rating.as_view("rating"), methods=['GET','POST'])

app.debug = True
app.run()
