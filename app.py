import flet as ft

def main(page: ft.Page):
    page.title = 'TALK'
    page.window_width = 393
    page.window_height = 852
    
    #=============================================================================================
    #                                       connect page
    #=============================================================================================

    def route_change(route):
        page.views.clear()

        if page.route == "/connect":
            connect_appbar = ft.AppBar(
            title=ft.Text("CONNECT", color='black', weight=ft.FontWeight.BOLD),
            bgcolor='#ffffff',
            center_title=True,
            toolbar_height=76,
            leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/"), icon_color='black'),
            )

            qrimg = ft.Image(
                src=f'./qrcode.png',
                fit=ft.ImageFit.CONTAIN,
                width=240,
                height=240,
            )

            bluetooth_button = ft.ElevatedButton(
                bgcolor='#83B4FF',
                width=242,
                height=52,
                content=ft.Container(
                    content=ft.Row(
                        [   
                            ft.Icon(ft.icons.BLUETOOTH, color="black"),
                            ft.Text("BLUETOOTH", color='black', weight=ft.FontWeight.BOLD, size=18),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=5,
                    ),
                    padding=ft.padding.all(10),
                ),
            )

            bluetooth_container = ft.Container(
                content=bluetooth_button,
                alignment=ft.alignment.center,
                margin=30
            )

            def key_click(e):
                if key.value == "123456":
                    page.go("/call")
                
                else:
                    key.value = ""
                    page.update()

            key = ft.TextField(label='key', border="underline", color='black',width=150, height=100, max_length=6,text_size=25, content_padding=20, filled=True,bgcolor="white")
            
            btn = ft.FloatingActionButton(
                    icon=ft.icons.ARROW_FORWARD, 
                    on_click=key_click,
                    bgcolor='#FD9F28',
                    shape=ft.RoundedRectangleBorder(radius=4)
                )

            row = ft.Row(controls=[
                ft.Container(
                        margin=28
                    ),
                key,
                btn
            ])

            col = ft.Column(
                [
                    ft.Container(
                        margin=10
                    ),
                    ft.Container(
                        ft.Text("08:36", color='red', weight=ft.FontWeight.NORMAL, size=20),
                        alignment=ft.alignment.bottom_center,
                    ),
                    ft.Container(
                        ft.Text("123 456", color='black', weight=ft.FontWeight.BOLD, size = 70),
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=qrimg,
                        alignment=ft.alignment.center,
                    ),

                    ft.Container(
                        content = row,
                        alignment=ft.alignment.center,
                        bgcolor='#ffffff',
                        margin=10
                    ),
                    
                ],
            )

            page.views.append(
                ft.View(
                    "/connect",
                    [
                        connect_appbar,
                        col,
                        bluetooth_container,
                    ],
                    bgcolor='#F4F4F4'
                )
            )
        
        #=============================================================================================
        #                                        calling page
        #=============================================================================================

        elif page.route == "/call":
            def send_msg(e):
                if len(msgs.controls) == 9:
                    del msgs.controls[0]

                msgs.controls.append(ft.Text(msg_field.value, color='black', weight=ft.FontWeight.BOLD, size=18, ))
                msg_field.value = ""
                page.update()

            camrimg = ft.Image(
                src=f'./cam_example.jpg',
                fit=ft.ImageFit.CONTAIN,
                width=393,
                height=393,
            )

            icons = ft.Row(
                controls=[
                    ft.IconButton(ft.icons.MIC, icon_color='black', bgcolor='#FD9F28', width=45, height=45),
                    ft.IconButton(ft.icons.PHONE_MISSED, on_click=lambda _: page.go("/"), icon_color='black', bgcolor='#FD9F28', width=45, height=45),
                    ft.IconButton(ft.icons.VIDEO_CALL_OUTLINED, icon_color='black', bgcolor='#FD9F28', width=45, height=45),
                ],
                spacing=40,
                alignment=ft.MainAxisAlignment.CENTER,
                
            )
            
            msgs = ft.Column(controls=[

            ])

            msg_field = ft.TextField(hint_text="input msg", expand = True, color='black', bgcolor='white', filled=True)
            send_btn = ft.FloatingActionButton(icon=ft.icons.SEND, on_click=send_msg)

            msg_row = ft.Row(controls=[
                msg_field,
                send_btn
            ])

            col = ft.Column(
                [
                    ft.Container(
                        width=393,
                        height=330,
                        margin=0,
                        content=camrimg
                    ),

                    ft.Container(
                        content=icons,
                        width=393,
                        height=60,
                        alignment=ft.alignment.center,
                        bgcolor='#CACACA'
                    ),
                    ft.Container(
                        content=msgs,
                        width=393,
                        height=320,
                        alignment=ft.alignment.center,
                        bgcolor='#EDEDED'
                    ),
                    ft.Container(
                        content=msg_row,
                        margin=0,
                        alignment=ft.alignment.center,
                        bgcolor='#EDEDED'
                    ),
                ],
            )

            page.views.append(
                ft.View(
                    "/call",
                    [
                        col,
                    ],
                    bgcolor='#F4F4F4'
                )
            )

        #=============================================================================================
        #                                           main page
        #=============================================================================================

        else: #page.route == "main"
            img = ft.Image(
                src=f'./logo.png',
                fit=ft.ImageFit.CONTAIN,
            )

            appbar = ft.AppBar(
                title=ft.Text("WELCOME", color='black', weight=ft.FontWeight.BOLD),
                center_title=True,
                bgcolor='#ffffff',
                
                toolbar_height=76
            )

            connect_button = ft.ElevatedButton(
                bgcolor='#FD9F28',
                width=242,
                height=52,
                on_click=lambda _: page.go("/connect"),
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

            page.bgcolor='#F4F4F4'
            page.views.append(
                ft.View(
                    "/",
                    [
                        appbar,
                        img,
                        btn_container
                    ],
                    bgcolor='#ffffff'
                )
            )

        #=============================================================================================
        #=============================================================================================

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.routes)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)