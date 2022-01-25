import csv
from typing import Dict, List

from calls_calculator.processor.processor import Processor


class InvoiceWorkflow:

    def read_csv_file(self, path_file: str):
        with open(path_file, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            yield reader

    def get_raw_calls_from_csv(self, path_file: str) -> List[Dict]:
        print('Reading from CSV.')
        raw_calls = []

        with open(path_file, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                raw_calls.append({
                    'caller_number': row.get('numero origen'),
                    'destination_number': row.get('numero destino'),
                    'is_reverse_charge': 'S' == row.get('cobro revertido'),
                    'duration': row.get('duracion'),
                    'start_time': row.get('fecha'),
                })

        return raw_calls

    def __init__(self, phone_number: str, file: str, billing_period: str):
        self.phone_number = phone_number
        self.file = file
        self.billing_period = billing_period

    def run(self):
        invoice = Processor(
            phone_number=self.phone_number,
            raw_calls=self.get_raw_calls_from_csv(self.file),
            billing_period=self.billing_period,
        ).process()
        return invoice
