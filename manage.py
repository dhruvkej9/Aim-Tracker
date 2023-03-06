#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Aim_Trainer.settings')
    try:
        from django.core.management import execute_from_command_line
    except:
        raise ImportError("Can not import django")
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
