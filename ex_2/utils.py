import os

def delete_a_record(sid, filename):
	with open(filename , "r") as fr, open(filename+"1", "w") as fw:
		
		sid = str(sid)

		for line in fr.readlines():
			line_s = line.split(",")
			if sid not in line_s:
				fw.write(line)

	with open(filename+"1", "r") as fr, open(filename, "w") as fw:
		fw.write(fr.read())

	os.system("rm "+filename+"1")




