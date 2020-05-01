# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp,self).__init__()
        self.set_default_size(640,480)
        self.set_title("Anish Asokan")
        self.show_all()


        """
        self.md = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "Hello, I am a simple dialog box!")
        """
        self.md = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_YES_NO, "Do you want to close me?")
        response = self.md.run()

        if response == gtk.RESPONSE_YES:
        	print("Clicked Yes")
        else:
        	print("Clicked No")

PyApp()
gtk.main()
