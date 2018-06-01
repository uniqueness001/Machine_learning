#encoding: utf-8
import urllib.parse
import urllib.request
import random
import hashlib
import time
import json
from tkinter import Tk,Button,Entry,Label,Text,END

class YouDaoHelper(object):
    def __init__(self):
        pass
    def crawl(self,content):

        timestamp =int(time.time()*1000)+random.randint(1,10)
        u ="fanyideskweb"
        d =content
        f =str(timestamp)
        c ='rY0D^0\'nM0}g5Mm1z%1G4'
        salt =hashlib.md5((u+d+f+c).encode('utf-8')).hexdigest()
        data = {
            'i' : content ,
            'from':'AUTO',
            'to':'AUTO',
            'smartresult' :'dict',
            'client':'fanyideskweb',
            'salt':timestamp,
            'sign':salt,
            'doctype':'json',
            'version':'2.1',
            'keyfrom':'fanyi.web',
            'action':'FY_BY_REALTIME',
            'typoResult':'false'
        }
        data = urllib.parse.urlencode(data).encode('utf-8')
        request = urllib.request.Request(url ='http://fanyi.youdao.com/translate?smartresult=dict&'
                                              'smartresult=rule&smartresult=ugc&sessionFrom=dict2.top'
                                            ,method='POST',data =data)
        response = urllib.request.urlopen(request)
        html=response.read().decode('utf-8')
        target=json.loads(html)
        result=target['translateResult'][0][0]['tgt']
        return result
class Application(object):
    def __init__(self):
        self.helper = YouDaoHelper()
        self.window = Tk()
        self.window.title(u'记录爱的字典')
        self.window.geometry("280x350+700+300")

        self.entry =Entry(self.window)
        self.entry.place(x=10, y=10,width=200,height=25)

        self.submit_btn=Button(self.window,text=u'心之往',command=self.submit)
        self.submit_btn.place(x=220,y=10,width=50,height=25)

        self.title_label=Label(self.window,text=u'往之果：')
        self.title_label.place(x=10,y=55)

        self.result_text=Text(self.window,background='#ccc')
        self.result_text.place(x=10,y=75,width=260,height=265)
    def submit(self):
        content =self.entry.get()
        result = self.helper.crawl(content)
        self.result_text.delete(1.0,END)
        self.result_text.insert( END,result)
    def run(self):
        self.window.mainloop()
if __name__=='__main__':
    app =Application()
    app.run()
