import flet as ft

def main(page: ft.Page):
    page.title = 'TALK'
    page.window_width = 393
    page.window_height = 852
    page.bgcolor='#F4F4F4'

    def page_change():
        ft.app(target=page1)
        
    img = ft.Image(
        src=f'./logo.png',
        fit=ft.ImageFit.CONTAIN,
    )

    page.appbar = ft.AppBar(
        title=ft.Text("WELCOME", color='black', weight=ft.FontWeight.BOLD),
        center_title=True,
        bgcolor='#ffffff',
        
        toolbar_height=76
    )

    connect_button = ft.ElevatedButton(
        bgcolor='#FD9F28',
        width=242,
        height=52,
        on_click=page_change,
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

    
    page.add(img)
    page.add(btn_container)


def page1(page: ft.Page):
    page.title = "Basic filled buttons"
    page.add(
        ft.FilledButton(text="Filled button"),
        ft.FilledButton("Disabled button", disabled=True),
        ft.FilledButton("Button with icon", icon="add"),
    )


ft.app(target=main)