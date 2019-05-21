from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Frame, KeepInFrame, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch


class Good(object):
    """
    It represents each item on the invoice.
    :param title : Item name
    :param units: total number of items
    :param unit_price: price per unit of item
    """

    def __init__(self, title, units, unit_price):
        self.title = title
        self.units = units
        self.unit_price = unit_price
    
    @property
    def price(self):
        return self.units * self.unit_price


class Invoice:
    """
    It represents the invoice object.
    :param operator : billing person
    :param company: company associated with that bill
    :param user: user for whom bill is being created.

    """
    def __init__(self, operator, company, user=''):
        self.operator = operator
        self.company = company
        self.user = user
        self._goods = []
    

    def add_good(self, good):
        """
        Add a good/item to the invoice.
        :param item: the new item/good
        :type item: Good class
        """
        assert isinstance(good, Good)
        self._goods.append(good)
    
    @property
    def goods(self):
        return self._goods



class InvoiceBuilder:

    def __init__(self, invoice):
        self.invoice = invoice

    def create(self, file_name):
        bill_canvas = Canvas("hello.pdf", pagesize=letter, bottomup=0)
        text_object = bill_canvas.beginText(inch, inch)
        text_object.textLine("Bill example")
        print('data is', self.invoice.goods)
        for index, good in enumerate(self.invoice.goods):
            text_object.textLine("   {}. {}           {}          {}".format(index + 1, good.title, good.units, good.price))
        text_object.textLine("................")
        bill_canvas.drawText(text_object)
        bill_canvas.save()
