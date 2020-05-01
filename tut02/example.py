# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp,self).__init__()
        self.set_default_size(640,480)
        self.set_title("Anish Asokan")
        self.btn = gtk.Button("Submit")
        self.btn.connect("button_press_event", self.youtube)
        screen = gtk.Fixed()
        screen.put(self.btn, 50,50)
        self.add(screen)
        self.show_all()

    def youtube(self,widget,event):
    	print("Submit button clicked")

PyApp()
gtk.main()
