
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
	try:
	    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settingss")

	    from django.core.management import execute_from_command_line

	    execute_from_command_line(sys.argv)
	except Exception as e:
		raise Exception("Script failed because of failed to start the server and exception has raised"+ str(e))
