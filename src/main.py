
import flet as ft





import flet as ft

class DoctorsView(ft.View):
    def __init__(self):
        super().__init__(
            route="/doctors",
            padding=ft.padding.only(left=0, right=0, bottom=0, top=0),
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            bgcolor="#E6F3F3"  # Consistent background
        )

        # Mock data (replace with your actual data source)
        self.doctors_data = [
            {"name": "د. أحمد علي", "phone": "+967 777 123 456", "specialty": "أخصائي قلب"},
            {"name": "د. فاطمة سالم", "phone": "+967 733 987 654", "specialty": "أخصائي أطفال"},
            {"name": "د. عمر حسن", "phone": "+967 711 555 222", "specialty": "أخصائي أعصاب"},
            {"name": "د. ليلى محمد", "phone": "+967 772 333 444", "specialty": "أخصائي جلدية"},
            {"name": "د. سامي يوسف", "phone": "+967 735 777 888", "specialty": "جراح عام"},
            {"name": "د. هدى إبراهيم", "phone": "+967 778 999 000", "specialty": "أخصائي عيون"},
            {"name": "د. خالد سعيد", "phone": "+967 712 444 555", "specialty": "جراح عظام"},
            {"name": "د. منى عبد الله", "phone": "+967 774 666 777", "specialty": "أخصائي أنف وأذن وحنجرة"},
            {"name": "د. رامي ناصر", "phone": "+967 736 888 999", "specialty": "أخصائي مسالك بولية"},
            {"name": "د. نور مصطفى", "phone": "+967 779 111 222", "specialty": "طبيب نفسي"},
        ]


        self.__header = ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_color="#000000",
                        on_click=lambda e: e.page.go("/Splash")  # Back to main
                    ),
                   
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
             bgcolor="#87CEEB",  # Consistent header color
             padding=ft.padding.only(top=8)
        )


        self.__title = ft.Text(
            value="الأطباء",
            color=ft.colors.BLACK,
            size=22,
            font_family="Poppins",
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER
        )

        self.doctors_list = ft.Column(
            scroll=ft.ScrollMode.AUTO,  # Enable scrolling if needed
            controls=self.create_doctor_cards(),
            spacing=15,
            height=550,  # Set a fixed height for the scrollable area
        )

        self.__content = ft.Container(
            content=ft.Column(
                controls=[
                    self.__title,
                    ft.Divider(height=10, color=ft.colors.GREY_300),
                    self.doctors_list,

                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
            ),
            padding=20,  # Add padding around content
        )

        self.controls = [self.__header, self.__content]


    def create_doctor_cards(self):
        cards = []
        for doctor in self.doctors_data:
            card = ft.Card(
                elevation=4,
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.PERSON, size=40, color="#87CEEB"),
                                title=ft.Text(doctor["name"], size=18, weight=ft.FontWeight.BOLD),
                                subtitle=ft.Text(doctor["specialty"], size=14, color=ft.colors.GREY_700),
                                trailing= ft.IconButton(ft.icons.PHONE,icon_color="#87CEEB"), #  phone icon
                            ),
                             ft.Row([  # Display phone number under the name/specialty.  Better layout.
                                 # ft.Icon(ft.icons.PHONE, size=16, color=ft.colors.GREY_600), #Removed, it's redundant
                                 ft.Text(doctor["phone"], size=14, color=ft.colors.GREY_600)

                             ],
                             alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Divider(height=1, color=ft.colors.GREY_300), # Add dividers
                            
                        ],
                        spacing=5, # Reduce spacing within the card
                    ),
                    width=320,   # consistent width
                    padding=10,  # consistent padding
                    # bgcolor=ft.colors.WHITE, # Optional:  Make card background white
                    border_radius=ft.border_radius.all(10),  # Rounded corners for the card
                ),
                # margin=ft.margin.only(bottom=10) # Removed, as we're using spacing in Column

            )
            cards.append(card)
        return cards
if __name__ == "__main__":
    ft.app(target=DoctorsView)































