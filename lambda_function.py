import pathlib
from datetime import datetime
# from returns_prime_etl.api.gdrive import GdriveData
# from returns_prime_etl.service import modify_df, bigquery_service

columns = ['serial_number', 'type', 'status', 'customer_name', 'customer_address'
        , 'customer_email', 'customer_phone', 'requested_at', 'order_number'
        , 'order_created_at', 'approved_at'
        , 'received_at', 'inspected_at', 'archived_at', 'inspection_due_by', 'exchange_with', 'exchange_with_sku'
        , 'exchange_with_amount', 'difference_amount', 'exchange_order_name', 'additional_amount_captured'
        , 'payment_gateway_name', 'payment_gateway_transaction_id', 'payment_transaction_date', 'order_payment_gateway'
        , 'item_name', 'item_quantity', 'item_price', 'sku', 'reason', 'customer_comment', 'pickup_awb'
        , 'pickup_logistics', 'warehouse_location', 'exchanged_at', 'exchange_order_status', 'refund_status',
               'requested_refund_mode'
        , 'actual_refund_mode', 'refunded_at', 'return_fee', 'eligible_refund_amount', 'refunded_amount',
               'gift_card_number'
        , 'account_number', 'ifsc_code', 'account_holder_name', 'refund_link', 'shipment_tracking_status',
               'original_return_method'
        , 'actual_return_method', 'custom_attributes'
               ]


def exec_report_etl(columns = columns, date= datetime.now().strftime('%d-%m-%Y')):
    gdrive = GdriveData(f"{pathlib.Path(__file__).parent.resolve()}\double-exchange-300905-493cb131488e.json")
    client = gdrive.generate_gdrive_client()
    returns_prime_df = gdrive.create_df(client, date, columns)
    modify_df_ = modify_df.ModifyDataframe(returns_prime_df)
    returns_prime_df = modify_df_.add_report_upload_date()
    returns_prime_df = modify_df_.convert_dtype_to_string(returns_prime_df)
    return bigquery_service.save_df_to_table(returns_prime_df, 'double-exchange-300905.production.returns_prime_report_raw')


def lambda_handler(event, context):
    return exec_report_etl()

