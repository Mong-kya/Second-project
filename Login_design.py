from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.app import MDApp

class LoginApp(MDApp):
    def build(self):
        layout = FloatLayout()  # Change BoxLayout to FloatLayout
        
        # Username TextField
        self.username = MDTextField(
            hint_text="Enter Username",
            size_hint=(None, None), width=300, height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.6}  # Position adjusted to center
        )
        
        # Password TextField
        self.password = MDTextField(
            hint_text="Enter Password",
            password=True,
            size_hint=(None, None), width=300, height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.4}  # Position adjusted to center
        )
        
        # Login Button
        login_btn = MDFlatButton(
            text="Login",
            size_hint=(None, None), width=300, height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.2},  # Position adjusted to center
            on_release=self.verify_login
        )
        
        # Add all widgets to layout
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_btn)
        
        return layout

    def verify_login(self, instance):
        print(f"Username: {self.username.text}, Password: {self.password.text}")

# Run the app
LoginApp().run()
