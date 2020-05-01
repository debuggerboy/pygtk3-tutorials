# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp,self).__init__()
        self.set_default_size(640,480)
        self.set_title("Anish Asokan")        
        self.show_all()

        self.about = gtk.AboutDialog()
        self.about.set_program_name("Anish Asokan")
        self.about.set_version("v.0.01")
        self.about.set_authors("Anish Asokan")
        self.about.set_copyright("(C) Sodamker Software Inc, GNU GPL2")
        self.about.set_comments(" This is a simple tutorial to learn PyGTK")
        self.about.set_website("https://debuggerboy.com/")
        self.about.run()
        self.about.destroy()

PyApp()
gtk.main()
