from Bio import Entrez
from Bio import SeqIO
import csv
import argparse
import os.path
import sys
import pprint


def read_in_tax_ids(path):
    with open(path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=' ')
        return [item for sublist in list(csv_reader) for item in sublist]


def search_nuccore_ids(genome_ids):
    handle = Entrez.elink(dbfrom="genome", db="nuccore", id=genome_ids)
    nuccore_ids = Entrez.read(handle)
    return nuccore_ids


def search_taxonomy_ids(taxonomy_ids):
    handle = Entrez.elink(dbfrom="taxonomy", db="genome", id=taxonomy_ids)
    genome_ids = Entrez.read(handle)
    return genome_ids


def fetch_fasta(ids):
    hdl = Entrez.efetch(db="nuccore", id=ids, retmode="text", rettype="fasta")
    genome_ids = list(SeqIO.parse(hdl,'fasta'))
    return genome_ids


def write_fasta(genome_ids, path):
    w_hdl = open(path, "w")
    SeqIO.write(genome_ids, w_hdl,'fasta')
    w_hdl.close()


def parse_arguments(args):
    def is_valid_path(path):
        if not os.path.exists(path):
            raise argparse.ArgumentTypeError("The file %s does not exist!" % path)
        else:
            return path

    parser = argparse.ArgumentParser(description='Fetch Genomes By Providing Taxonomy Ids.')
    parser.add_argument('-i', dest='input', help='Input csv file containing taxonomy ids.',
                        required=True, type=is_valid_path)
    parser.add_argument('-e', dest='email', help='Email for accessing Entrez.', required=True)
    parser.add_argument('-o', dest='output', help='Output directory for storing the fasta files.',
                        required=True, type=is_valid_path)
    parser.add_argument('--store-all', dest='store_all', help='Download just one strain.',
                        action='store_true', required=False, default=False)
    return parser.parse_args(args)


def main(argv):
    args = parse_arguments(argv)
    Entrez.email = args.email
    output_dir = args.output
    store_all = args.store_all
    tax_ids = read_in_tax_ids(args.input)
    genome_ids = search_taxonomy_ids(tax_ids)

    pp = pprint.PrettyPrinter(indent=4)

    filtered_genome_ids = dict(map(lambda x: (x["IdList"][0], x["LinkSetDb"][0]["Link"][0]["Id"]), genome_ids))

    print("\nFound the following tax ids - genome ids")
    pp.pprint(filtered_genome_ids)

    nuccore_ids = search_nuccore_ids(list(filtered_genome_ids.values()))
    filtered_nuccore_ids = dict(map(lambda x: (x["IdList"][0], [genome["Id"] for genome in x["LinkSetDb"][0]["Link"]]), nuccore_ids))

    print("\nFound the following genome ids - nuccore ids")
    pp.pprint(filtered_nuccore_ids)

    for tax_id in tax_ids:
        #genome id has a one to one relation to taxId
        genome_id = filtered_genome_ids[tax_id]
        nuccore_id_list = filtered_nuccore_ids[genome_id]

        nuccore_id_counter = len(nuccore_id_list)
        print("\nFetching "
              + (" {} nuccore ids ".format(nuccore_id_counter) if store_all else " one out of {} ".format(nuccore_id_counter))
              + " of genome id: {} ".format(genome_id))

        for nuccore_id in nuccore_id_list:
            path_to_genome_id_folder = os.path.join(output_dir, tax_id, genome_id)
            os.makedirs(path_to_genome_id_folder, exist_ok=True)
            print("\nStarting to fetch the fasta of nuccore id: {} ".format(nuccore_id))
            fasta = fetch_fasta(nuccore_id)
            write_fasta(fasta, os.path.join(path_to_genome_id_folder, nuccore_id + ".fasta"))
            if not store_all:
                break

if __name__ == "__main__":
    main(sys.argv[1:])