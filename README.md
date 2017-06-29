# TaxonToGenome

This script should allow to download ncbi genomes by providing taxon ids.

## Requirements

* Python 3.4

* libraries stated in [requirements.txt](requirements.txt)

## Installation

### With virtualenv

1.Fetch the repository 

~~~Bash
wget https://github.com/pbelmann/TaxonToGenome/archive/master.zip && unzip master.zip && cd TaxonToGenome-master
~~~

2.Install python 3.5

~~~Bash
virtualenv vendor -p python3.5
~~~

3.Activate python

~~~BASH
source  vendor/bin/activate
~~~

4.Install all libraries

~~~BASH
pip install -r requirements.txt
~~~

(**Note** Dont forget to deactivate after usage by typing 'deactivate' )

You can test the successful installation by running:

~~~BASH
behave
~~~

### Without virtualenv

1.Fetch the repository 

~~~Bash
wget https://github.com/pbelmann/TaxonToGenome/archive/master.zip && unzip master.zip && cd TaxonToGenome-master
~~~

2.Install all libraries with

~~~BASH
pip install -r requirements.txt
~~~

You can test the successful installation by running the following command inside the project directory:

~~~BASH
behave
~~~


## How to use

~~~BASH
usage: database_request.py [-h] -i INPUT -e EMAIL -o OUTPUT [--store-all]

Fetch Genomes By Providing Taxonomy Ids.

optional arguments:
  -h, --help   show this help message and exit
  -i INPUT     Input csv file containing taxonomy ids.
  -e EMAIL     Email for accessing Entrez.
  -o OUTPUT    Output directory for storing the fasta files.
  --store-all  Download all strains.
~~~

On a successful run the following folder structure will be created inside the output directory:

~~~BASH
output/taxonomy_id/genome_id/nuccore_id.fasta
~~~

For example

~~~BASH
output/926566/3572/390955930.fasta
output/926566/3572/390410848.fasta
output/1198114/13764/322836736.fasta
~~~

Inspect [this](features/usage.feature) file for example usage.
