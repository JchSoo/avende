import flet as ft
from pages.homepage import START
# from pages.login import Login

def views_handler(page):
    return {
        '/':ft.View(
            route='/',
            controls=[
            START(page)
            ]
        ),
        # '/login':ft.View(
        #     route='/login',
        #     controls=[
        #     Login(page)
        #     ]
        # ),
    }