import os, time
source = ['"/home/tlxy/dana"', '"/home/tlxy/learngit"']
target_dir = '/home/tlxy/myzip'
if not os.path.exists(target_dir):
    os.system("mkdir /home/tlxy/myzip")
today = target_dir + os.sep + time.strftime("%Y-%m-%d")
now = time.strftime("%H:%M:%S")
comment = input("please enter your comment->")
if len(comment ) ==0:
    target = today + os.sep + now + '.zip'
else:
    target = today +os.sep + now + '-' + \
    comment.replace(' ', '_') + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print("Successfully created dirctory", today)

zip_command = "zip -qr {0} {1}".format(target, " ".join(source))
if os.system(zip_command) == 0:
    print("Successfully backup to", target)
else:
    print("Backup FAILED")