print("      ** PROGRAM MENGHITUNG NILAI AKHIR **")
print("     ------------------------------------------")
print("")

nilai = 1

while nilai == 1:

	nama  =str(input("MASUKAN NAMA        :"))
	nim   =int(input    ("MASUKAN NIM         :"))
	print("")
	uts   =int(input    ("MASUKAN NILAI UTS   :"))
	uas   =int(input    ("MASUKAN NILAI UAS   :"))
	tugas =int(input     ("MASUKAN NILAI TUGAS :"))

	uts=uts*40/100;
	uas=uas*40/100;
	tugas=tugas*20/100;
	nilai_akhir=uts+uas+tugas;

	print("")
	print("         * HASIL NILAI AKHIR *")
	print("        ---------------------------")
	print("")

	print("NAMA         :%s"%nama)
	print("NIM          :%s"%nim)
	print("NILAI UTS    :%d"%uas)
	print("NILAI UAS    :%d"%uts)
	print("NILAI TUGAS  :%d"%tugas)
	print("")
	print("HASIL NILAI AKHIR:", (nilai_akhir))
	print("")
	
	if nilai_akhir >=80:
	    print ("NILAI HURUF  : A")
	elif nilai_akhir >=70:
	    print ("NILAI HURUF  : B")
	elif nilai_akhir >=55:
	    print ("NILAI HURUF : C")
	elif nilai_akhir >=40:
	    print ("NILAI HURUF  : D")
	elif nilai_akhir >=39:
	    print ("NILAI HURUF : F")

	if nilai_akhir >=60:
	    print ("KETERANGAN : LULUS")
	else :
	    print ("KETERANGAN : TIDAK LULUS")

	print()
	nilai = int(input("Masukkan angka (ulangi=1, berhenti=0): " ))

	if nilai == 0:
		break
	elif nilai == 1:
		pass