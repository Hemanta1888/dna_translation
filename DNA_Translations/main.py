from Translations.read_file import ReadFile
from Translations.translations import Translation


if __name__ == '__main__':
    inputfile = 'dna_sequence.txt'
    protein_file= 'protein_data.txt'
    files_data = ReadFile(inputfile, protein_file)
    seq = files_data.read_dna_sequence()
    protein = files_data.read_protein()
    translation = Translation()
    collect_protein = translation.collect_protein_info(seq)
    match_protein = translation.__eq__(protein)
    print(collect_protein)
    print(match_protein) #To check weather the protein is matching with real protein or not