# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp,self).__init__()
        self.set_default_size(640,480)
        self.set_title("Anish Asokan")
        self.image = gtk.Image()
        self.image.set_from_file("/home/anish/images/local-01.png")
        self.add(self.image)
        self.connect("destroy", gtk.main_quit)
        self.show_all()

PyApp()
gtk.main()
