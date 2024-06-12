import models

import argparse
from models import Owner

def create_owner(args):
    owner = Owner(args.id, args.first_name, args.last_name, args.email, args.phone, args.username, args.location)
    owner.save()
    print("Owner created successfully.")

def main():
    parser = argparse.ArgumentParser(description="CLI for managing owners")
    subparsers = parser.add_subparsers(title="subcommands", dest="command")

    
    create_parser = subparsers.add_parser("create", help="Create a new owner")
    create_parser.add_argument("id", type=int, help="Owner ID")
    create_parser.add_argument("first_name", help="First name")
    create_parser.add_argument("last_name", help="Last name")
    create_parser.add_argument("email", help="Email address")
    create_parser.add_argument("phone", type=int, help="Phone number")
    create_parser.add_argument("username", help="Username")
    create_parser.add_argument("location", help="Location")

    args = parser.parse_args()

    if args.command == "create":
        create_owner(args)
    else:
        print("ERROR.Please try again.")

if __name__ == "__main__":
    main()