
#!/usr/bin/env python
import os
import sys
a = 1
if a == 1:
    raise Exception("Script failed because of bla bla bla")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
