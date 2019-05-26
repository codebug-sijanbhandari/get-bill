from gen_bill.api import Good, Invoice, InvoiceBuilder

if __name__ == '__main__':


    invoice = Invoice("Kumar", "XYZ Company", "Robin")
    invoice.add_good(Good('Eggs', 10, 0.9))
    invoice.add_good(Good('Bread', 2, 2))
    invoice.add_good(Good('Potato', 1, 2))
    builder = InvoiceBuilder(invoice)
    builder.create('abc.pdf')