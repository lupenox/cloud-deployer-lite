#!/usr/bin/env python3
import argparse

def up(args):
    print(f"[UP] Launching instance type: {args.instance_type}")

def down(args):
    print(f"[DOWN] Terminating instance: {args.instance_id}")

def list_instances(args):
    print("[LIST] Showing all instances for this project")

def main():
    parser = argparse.ArgumentParser(description="Cloud Deployer Lite")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # up command
    up_parser = subparsers.add_parser("up", help="Launch a new EC2 instance")
    up_parser.add_argument("--instance-type", default="t3.micro", help="EC2 instance type")
    up_parser.set_defaults(func=up)

    # down command
    down_parser = subparsers.add_parser("down", help="Terminate an EC2 instance")
    down_parser.add_argument("--instance-id", required=True, help="ID of instance to terminate")
    down_parser.set_defaults(func=down)

    # list command
    list_parser = subparsers.add_parser("list", help="List project instances")
    list_parser.set_defaults(func=list_instances)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
