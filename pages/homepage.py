import flet as ft

class START(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page

    def build(self):
        img = ft.Image(
        src=f'./logo.png',
        fit=ft.ImageFit.CONTAIN,
        )

        self.width=393,
        self.height=852,

        self.appbar = ft.AppBar(
            title=ft.Text("WELCOME", color='black', weight=ft.FontWeight.BOLD),
            center_title=True,
            bgcolor='#ffffff',
            
            toolbar_height=76
        )

        connect_button = ft.ElevatedButton(
            bgcolor='#FD9F28',
            width=242,
            height=52,
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text("PRESS TO CONNECT", color='white', weight=ft.FontWeight.BOLD, size=18)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=ft.padding.all(10),
            ),
        )

        btn_container = ft.Container(
            content=connect_button,
            alignment=ft.alignment.center,
            margin=30
        )

        return ft.View(
            controls=[
                # img,
                btn_container
            ]
        )