
#First one
import os
import subprocess

my_env = os.environ.copy()
my_env['PATH'] = os.pathsep.join(["/opt/myapp/", my_env['PATH']])

resutl = subprocess.run(["myapp"], env=my_env)

#Second one
import re
import sys

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
      pattern = r"USER \((\w+)\)$"
      result = re.search(pattern, line)
      if result is None:
        continue
       name = result[1]
      usernames[name] = usernames.get(name, 0) + 1
print(usernames)
