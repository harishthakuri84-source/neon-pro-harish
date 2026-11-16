from kivy.app import App
from kivy.uix.label import Label
from android.permissions import request_permissions, Permission

class PermissionApp(App):
    def build(self):
        # Android storage permission request
        request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
        return Label(text="Permission Requested. Now you can download files!")

if __name__ == '__main__':
    PermissionApp().run()
