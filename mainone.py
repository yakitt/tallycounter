from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.core.window import Window

Window.set_icon('book.png')
class MyApp(App):
    def build(self):
        self.layout=BoxLayout(orientation="vertical")
        self.label=Label(text="Библеотека",font_size=50)
        self.button=Button(text='Начать',font_size=50,size_hint_y=None)
        self.image=Image(source='book.png',size=(100,100))
        self.label1=Label(text='Еще книги скоро будут...',font_size=20)
        self.button1=Button(text='Обратно',pos=(500,0),size_hint_y=None)
        self.button1.bind(on_press=self.on_two_button_press)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.image)
        self.button.bind(on_press=self.on_button_press)
        return self.layout
    def on_button_press(self,instance):
        self.layout.clear_widgets()
        self.layout.add_widget(self.button1)
        self.layout.add_widget(self.label1)
        self.button4=Button(text='')
        self.button2=Button(text='Книга про кота',font_size=30,size_hint_y=None)
        self.button2.bind(on_press=self.catbook)
        self.layout.add_widget(self.button2)
    def on_two_button_press(self,instance):
        self.layout.clear_widgets()
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.image)
        self.button.bind(on_press=self.on_button_press)
    def catbook(self,instance):
        self.layout.clear_widgets()
        self.label3=Label(text='Книга скоро будет....',font_size=50,color=(1,0,0,1))
        self.button3=Button(text='Обратно',pos=(500,0),size_hint_y=None)
        self.button3.bind(on_press=self.on_button_press)
        self.layout.add_widget(self.label3)
        self.layout.add_widget(self.button3)
if __name__=='__main__':
    MyApp().run()