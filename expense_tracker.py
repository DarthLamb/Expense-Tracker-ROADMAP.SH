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
from datetime import datetime, timezone, date

parser = argparse.ArgumentParser(description='Track your expenses efficiently.')
subparser = parser.add_subparsers(dest='command', required=True)
# Subparser for the 'add' expense command
parser_add = subparser.add_parser('add', help='Add a new expense.')
parser_add.add_argument('-a','--amount',required=True, type=float, help='The amount of the expense.')
parser_add.add_argument('-d','--description', required=True,type=str, help='The description of the expense.')
# Subparser for the update expense command
parser_update = subparser.add_parser('update', help='Update a previous expense')
parser_update.add_argument('-u', '--update', type=float, help='Which expense to update')
parser_update.add_argument('-n', '--new', type=float, help='The new amount')

# 
# 

#Function to add an expense
def add_expense(args):
    amount = args.amount
    description = args.description
    expense_list = {}
    id_pair = 1
    now = datetime.today()
    expense_list.update({'description': description,'amount': amount, 'Date': now.isoformat()})
    if amount is None or description is None:
        print("Error: Amount and description are required.")
        return
    print(f"Added expense: {description} -> ${amount} ({now.isoformat()})")
    id_pair += 1
    return expense_list

if __name__ == "__main__":
    args = parser.parse_args()
    if args.command == 'add':
        expenselist = add_expense(args)
        add_expense(args)
        print(args)
        


#Function to update expense
def update_expense(args):
    update_key = args.update
    update_pair = args.new
