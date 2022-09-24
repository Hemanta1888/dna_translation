"""
    Translate a string containing a nucleotide sequence into a 
    string containing the corresponding sequence of amino acids . 
    Nucleotides are translated in triplets using the table dictionary; 
    each amino acid 4 is encoded with a string of length 1. 
"""

from .amino_acid_assosiate_protein import amino_acid_codeon_protein


class Translation:

    def __init__(self) -> None:
        self.protein = ''

    def collect_protein_info(self, dna_sequence):
        """Take dna sequence as parameter and found the amino acid abbreviations"""

        protein = ''
        if len(dna_sequence) % 3 == 0:
            for i in range(0, len(dna_sequence), 3):
                codeon = dna_sequence[i:i+3]
                protein += amino_acid_codeon_protein[codeon.upper()]
        self.protein = protein[:-1]
        return protein[:-1]

    def __eq__(self, protein: object) -> bool:
        """matched the real protein with the protein we found"""

        return self.protein == protein
             
