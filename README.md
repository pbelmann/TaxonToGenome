# TaxonToGenome

This script should allow to download ncbi genomes by providing taxon ids.

## Requirements

* Python 3.4

* libraries stated in [requirements.txt](requirements.txt)

## Installation

### With virtualenv

1.Fetch the repository 

~~~Bash
wget https://github.com/pbelmann/TaxonToGenome.git && cd TaxonToGenome
~~~

2.Install python 3.4

~~~Bash
virtualenv vendor -p python3.4
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

Install all libraries with

~~~BASH
pip install -r requirements.txt
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
  --store-all  Download just one strain.
~~~

Inspect [this](features/usage.feature) file for example usage.
