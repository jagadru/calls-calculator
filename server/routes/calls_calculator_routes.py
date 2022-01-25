from workflow.invoice import InvoiceWorkflow


def init(app):

    """
    Create all routes for calculate the fees of calls.
    app: Flask
    """
    @app.route('/v1/<phone_number>/invoice/<billing_period>/', methods=['GET'])
    def get_price(phone_number, billing_period):
        try:
            return InvoiceWorkflow(
                phone_number,
                'example.csv',
                billing_period,
            ).run()
        except Exception as err:
            print(err)
            return {'error': 1}
