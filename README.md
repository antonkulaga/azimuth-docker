Docker image for Azimuth CRISPR tool
====================================

This is a docker tool for Azimuth tool that computes the scores for CRISPR-CAS9 guideRNA design.
The sources of this docker-container are at https://github.com/antonkulaga/azimuth-docker
The github repository contains two containers: azimuth (console one) and azimuth-server - flask server to answer to queries

Running azimuth container
--------------------------
Make sure that [Docker](https://docs.docker.com/engine/installation/linux/) is installed. Then run the container and give it a list of DNA sequences where you want to make a cut. The sequences should be 30nt long and contain NGG sequence. Why 30nt is not clear for me, for details look at official github https://github.com/MicrosoftResearch/Azimuth

Here is a usage example:
```bash
sudo docker run compbioaging/azimuth ACAGCTGATCTCCAGATATGACCATGGGTT CAGCTGATCTCCAGATATGACCATGGGTTT CCAGAAGTTTGAGCCACAAACCCATGGTCA
```
It should return something like:
```
(u'ACAGCTGATCTCCAGATATGACCATGGGTT', 0.67229819690718751)
(u'CAGCTGATCTCCAGATATGACCATGGGTTT', 0.68794423702109719)
(u'CCAGAAGTTTGAGCCACAAACCCATGGTCA', 0.65924539040070207)
```

Azimuth server container
------------------------

Run:
```bash
sudo docker run -p 5000:5000 compbioaging/azimuth-server
```
to start the container. Then open http://127.0.0.1:5000 and send your sequences

