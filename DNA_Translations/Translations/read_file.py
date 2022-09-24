"""
    Read the dna sequence and protein data file.
    Return the datasets
"""

class ReadFile:

    def __init__(self, dna_seq_data, protein_data) -> None:
        self.dna_sequence = dna_seq_data
        self.protein_data = protein_data
    
    def read_dna_sequence(self):
        """Read the dna sequence file and return the sequence data"""

        with open(self.dna_sequence, 'r') as file:
            seq = file.read()
        seq = seq.replace("\n", '').replace("\r", "").replace(" ","")

        return seq

    def read_protein(self):
        """Read the protein file and return the protein data"""

        with open(self.protein_data, 'r') as file:
            protein = file.read()
        protein = protein.replace("\n", '').replace("\r", "")

        return protein