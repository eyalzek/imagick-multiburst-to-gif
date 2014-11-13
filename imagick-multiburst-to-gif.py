#!/usr/bin/python
import os
import sys
import subprocess, shlex

print("test")
try:
	ticks = str(sys.argv[1])
except IndexError:
	ticks = "50"

crop_action = "convert -crop 320x240 {} shot-%02d.JPG"
gif_action = "convert -delay " + ticks + " shot-*.JPG {}.gif"
mv_action = "mv {} processed/"

if not os.path.exists("processed"):
	os.makedirs("processed")

def run_cmd(cmd):
	p = subprocess.Popen(cmd)
	p.wait()

files = [x for x in os.listdir(".") if ".JPG" in x or ".jpg" in x]
for f in files:
	run_cmd(shlex.split(crop_action.format(f)))
	run_cmd(shlex.split(gif_action.format(f.split(".")[0])))
	run_cmd(shlex.split(mv_action.format(f)))

	# remove shot-* files
	tmp = [x for x in os.listdir(".") if "shot-" in x]
	for i in range(len(tmp)):
		os.remove(tmp[i])
