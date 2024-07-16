from sense_emu import SenseHat
import time

class RedXAnimation:
    black = (0, 0, 0)
    red = (255, 0, 0)

    frame1 = [
        red, black, black, black, black, black, black, red,
        black, red, black, black, black, black, red, black,
        black, black, red, black, black, red, black, black,
        black, black, black, red, red, black, black, black,
        black, black, black, red, red, black, black, black,
        black, black, red, black, black, red, black, black,
        black, red, black, black, black, black, red, black,
        red, black, black, black, black, black, black, red,
    ]

    frame2 = [
        red, red, red, red, red, red, red, red,
        red, red, red, red, red, red, red, red,
        red, red, red, red, red, red, red, red,
        red, red, red, red, red, red, red, red,
        red, red, red, red, red, red, red, red,
        red, red, red, red, red, red, red, red,
        red, red, red, red, red, red, red, red,
        red, red, red, red, red, red, red, red
    ]

    def __init__(self, rotation=0):
        self.sense = SenseHat()
        self.sense.set_rotation(rotation)

    def display_animation(self, duration):
        no_frames = 2
        display_time = duration / no_frames
        start_time = time.time()
        end_time = start_time + 80
        while time.time() <= end_time:
            for frame in [self.frame1, self.frame2]:
                self.sense.set_pixels(frame)
                time.sleep(display_time)

if __name__ == "__main__":
    redanimation = RedXAnimation(rotation=270)
    redanimation.display_animation(duration=1)
