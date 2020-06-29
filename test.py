from tg_gui_4_applocals import *

@appwindow(400, 400)
class foo(container):

    def build(self):
        self.button(centeredin(self), centeredin(self), unit.base, unit.base, tap=print)
