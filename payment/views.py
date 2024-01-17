from django.shortcuts import render


def index(req):
    import stripe

    stripe.api_key = s_key
    invoice = stripe.Invoice.create(
        customer="cus_MbbMzORORskNaA",
        collection_method="charge_automatically",
        auto_advance=True,
        currency="INR",
        # automatic_tax={
        #     "enabled": True,
        # }
    )
    stripe.InvoiceItem.create(
        customer="cus_MbbMzORORskNaA",
        invoice=invoice.id,
        price_data={
            "currency": "INR",
            "unit_amount": 1000,
            "tax_behavior": "exclusive",
            "product": "prod_PL3bigwgvH8GGc",
        },
    )
    stripe.Invoice.finalize_invoice(invoice.id)
    stripe.Invoice.pay(
        invoice.id,
    )
    return render(req, "payment/index.html")


# Create your views here.
def sub(req):
    # stripe.Subscription.create(
    #     customer="cus_MbbLQ3oONSg1bW",
    #     items=[{"price": "price_1OZbmFSF0mfKhKajxBLYylYC"}],
    #     default_payment_method='card_1LsO91SF0mfKhKaj813sy16D',
    #     collection_method='charge_automatically'
    # )

    # new_price = stripe.Price.create(
    #     product="prod_POOZRUtvwjH9Nq",
    #     unit_amount=50000,
    #     currency="inr",
    #     recurring={
    #         "interval": "day",  # Set the interval for the subscription (e.g., month, year)
    #     },

    # )
    # stripe.Product.modify(
    #     "prod_POOZRUtvwjH9Nq",
    #     default_price=new_price.id
    # )
    # stripe.Price.modify("price_1OZbmFSF0mfKhKajxBLYylYC", active=False)

    # stripe.Subscription.modify(
    #     "sub_1OZcg0SF0mfKhKaj8WvBi7u9",
    #     items=[
    #         {
    #             "price": 'price_1OZcZHSF0mfKhKajmUA6crnb',
    #         }
    #     ],
    #     proration_behavior= 'none'
    # )

    # subscription = stripe.Subscription.retrieve('sub_1OZcg0SF0mfKhKaj8WvBi7u9')

    # Inspect the subscription items to get the item ID
    # for item in subscription['items']['data']:
    #     subscription_item_id = item['id']
    #     print(subscription_item_id)
    #     print(item)

    stripe.SubscriptionItem.delete("si_POPj7koYuuaIn5", proration_behavior="none")

    return HttpResponse("ok")
