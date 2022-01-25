import argparse

from calls_calculator.command.invoice import Command

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--phone-number', type=str, required=True)
    parser.add_argument('--file', type=str, required=True)
    parser.add_argument('--billing-period', type=str, required=True)

    args = parser.parse_args()
    print(Command(args.phone_number, args.file, args.billing_period).run())
