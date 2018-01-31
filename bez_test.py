from Tkinter import *
import random

class Application(Frame):
    def canvas_click(self, event):
        print "clicked at", event.x, event.y

 
    def createWidgets(self):
#        self.butt = Button(self, highlightbackground='#3E4149')
#        self.butt["text"] = "test"
#        self.butt["activebackground"] = "#42f474" 
#        self.butt["activeforeground"] = "#42f474" 
#        self.butt["bg"] = "#42f474" 
#        self.butt.pack({"side":"left"})
        self.can = Canvas(self)
        self.can.pack({"side":"left"})
        one = GitNode(self.can, self.canvas_click, x=5, y= 10)
        two = GitNode(self.can, self.canvas_click, x=90, y= 10)
        GitConnection(self.can, one,two,5)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

class GitNode:
    def __init__(self, canvas, click_callback=None, hover_callback=None, x=5, y=5,diam=20):
        self.x = x
        self.y = y
        self.diam = diam
        node = canvas.create_oval(x,y,x+diam,y+diam, tags="node", fill="#fff", outline="#000", width=diam/5)
        canvas.tag_bind("node","<Button-1>", click_callback)
        canvas.tag_bind("node", "<Enter>", hover_callback)

class GitConnection:
    def __init__(self, canvas, start_node, end_node, line_width):
        conne = canvas.create_line(start_node.x+start_node.diam/2, start_node.y+start_node.diam/2, \
                           end_node.x+end_node.diam/2, end_node.y + end_node.diam/2\
                           ,width=line_width)
        canvas.lower(conne)

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
