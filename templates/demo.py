import flask,flask.views
app=flask.Flask(__name__)

class View(flask.views.MethodView):
    def get(self, page="home"):
        page+=".html"
        return flask.render_template(page)
    def post(self):
        return str(flask.request.form["name"])+str(flask.request.form["name1"])

class log(flask.views.MethodView):
    def get(self):
        return flask.render_template("login.html")
        #return 'helooo'  
    def post(self,page1="loginhgjfdj"):
        return page1
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
