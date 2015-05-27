
# Path to a file
p = '/Users/ralph/Documents/_development/me/SANDBOX/README.md'

try:
    process_file(f)
except OSError as e:
    print('Could not process file because{}'\
          .format(str(e)))