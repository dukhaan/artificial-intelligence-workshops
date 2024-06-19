from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

#Hierarki atau tree dari penyakit gastro usus
bagansakit=[
    [0,1,2,3,9], #20,21,22,23,29
    [0,1,2,4,10], #20,21,22,24,30
    [0,1,2,5,6,9], #20,21,22,25,26,29
    [1,7,11], #21,27,31
    [8,2,5,12] #28,22,25,32
]
bagangejala=[
    [1,2,4,5],
    [4,5,6],
    [4,7],
    [4,8,9],
    [8,10],
    [4,5,9,11],
    [4,8,11,12],
    [4,13],
    [1,2,3,4],
    [14,15],
    [14,16],
    [14,17],
    [18,19]
]
penyakit=[
    "Staphylococcus aureus",
    "Jamur beracun",
    "Salmonellae",
    "Clostridium botulinum",
    "Campylobacter"
]


#tampilan form gejala
txtgejala = [
    "1. Sering mengalami buang air besar (> 2 kali)?",
    "2. Mengalami berak encer?",
    "3. Mengalami berak berdarah?",
    "4. Merasa lesu dan tidak bergairah?",
    "5. Tidak selera makan?",
    "6. Merasa mual dan sering muntah (lebih dari 1 kali) ?",
    "7. Merasa sakit di bagian perut ?",
    "8. Tekanan darah anda rendah ?",
    "9. Anda merasa pusing ?",
    "10. Anda mengalami pingsan ?",
    "11. Suhu badan anda tinggi ?",
    "12. Mengalami luka di bagian tertentu ?",
    "13. Tidak dapat menggerakkan anggota badan tertentu ?",
    "14. Pernah memakan sesuatu ?",
    "15. Memakan daging ?",
    "16. Memakan jamur ?",
    "17. Memakan makanan kaleng ?",
    "18. Membeli susu ?",
    "19. Meminum susu ?"
]
i=0
var = {}
while i < len(txtgejala):
  var[i] = widgets.Checkbox(
    value=False,
    description=txtgejala[i],
    disabled=False,
    indent=False
    )
  display(var[i])
  i+=1

threshold = widgets.FloatText(
    value=20,
    description='Th(%): ',
    disabled=False
)
threshold.layout = widgets.Layout(width='150px')
display(threshold)

################################################################
#TUGAS: TULISLAH CODING ALGORITMA ANDA DISINI
#Fungsi Proses Sistem Pakarnya menggunakan prosentase
def proses(button):
    jawaban = {}
    for i in range(len(var)):
        jawaban[i] = var[i].value

    target = [0.0] * len(penyakit)
    sakit = [0.0] * len(bagangejala)

    for i in range(len(bagangejala)):
        for j in bagangejala[i]:
            if jawaban[j - 1]:
                sakit[i] += 100 / len(bagangejala[i])

    for i in range(len(bagansakit)):
        for j in bagansakit[i]:
            target[i] += (100 / len(bagansakit[i])) * (sakit[j] / 100)

    threshold_val = threshold.value

    output = ""
    max_percentage = 0.0
    max_index = 0

    for i in range(len(target)):
        output += f"{penyakit[i]} : {target[i]:.2f} %\n"
        if target[i] > max_percentage:
            max_percentage = target[i]
            max_index = i

    print(output)

    if max_percentage >= threshold_val:
        print(penyakit[max_index])
    else:
        print("none")

  #proses perhitungan prosentase

######################################################################

#tombol proses
#tombol proses
button = widgets.Button(
    description='Proses',
    disabled=False,
    button_style='success',
    tooltip='Proses Gejala Gastro-Usus'
)
display(button)
button.on_click(proses)
