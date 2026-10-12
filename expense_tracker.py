# import argparse

# print("Expense Tracker")

# parser = argparse.ArgumentParser(description='Track your expenses efficiently.')
# parser.add_argument('num1', type=int, help='The first number.')
# parser.add_argument('num2', type=int, help='The second number.')
# parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity.')
# args = parser.parse_args()

# result = args.num1 + args.num2
# print('The sum of {} and {} is {}'.format(args.num1, args.num2, result))
# if args.verbose:
#     print('Verbose mode is enabled.')
import argparse

parser = argparse.ArgumentParser(description='Track your expenses efficiently.')
subparser = parser.add_subparsers(dest='command', required=True)
# Subparser for the 'add' expense command
parser_add = subparser.add_parser('add', help='Add a new expense.')
parser_add.add_argument('-a','--amount', type=float, help='The amount of the expense.')
parser_add.add_argument('-d','--description', type=str, help='The description of the expense.')
# Subparser for the update expense command
# 
# 
# 

#Function to add an expense
def add_expense(args):
    amount = args.amount
    description = args.description
    expense_list = []
    expense_list.append({'description': description,'amount': amount})
    if amount is None or description is None:
        print("Error: Amount and description are required.")
        return
    print(f"Added expense: {description} -> ${amount}")
# parser_add.set_defaults(func=add_expense)
if __name__ == "__main__":
    args = parser.parse_args()
    if args.command == 'add':
        add_expense(args)