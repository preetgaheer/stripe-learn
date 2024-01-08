from django.shortcuts import render


def index(req):
    import stripe
    stripe.api_key = s_key
    invoice = stripe.Invoice.create(
        customer="cus_MbbMzORORskNaA",
        collection_method='charge_automatically',
        auto_advance=True,
        currency='INR',
        # automatic_tax={
        #     "enabled": True,
        # }
    )
    stripe.InvoiceItem.create(
        customer='cus_MbbMzORORskNaA',
        invoice=invoice.id,
        price_data={
            'currency': 'INR',
            'unit_amount': 1000,
            'tax_behavior': 'exclusive',
            'product': 'prod_PL3bigwgvH8GGc'
        }
    )
    stripe.Invoice.finalize_invoice(
        invoice.id
    )
    stripe.Invoice.pay(
        invoice.id,
    )
    return render(req, 'payment/index.html')
