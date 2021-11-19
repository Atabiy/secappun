from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.core.camera import Camera
from kivy.uix.widget import Widget
import time

class Settings(Screen):
    pass

class SimpleSettings(Screen):
    pass

class SimpleSettings1(Screen):
    pass

class AdvancedSettings(Screen):
    pass

class PasswordS(Screen):
    back = 'SimpleSettings'
    def go_back(self):
        return self.back
    def clear_text(self):
        self.ti1.text = ''
        self.ti2.text = ''
    def is_valid(self, fp, sp):
        if self.ti1.text == self.ti2.text:
            return True
        return False

class PasswordA(PasswordS):
    back = 'AdvancedSettings'

class CameraS(Screen):
    i = 0
    back = 'SimpleSettings1'
    def change_text_temp(self):
        self.i += 1
        time.sleep(2)
        if self.i > 1:
            self.text.text = 'Анализ лица'
        else:
            self.text.text = 'Запомнить лицо'
    def go_back(self):
        return self.back

class passS(Screen):
    pass

class PinCodeS(Screen):
    back = 'SimpleSettings'
    def add_number(self, digit):
        if self.pincode_text.text == 'PINCODE':
            self.pincode_text.text = ''
        self.pincode_text.text += str(digit)
    def clear(self):
        self.pincode_text.text = 'PINCODE'
    def delit(self):
        self.pincode_text.text = self.pincode_text.text[0:-1]
    def go_back(self):
        return self.back
class PinCodeA(PinCodeS):
    back = 'AdvancedSettings'
    pass

class PinS(Screen):
    def add_number(self, digit):
        if self.pincode_text.text == 'Введите PINCODE':
            self.pincode_text.text = ''
        self.pincode_text.text += str(digit)
    def clear(self):
        self.pincode_text.text = 'Введите PINCODE'
    def delit(self):
        self.pincode_text.text = self.pincode_text.text[0:-1]

class SecurityApp(App):
    back = ''
    i = 0
    def set_back_ss1(self):
        self.back = 'SimpleSettings1'
    def set_back_a(self):
        self.back = 'AdvancedSettings'


    pin_code = ''
    password = ''

    pin_status = True
    pass_status = True
    face_status = True

    def clear_data(self):
        self.pin_code = ''
        self.password = ''

    '''def go_to_secure_screen(self):
        if self.pin_code != '' and self.pin_status:
            self.pin_status = False
            return 'pinS'
        if self.password != '' and self.pass_status:
            self.pass_status = False
            return 'passS'
        return 'Settings'''

    def check_pincode(self, pincode_text):
        if self.pin_code == pincode_text:
            return 'passS'
        return 'pinS'

    def check_pass(self, pas):
        if self.password == pas:
            return 'CameraS'
        return 'passS'

    def set_face(self):
        self.face_status = True
        self.i += 1
        if self.i > 2:
            self.back = 'CameraS'
        if self.i > 3:
            self.back = 'Settings'

    def set_pass(self, trfl, pas):
        if trfl:
            self.password = pas
        else:
            print('false')

    def set_pincode(self, pin):
        self.pin_code = pin

    def build(self):
        sm = ScreenManager()

        sm.add_widget(Settings(name ='Settings'))
        sm.add_widget(SimpleSettings(name = 'SimpleSettings'))
        sm.add_widget(SimpleSettings1(name = 'SimpleSettings1'))
        sm.add_widget(AdvancedSettings(name = 'AdvancedSettings'))

        sm.add_widget(PinCodeS(name ='PinCodeS'))
        sm.add_widget(PinCodeA(name ='PinCodeA'))
        sm.add_widget(PasswordS(name ='PasswordS'))
        sm.add_widget(PasswordA(name ='PasswordA'))
        sm.add_widget(CameraS(name = 'CameraS'))

        sm.add_widget(PinS(name = 'pinS'))
        sm.add_widget(passS(name = 'passS'))

        return sm

if __name__ == '__main__':
    SecurityApp().run()
