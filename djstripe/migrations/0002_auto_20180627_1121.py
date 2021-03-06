# Generated by Django 2.0.6 on 2018-06-27 08:21

from django.db import migrations

import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="business_name",
            field=djstripe.fields.StripeCharField(help_text="The publicly visible name of the business", max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="account",
            name="support_url",
            field=djstripe.fields.StripeCharField(help_text="A publicly shareable URL that provides support for this account", max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="charge",
            name="receipt_number",
            field=djstripe.fields.StripeCharField(help_text="The transaction number that appears on email receipts sent for this charge.", max_length=14, null=True),
        ),
        migrations.AddField(
            model_name="coupon",
            name="name",
            field=djstripe.fields.StripeCharField(blank=True, help_text="Name of the coupon displayed to customers on for instance invoices or receipts.", max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="deactivate_on",
            field=djstripe.fields.StripeJSONField(help_text="An array of connect application identifiers that cannot purchase this product. Only applicable to products of `type=good`.", null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="images",
            field=djstripe.fields.StripeJSONField(help_text="A list of up to 8 URLs of images for this product, meant to be displayable to the customer. Only applicable to products of `type=good`.", null=True, blank=True),
        ),
        migrations.AddField(
            model_name="plan",
            name="active",
            field=djstripe.fields.StripeBooleanField(default=True, help_text="Whether the plan is currently available for new subscriptions."),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="charge",
            name="receipt_sent",
        ),
        migrations.AlterModelOptions(
            name="account",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="bankaccount",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="card",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="charge",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="dispute",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="event",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="fileupload",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="invoiceitem",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="payout",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="refund",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="source",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="subscription",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="transfer",
            options={"get_latest_by": "created"},
        ),
        migrations.AlterModelOptions(
            name="upcominginvoice",
            options={"get_latest_by": "created"},
        ),
    ]
