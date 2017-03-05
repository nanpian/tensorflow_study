# code: UTF-8
import tornado.ioloop
import tornado.web
import uuid
import Image
import StringIO
import os

class PredictHandler(tornado.web.RequestHandler):
     def get(self):
		self.render("index.html")

     def post(self):  
        if self.request.files:  
            file_name = "%s" % uuid.uuid1()
            print 'file_name',file_name
            file_raw = self.request.files["file"][0]["body"]
            usr_home = os.path.expanduser('~')
            fin = open(usr_home+"/tensorflow/static/tmp/m_%s.png" % file_name,"w")
            print "success to open file"  
            fin.write(file_raw)  
            fin.close()

application = tornado.web.Application([
    (r"/predict", PredictHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
