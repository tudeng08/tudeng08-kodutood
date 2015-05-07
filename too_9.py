#!/usr/bin/env python3
"""
Programm loeb etteantud valgu FASTA faili ning arvutab valgu vastavaid parameetreid.
"""

__author__ = "Maria F"
__copyright__ = "Copyright 2015, Minufirma"
__credits__ = ["Maria Fomitsenko", "Friend1", "Friend2"]
__version__ = "0.001"
__email__ = "mariafomit@ya.ru"

from Bio import SeqIO
from Bio.SeqUtils import ProtParam


def read(fasta): # loeb etteantud FASTA faili
    for seq_record in SeqIO.parse(fasta, "fasta"):
        print("Kirjeldus:",seq_record.description)
        print("Järjestus:",seq_record.seq)
    return(seq_record.seq)
    
def main(): #programm, mis annab kasutajal sisestada tahetut FASTA faili ning arvutab vastavaid parameetreid
    fasta = input() # kysib FASTA faili nime
    sequence = read(fasta)
    from_fasta = ProtParam.ProteinAnalysis(str(sequence))
    
    #need print-laused annavad kohe vastuse konsooli
    print("\n","Valgu pikkus:",len(sequence))
    print("\n","Molekulaarmass:",from_fasta.molecular_weight())
    print("\n","Stabiilsuse indeks:",from_fasta.instability_index())
    print("\n","Aromaatsus:",from_fasta.aromaticity())
    print("\n","Aminohappeid:",from_fasta.count_amino_acids())
    print("\n","Isoelektriline punkt:",from_fasta.isoelectric_point())
          
    """järgnev annab vastuse eraldiseisvasse faili, kahjuks write funktsioon laseb kirjutada ühe argumendi kaupa, seega iga reavahe on eraldi väljakirjutatud """
   
    text_file = open("Fasta_analyys.txt", "w")
    text_file.write("\n Length = ")
    text_file.write(str(len(sequence)))
    text_file.write("\n MW = ")
    text_file.write(str(from_fasta.molecular_weight()))
    text_file.write("\n Index = ")
    text_file.write(str(from_fasta.instability_index()))
    text_file.write("\n Aromaticity = ")
    text_file.write(str(from_fasta.aromaticity()))
    text_file.write("\n aa = ")
    text_file.write(str(from_fasta.count_amino_acids()))
    text_file.write("\n pI = ")
    text_file.write(str(from_fasta.isoelectric_point()))
    text_file.close()

if __name__ == "__main__":
    main()