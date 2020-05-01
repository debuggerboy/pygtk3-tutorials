# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp,self).__init__()
        self.set_default_size(640,480)
        self.set_title("Anish Asokan")

        self.cb = gtk.combo_box_new_text()
        self.cb.connect("changed", self.on_changed)
        self.cb.append_text("list1")
        self.cb.append_text("list2")
        self.cb.append_text("list3")

        screen = gtk.Fixed()
        screen.put(self.cb, 50,50)
        self.add(screen)

        self.show_all()

    def on_changed(self,widget):
    	print(widget.get_active_text() )

PyApp()
gtk.main()
