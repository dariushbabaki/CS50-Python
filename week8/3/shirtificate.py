from fpdf import FPDF

class ShirtificatePDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.add_page()
        self.set_auto_page_break(auto=False)
        self.create_shirtificate()

    def create_shirtificate(self):
        self.set_title("CS50 Shirtificate")
        self.set_font("Arial", "B", 24)
        self.cell(0, 20, "CS50 Shirtificate", ln=True, align="C")
        self.image("shirtificate.png", x=35, y=60, w=140)
        self.set_text_color(255, 255, 255) 
        self.set_xy(0, 140)
        self.set_font("Arial", "B", 20)
        self.cell(0, 10, f"{self.name} took CS50", align="C")

if __name__ == "__main__":
    name = input("Enter your name: ")
    pdf = ShirtificatePDF(name)
    pdf.output("shirtificate.pdf")
