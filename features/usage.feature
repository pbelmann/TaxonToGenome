Feature: Run the cli

  Scenario: Run basic command
    Given the output directory exists
    When  I run database request with the commands "-e pbelmann@web.de -i input/taxids.csv -o output"
    Then the following files should be available:
      """
      output/926566/3572/390955930.fasta
      output/1198114/13764/322836736.fasta
      """

  Scenario: Report all strains
    Given the output directory exists
    When  I run database request with the commands "-e pbelmann@web.de -i input/taxids.csv -o output --store-all"
    Then the following files should be available:
      """
      output/926566/3572/390955930.fasta
      output/926566/3572/390410848.fasta
      output/1198114/13764/322836736.fasta
      """