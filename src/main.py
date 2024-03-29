
from functions import read_txt, read_cli, process, output_cli, output_txt
import time

print("|------------------------------------------|")
print("|----          SELAMAT DATANG          ----|")
print("|----     DI CYPERBUNK 2077 BREACH     ----|")
print("|----          PROTOCOL SOLVER         ----|")
print("|------------------------------------------|\n")
print("Silakan pilih metode masukan yang diinginkan \n")
print("| 1 | Metode TXT: dengan memasukkan file '.txt'")
print("| 2 | Metode CLI: dengan masukan dari command line")

metode = 999
while metode != 1 and metode != 2:
    try:
        metode = int(input("\nMetode yang dipilih: "))
        if metode == 1:
            bufferSize, matrix, sequences, rewards = read_txt()
        elif metode == 2:
            bufferSize, matrix, sequences, rewards = read_cli()
        else:
            print("\nPilih antara 1 dan 2")
            print("| 1 | Metode TXT: dengan memasukkan file '.txt'")
            print("| 2 | Metode CLI: dengan masukan dari command line")
    except ValueError:
        print("\nMasukan harus berupa angka antara 1 dan 2. Silakan coba lagi.")


if bufferSize != None:
    start = time.time()
    reward_solution, array_solution, steps_solution = process(bufferSize, matrix, sequences, rewards)
    end = time.time()
    process_time = end - start

    print("\nSolusi dari data yang telah didapatkan adalah:")
    output_cli(reward_solution, array_solution, steps_solution, process_time)

    save = input("\nApakah ingin menyimpan solusi? (Y/N) ")
    if save.upper() == 'Y':
        name = input("\nMasukkan nama untuk file solusi yang hendak disimpan: ")
        output_txt(reward_solution, array_solution, steps_solution, process_time, name)
    else:
        print("\n|----          SEE YOU SOON!!          ----|")