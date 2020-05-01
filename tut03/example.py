# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp,self).__init__()
        self.set_default_size(640,480)
        self.set_title("Anish Asokan")

        self.lbl = gtk.Label("Your Name")
        screen = gtk.Fixed()
        screen.put(self.lbl, 50,50)
        self.add(screen)

        self.show_all()

PyApp()
gtk.main()
