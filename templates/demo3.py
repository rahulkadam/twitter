import flask,flask.views
#from flask.ext.fillin import FormWrapper
app=flask.Flask(__name__)
#********************************************
#***********************************************

class View(flask.views.MethodView):
    def get(self):
#        return hello(name="ashish")    
        return flask.render_template("login.html") 
   #return flask.render_template("hello.html",name=name)
    def post(self,name='none'):
        name="ashish" 
        return flask.render_template("hello.html",name=name)
        #return str(flask.request.form["name"])+str(flask.request.form["name1"])
app.add_url_rule("/hello/name=/<name>/",view_func=View.as_view("main"), methods=['hello','GET','POST'])
app.add_url_rule("/",view_func=View.as_view("main"), methods=['GET','POST'])
app.add_url_rule("/login",view_func=View.as_view("main"), methods=['GET','POST'])


app.debug = True
app.run()
