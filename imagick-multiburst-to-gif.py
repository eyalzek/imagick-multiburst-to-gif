#!/usr/bin/python
import os
import subprocess, shlex

crop_action = "convert -crop 320x240 {} shot-%02d.JPG"
gif_action = "convert -delay 30 shot-*.JPG {}.gif"

files = [x for x in os.listdir(".") if ".JPG" in x]
for f in files:
	cmd = shlex.split(crop_action.format(f))
	p1 = subprocess.Popen(cmd)
	p1.wait()

	cmd = shlex.split(gif_action.format(f.split(".")[0]))
	p2 = subprocess.Popen(cmd)
	p2.wait()

	tmp = [x for x in os.listdir(".") if "shot-" in x]
	for i in range(len(tmp)):
		os.remove(tmp[i])
