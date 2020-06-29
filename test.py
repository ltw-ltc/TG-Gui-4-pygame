from tg_gui_4_applocals import *

@container.widgetclass
class container(container):
    pass

# do not do this, this if for developing
@container.widgetclass
class windowview(viewport):

    @subview
    class page1(container):

        def build(self):
            self.label(0, 0, self.width, unit.char_height,
                text="this is page 1"
                )
            self.button(centeredin(self), centeredin(self), unit.base, unit.base,
                text="PAGE1")

    @subview
    class page2(container):

        def build(self):
            self.rect(0, 0, self.width, self.height, color=color.red)
            self.label(0, 0, self.width, unit.char_height,
                text="this is page 2",
                color=color.red
                )
            self.button(centeredin(self), centeredin(self), unit.base, unit.base,
                text="PAGE2"
                )


@appwindow(400, 400, x = 10000)
class foo(container):

    def build(self):
        self.window = window = self.windowview(0, -1, self.width, self.height - unit.small)

        # the buttons to switch tabs
        self.btn1 = btn1 = self.button(0, above(window), self.width//2, unit.small,
            identifier=windowview.page1,
            tap=self._switch_tab,
            text='tab1',
            )
        self.btn1 = btn2 = self.button(rightof(btn1), above(window), self.width//2, unit.small,
            identifier=windowview.page2,
            tap=self._switch_tab,
            text='tab2',
            )

    def _switch_tab(self, inst, *args):
        self.window.switchview(inst.identifier)
