# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp,self).__init__()
        self.set_default_size(640,480)
        self.set_title("Anish Asokan")

        """
        Container
        """

        self.fixed = gtk.Fixed()

        self.entry = gtk.Entry()
        self.entry.add_events(gtk.gdk.KEY_RELEASE_MASK)
        self.entry.connect("key-release-event", self.on_key_release)

        self.lbl   = gtk.Label("Username: ")

        self.fixed.put(self.lbl, 10,10)
        self.fixed.put(self.entry, 10, 50)

        self.add(self.fixed)

        self.show_all()

    def on_key_release(self,widget, event):
    	print("Key pressed: " + widget.get_text())

PyApp()
gtk.main()
