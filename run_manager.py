# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
from manager.core import list_keys, get_key_details, delete_key

def main():
    parser = argparse.ArgumentParser(description="Redis Key Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # List
    parser_list = subparsers.add_parser("list", help="List keys matching check pattern")
    parser_list.add_argument("pattern", nargs="?", default="*", help="Key pattern (default: *)")

    # Get
    parser_get = subparsers.add_parser("get", help="Get key details")
    parser_get.add_argument("key", help="Key name")

    # Delete
    parser_delete = subparsers.add_parser("delete", help="Delete a key")
    parser_delete.add_argument("key", help="Key name")

    args = parser.parse_args()

    if args.command == "list":
        try:
            keys = list_keys(args.pattern)
            print(f"Found {len(keys)} keys matching '{args.pattern}':")
            for k in keys[:20]: # Limit output
                print(f" - {k}")
            if len(keys) > 20:
                print(f"... and {len(keys)-20} more.")
        except Exception as e:
             # In case Redis is down or network issues
             pass

    elif args.command == "get":
        details = get_key_details(args.key)
        if details:
            print(f"Key: {args.key}")
            print(f"Type: {details['type']}")
            print(f"TTL: {details['ttl']}")
            print(f"Value: {details['value']}")
        else:
            print("Key not found.")

    elif args.command == "delete":
        confirm = input(f"Are you sure you want to delete '{args.key}'? (y/N): ")
        if confirm.lower() == 'y':
            count = delete_key(args.key)
            if count > 0:
                print("Deleted.")
            else:
                print("Key does not exist.")
        else:
            print("Cancelled.")

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
