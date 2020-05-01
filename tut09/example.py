# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp,self).__init__()
        self.set_default_size(640,480)
        self.set_title("Anish Asokan")

        self.menubar = gtk.MenuBar()

        self.file = gtk.MenuItem("_File")

        self.filemenu = gtk.Menu()
        self.open = gtk.ImageMenuItem(gtk.STOCK_OPEN)
        self.filemenu.append(self.open)
        self.open.connect("activate", self.openFunction)
        self.file.set_submenu(self.filemenu)

        self.menubar.append(self.file)

        self.vbox = gtk.VBox(False, 2)
        self.vbox.pack_start(self.menubar, False, False, 0)
        self.add(self.vbox)

        self.show_all()

    def openFunction(self, widget):
    	print("Opening a file")

PyApp()
gtk.main()
