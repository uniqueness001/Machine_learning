#encoding: utf-8
from tkinter import Tk,Button,Entry,Label,Text,END
class Application(object):
    def __init__(self):
        self.helper = YouDaoHelper()
        self.window = Tk()
        self.window.title(u'知了字典')
        self.window.geometry("280x350+700+300")

        self.entry =Entry(self.window)
        self.entry.place(x=10, y=10,width=200,height=25)

        self.submit_btn=Button(self.window,text=u'查询',command=self.submit)
        self.submit_btn.place(x=220,y=10,width=50,height=25)

        self.title_label=Label(self.window,text=u'翻译结果：')
        self.title_label.place(x=10,y=55)

        self.result_text=Text(self.window,background='#ccc')
        self.result_text.place(x=10,y=75,width=260,height=265)
    def submit(self):
        content =self.entry.get()
        result =self.helper.crawl(content)
        self.result_text.delete(1.0,END)
        self.result_text.insert( END,result)
    def run(self):
        self.window.mainloop()
if __name__=='__main__':
    app =Application()
    app.run()

