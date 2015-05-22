import subprocess
import json
import collections
import random
import sys
import shlex
import p7_visualize


sub1 = subprocess.Popen(shlex.split("gringo level-core.lp level-style.lp level-sim.lp level-shortcuts.lp -c width=7"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
sub2 = subprocess.Popen(shlex.split("reify"), stdin = sub1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
sub3 = subprocess.Popen(shlex.split("clingo - meta.lp metaD.lp metaO.lp metaS.lp --parallel-mode=4 --outf=2"), stdin = sub2.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = sub3.communicate()
if err:
    print err

print p7_visualize.render_ascii_dungeon(p7_visualize.parse_json_result(out))

"""
command= shlex.split("gringo level-core.lp level-style.lp level-sim.lp level-shortcuts.lp -c width=7 | reify | clingo - meta.lp metaD.lp metaO.lp metaS.lp > example_noshortcut.json")
print command
yay = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = yay.communicate()
print out

if err:
    print err
    
print p7_visualize.parse_json_result(out)
"""
junk = """
return parse_json_result(out)

CLINGO = "./clingo-4.5.0-macos-10.9/clingo"

clingo = subprocess.Popen(
    [CLINGO, "--outf=2"] + list(args),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
out, err = clingo.communicate()
if err:
    print err
    
return parse_json_result(out)

# gringo level-core.lp level-style.lp level-sim.lp level-shortcuts.lp -c width=7 | reify | clingo - meta.lp metaD.lp metaO.lp metaS.lp --parallel-mode=4 --outf=2 > example_noshortcut.json
"""

