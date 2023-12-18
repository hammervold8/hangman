import re

def fjern_ikke_bokstaver(ordliste):
    # Fjern ord som inneholder noe annet enn bokstaver
    return [ord for ord in ordliste if re.match('^[a-zA-Z]+$', ord)]

def hovedprogram(input_fil, output_fil):
    try:
        # Leser innholdet fra input-filen
        with open(input_fil, 'r', encoding='utf-8') as fil:
            innhold = fil.read().split()

        # Fjerner ord som inneholder noe annet enn bokstaver
        filtrert_innhold = fjern_ikke_bokstaver(innhold)

        # Lagrer det endrede innholdet i output-filen
        with open(output_fil, 'w', encoding='utf-8') as fil:
            fil.write('\n'.join(filtrert_innhold))

        print(f"Programmet kjørte vellykket. Resultatet er lagret i {output_fil}")

    except FileNotFoundError:
        print(f"Filen '{input_fil}' ble ikke funnet.")
    except Exception as e:
        print(f"Noe gikk galt: {e}")

# Eksempel på bruk:
input_fil = '/Users/aleksanderhammervold/Library/CloudStorage/OneDrive-Trøndelagfylkeskommune/VG2/Matte R1/programmering/hangman/wordlist.txt'  # Erstatt med navnet på din input-fil
output_fil = 'hangman/output.txt'  # Erstatt med ønsket navn på output-filen

hovedprogram(input_fil, output_fil)
