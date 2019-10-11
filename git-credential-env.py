#!/usr/bin/env python3

import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action')
    parser.add_argument('--username-var', default='GIT_USERNAME')
    parser.add_argument('--password-var', default='GIT_PASSWORD')
    args = parser.parse_args()

    if args.action == 'get':
        print('username=' + os.environ.get(args.username_var, ''))
        print('password=' + os.environ.get(args.password_var, ''))

