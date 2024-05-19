import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import serial
from abc import ABC, abstractmethod

class MotorBase(ABC):
    def __init__(self, port, baudrate):
        self._ser = serial.Serial(port, baudrate)
        print("Motor inicializado y conectado a", port)   
    @abstractmethod
    def mover_derecha(self):
        pass  
    @abstractmethod
    def mover_izquierda(self):
        pass
    @abstractmethod
    def parar(self):
        pass

class Motor(MotorBase):
    def mover_izquierda(self, *args):
        self._ser.write(b'D')
    def mover_derecha(self, *args):
        self._ser.write(b'I')
    def parar(self, *args):
        self._ser.write(b'S')

class ServoApp(App):
    def build(self): 
        self.motor = Motor(port='COM3', baudrate=9600)
        layout = BoxLayout(orientation='horizontal')
        self.boton_derecha = Button(text='Mover Izquierda')
        self.boton_derecha.bind(on_press=self.motor.mover_izquierda) # type: ignore
        self.boton_derecha.bind(on_release=self.motor.parar) # type: ignore
        self.boton_izquierda = Button(text='Mover Derecha')
        self.boton_izquierda.bind(on_press=self.motor.mover_derecha)# type: ignore
        self.boton_izquierda.bind(on_release=self.motor.parar)# type: ignore
        layout.add_widget(self.boton_derecha)
        layout.add_widget(self.boton_izquierda)
        return layout

if __name__ == '__main__':
    ServoApp().run()
