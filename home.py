import flet  as ft
from connections.connections import db

def home(page: ft.Page, width: int, height: int):
         
       

    valores_controls = {
        'titulo':['entradas','Saidas', 'Ativos'],
        'icons':[ft.icons.ARROW_UPWARD,ft.icons.ARROW_DOWNWARD, ft.icons.PERSON],
        'color':[ft.colors.BLUE,ft.colors.RED, ft.colors.BLUE],
        'values':[0,0,0]
    }    

    def inserir_dados(e):
        alertdialog = alertDialog(page, 'Adicionar Usuarios')

        alertdialog.actions[0].controls[0].on_click = lambda e: novo_func(e)

        def novo_func(e):
            dados = []

            for control in alertdialog.content.controls[0].controls:
                if control.value.strip() == '':                
                    SnackBar(page, f'{control.hint_text} não prenchido!', ft.icons.CLOSE)
                    dados.clear()
                    break 
                
                else:
                    dados.append(control.value)

            if len(dados) == 4:                
                 alertdialog.open = False

                 db.inserirDad(
                     nomeTabela='funcionarios',
                     colunas=['nome','cargo','departamento','email'],
                     dados=dados
                 )

            page.update()
            


    view = ft.View(
        route='/',
        controls=[
            ft.Stack(
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                col={'xs': 12, 'sm': 12},
                                bgcolor=ft.colors.BLUE,
                                height=height * 0.15
                            )
                                
                        ],                        
                    ),
                    ft.Container(                        
                        padding=ft.padding.only(
                            top=60
                        ),                                         

                        content=ft.ResponsiveRow(
                            controls=[
                                ft.Container(
                                    bgcolor=ft.colors.WHITE,
                                    col={'xs': 12, 'sm': 12, 'md': 2.6},
                                    height=height*0.18,
                                    border_radius=10,
                                    padding=ft.padding.only(
                                         top=8,
                                         left=5,
                                         right=5,
                                         bottom=5
                                    ),

                                    content=ft.Column(
                                        controls=[
                                            ft.Text(
                                                value=valores_controls['titulo'][i].upper(),
                                                size=16,
                                               color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
                                               weight='bold'
                                            ),
                                            ft.Divider(
                                                height=1,
                                                thickness=1,
                                                color=ft.colors.with_opacity(0.4, ft.colors.BLACK),                                                
                                            ),

                                            ft.Row(
                                                controls=[
                                                    ft.Text(
                                                        value=format(valores_controls['values'][i], ",.2f"),
                                                        size=18,
                                                        color=valores_controls['color'][i],
                                                        weight='bold'
                                                    ),
                                                    ft.Icon(
                                                        name=valores_controls['icons'][i],
                                                        size=30,
                                                        color=valores_controls['color'][i]
                                                    )
                                                ],
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                            )

                                        ],
                                        spacing=15
                                    )

                                 ) for i in range(len(valores_controls['titulo']))
                           ],
                           alignment=ft.MainAxisAlignment.CENTER,
                           spacing=40

                        ),
                                                            
                    ),
                    ft.Container(
                        padding=ft.padding.only(
                            top=height * 0.18 + 75
                        ),
                         content=ft.ResponsiveRow(
                            controls=[
                                ft.Container(
                                    bgcolor=ft.colors.WHITE,
                                    col={'xs': 12, 'sm': 12, 'md': 7.8},
                                    height=height*60,
                                    border_radius=10,
                                    padding=ft.padding.only(
                                        top=8,
                                        left=5,
                                        right=5,
                                        bottom=5        
                                    ),  
                                    
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                     ft.Text(
                                                         value='Tabela de Funcionários',
                                                         color=ft.colors.with_opacity(0.4, 'black'),
                                                         size=16,
                                                         weight='bold',
                                                     ),

                                                     ft.IconButton(
                                                         icon=ft.icons.ADD_CIRCLE_OUTLINE,
                                                         icon_color=ft.colors.BLUE,
                                                         icon_size=20,
                                                         on_click= lambda e: inserir_dados(e)
                                                     )                                                   
                                                ],
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                            ),
                                           
                                            ft.Divider(
                                                height=1,
                                                thickness=2
                                            ),
                                            ft.ResponsiveRow(
                                                controls=[
                                                    ft.Column(
                                                        col={'sm': 12,},

                                                        controls=[
                                                            ft.Row(
                                                                controls=[
                                                                    ft.DataTable(
                                                                        show_bottom_border=True,
                                                                        heading_row_height=35,
                                                                        data_row_max_height=40, 

                                                                        columns=[
                                                                            ft.DataColumn(ft.Text(value='Nome', size=13, color=ft.colors.with_opacity(0.4, 'black'))),
                                                                            ft.DataColumn(ft.Text(value='Cargo', size=13, color=ft.colors.with_opacity(0.4, 'black'))),
                                                                            ft.DataColumn(ft.Text(value='Departamento', size=13, color=ft.colors.with_opacity(0.4, 'black'))),
                                                                            ft.DataColumn(ft.Text(value='Email', size=13, color=ft.colors.with_opacity(0.4, 'black'))),
                                                                            ft.DataColumn(ft.Text(value='Gerar', size=13, color=ft.colors.with_opacity(0.4, 'black'))),
                                                                        ],

                                                                        rows=[
                                                                            ft.DataRow(
                                                                                 cells=[
                                                                                     ft.DataCell(ft.Text(value='Web Tech', size=13, color=ft.colors.with_opacity(0.4, 'black'))),
                                                                                     ft.DataCell(ft.Text(value='Admin', size=13, color=ft.colors.with_opacity(0.4, 'black'))),
                                                                                     ft.DataCell(ft.Text(value='Redes Social', size=13, color=ft.colors.with_opacity(0.4, 'black'))),
                                                                                     ft.DataCell(ft.Text(value='webtech@wemai.com', size=13, color=ft.colors.with_opacity(0.4, 'black'))),
                                                                                     ft.DataCell(
                                                                                         ft.Row(
                                                                                             controls=[
                                                                                                 ft.IconButton(
                                                                                                     icon=ft.icons.EDIT_DOCUMENT,
                                                                                                     icon_color=ft.colors.BLUE,
                                                                                                     icon_size=18                                                                                                    
                                                                                                 ),
                                                                                                  ft.IconButton(
                                                                                                     icon=ft.icons.DELETE,
                                                                                                     icon_color=ft.colors.RED,
                                                                                                     icon_size=18                                                                                                    
                                                                                                 )
                                                                                             ]
                                                                                         )
                                                                                     ),
                                                                                 ]  
                                                                            )
                                                                        ],
                                                                        
                                                                        width=820                                                                          
                                                                    )
                                                                ],
                                                                scroll=ft.ScrollMode.ADAPTIVE
                                                            )
                                                        ]
                                                    )
                                                ],
                                            )
                                        ]

                                    )               
                                )
                           ],
                           alignment=ft.MainAxisAlignment.CENTER,
                           spacing=40

                        )
                    )               
                        
                    
                ],
                height=height,
                width=width
            )
        ],
        bgcolor=ft.colors.with_opacity(00.02, ft.colors.BLACK)
    )


    return view

def alertDialog(page: ft.Page, title: str, dados: list = []):

    value_controls = {

        'hint_text':['Nome', 'Cargo' , 'Departamento' , 'Email'],
        'icon': [ft.icons.PERSON, ft.icons.WORK, ft.icons.WORK, ft.icons.EMAIL]
    }

    def close(e):
        alertDialog.open = False

        page.update()

    alertDialog = ft.AlertDialog(
        modal= True,
        title=ft.Row(
            controls=[
                ft.Text(
                    value=title,
                    color=ft.colors.with_opacity(0.4, 'black'),
                    size=16,
                    weight='bold'
                ),
                ft.IconButton(
                    icon=ft.icons.CLOSE,
                    icon_color=ft.colors.RED,
                    icon_size=25,
                    on_click = lambda e: close(e)
                    
                )                
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),        
        content=ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={'sm': 12, 'md' : 12},
                    height=220,
                    controls=[
                        ft.TextField(
                            hint_text=value_controls['hint_text'][i],
                            prefix_icon=value_controls['icon'][i],
                            hint_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.4, 'black'),
                                weight='bold'

                            ),
                            text_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.4, 'black'),
                                weight='bold'
                            ),
                             border=ft.InputBorder.UNDERLINE,                                                       
                            text_vertical_align=-0.40,
                            autofocus=True
                        ) for i in range(len(value_controls['hint_text']))
                    ]
                )
            ]
        ),
        actions=[
            ft.ResponsiveRow(
                controls=[
                    ft.FloatingActionButton(
                        text=title,
                        col={'sm':12},
                        bgcolor=ft.colors.BLUE,
                        height=40,
                        foreground_color=ft.colors.WHITE
                        
                    )
                ]
            )
        ]
    )

    page.overlay.append(alertDialog)
    alertDialog.open = True
    page.update()

    return alertDialog

def SnackBar(page: ft.Page, title: str, icon: ft.icons):

    SnackBar = ft.SnackBar(
        content=ft.Row(
            controls=[
                ft.Icon(
                    name=icon,
                    size=25,
                    color=ft.colors.BLUE
                ),
                ft.Text(
                    value=title,
                    size=14,
                    color=ft.colors.BLUE
                )
            ]
        )
    )
    page.overlay.append(SnackBar)
    SnackBar.open = True
    page.update()

    return SnackBar