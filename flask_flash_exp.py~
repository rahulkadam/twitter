import flask,flask.views
import os
app=flask.Flask(__name__)
app.secret_key="secret_twitter"
class View(flask.views.MethodView):
    def get(self):
        return flask.render_template("home_page.html")
            
    def post(self):
        flask.flash("this is from flASK")
        result = flask.request.form['username']
        flask.flash(result)
        return self.get() 
app.add_url_rule("/",view_func=View.as_view("main"), methods=['GET','POST'])
app.debug = True
app.run()
