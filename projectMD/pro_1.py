import kivy
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.properties import NumericProperty
from datetime import datetime, timedelta

class MyGrid(Widget):
    submit_button = ObjectProperty(None)
    submit_label = ObjectProperty(None)
    submit_reset = ObjectProperty(None)
    submit_minus = ObjectProperty(None)

    counter_button = ObjectProperty(None)
    counter_label = ObjectProperty(None)
    counter_reset = ObjectProperty(None)
    counter_minus = ObjectProperty(None)

    timer_label = ObjectProperty(None)

    clock = ObjectProperty(None)
    time_start = ObjectProperty(None)

    clock = None  # Initialize the clock
    time_remaining = 60
    timer_running = False  # Flag to track if the timer is running

    red_count = 0
    blue_count = 0


    def blue_press(self):
        self.blue_count += 1
        new_text = self.blue_count
        self.submit_label.text = str(new_text)

    def red_press(self):
        self.red_count += 1
        new_text = self.red_count
        self.counter_label.text = str(new_text)


    def red_minus(self):
        self.red_count -= 1
        red_text = self.red_count
        self.counter_label.text = str(red_text)

        if red_text < 0:
            self.red_count = 0
            red_text = self.red_count
            self.counter_label.text = str(red_text)


    def red_reset(self):
        self.red_count = 0
        red_text = self.red_count
        self.counter_label.text = str(red_text)

    def blue_minus(self):
        self.blue_count -= 1
        blue_text = self.blue_count
        self.submit_label.text = str(blue_text)

        if blue_text < 0:
            self.blue_count = 0
            blue_text = self.blue_count
            self.submit_label.text = str(blue_text)

    def blue_reset(self):
        self.blue_count = 0
        blue_text = self.blue_count
        self.submit_label.text = str(blue_text)

    time_remaining = NumericProperty(0)

    def start_timer(self):
        if not self.timer_running:  # Ensure the timer starts only once
            self.timer_running = True
            self.time_remaining = 60  # Set the initial time in seconds
            self.clock = Clock.schedule_interval(self.update_timer, 1)  # Schedule the timer update

    def stop_timer(self):
        if self.timer_running and self.clock:
            self.timer_running = False
            self.clock.cancel()  # Stop the timer
            self.timer_label.text = 'Timer stopped'

    def update_timer(self, dt):
        if self.time_remaining > 0:
            self.time_remaining -= 1  # Decrease time by 1 second
            self.minutes = int(self.time_remaining / 60)
            self.seconds = int(self.time_remaining % 60)
            self.timer_label.text = f'{self.minutes:02d}:{self.seconds:02d}'
        else:
            self.timer_label.text = 'Time up!'
            if self.clock:
                self.clock.cancel()






class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()