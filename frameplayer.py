import sys

from psychopy import visual, core, event  # import some libraries from PsychoPy
from psychopy.hardware import keyboard


class Frameplayer:
    def __init__(self):
        self.window = visual.Window([800, 600], monitor="testMonitor", units="pix",
                                    color=(-1, -1, -1), fullscr=True, checkTiming=False)
        self.dot = visual.GratingStim(win=self.window, size=3, pos=[10, 10], sf=0, rgb=(1, 1, 1))

        self.kb = keyboard.Keyboard()
        self.dot.draw()
        self.window.flip()

    def update_dot_pos(self, pos):
        """
        :param pos: X,Y tuple
        """
        self.dot.draw()
        self.dot.pos = pos
        self.window.flip()

        if len(self.kb.getKeys()) > 0:
            sys.exit()
        event.clearEvents()

    def __del__(self):
        # cleanup
        self.window.close()
        # core.quit()

        # super().__del__()


# current_frame = 0
# while True:  # this creates a never-ending loop
#     fixation.draw()
#     fixation.pos = [10, current_frame % 100]
#     mywin.flip()

if __name__ == '__main__':
    from time import sleep
    fp = Frameplayer()
    for i in range(20):
        fp.update_dot_pos([10, i*10 % 100])
        sleep(.1)



