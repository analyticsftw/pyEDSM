""" A simple script to process Elite: Dangerous system dumps from EDSM
"""
__author__      = "Julien Coquet"
__copyright__   = "Copyright 2016-2019, MIT License"

import csv, fnmatch, json, math, os, sys, progressbar

def main():
  # Define path to JSON files
  path = "./edsm"
  bc = 0

  #Find number of logs in logs folder
  lc = 0
  list_dir = []
  list_dir = os.listdir(path)
  maxSystems = len(list_dir)
  fcount = 0
  logcount = 0
  sheader = ["system","body","type","subType","temp","radius","absMagnitude","solMass","spectralClass","luminosity"]
  print ("opening file")
  fp = open('bodies.csv', 'w')
  writer = csv.writer(fp)
  writer.writerow(sheader)

  with progressbar.ProgressBar(max_value=maxSystems) as bar:
      for fileItem in os.listdir(path):
          if fnmatch.fnmatch(fileItem, '*.json'):

              with open(path+"/"+fileItem, encoding='utf-8') as file:
                  lines=file.readlines()
                  status = "system"
                  for line in lines:
                      bc+= 1
                      thisline = json.loads(line)
                      sname=thisline['name']
                      bodies = thisline['bodies']
                      for body in bodies:
                          if body['type']!= "Star":
                              continue
                          bc+= 1
                          sbody = [
                              sname,
                              body['name'],
                              body['type'],
                              body['subType'],
                              str(body['surfaceTemperature']),
                          ]
                          if "solarRadius" not in body:
                              sbody.append("")
                          else:
                              sbody.append(str(body["solarRadius"]) )
                          if "absoluteMagnitude" not in body:
                              sbody .append("")
                          else:
                              sbody.append(str(body["absoluteMagnitude"]) )
                          if "solarMasses" not in body:
                              sbody.append("")
                          else:
                              sbody.append(str(body["solarMasses"]) )
                          if "spectralClass" not in body:
                              sbody.append("")
                          else:
                              sbody.append(str(body["spectralClass"]))
                          if "luminosity" not in body:
                              sbody.append("")
                          else:
                              sbody.append(body["luminosity"])

                          writer.writerow(sbody)
              lc += 1
              bar.update(lc)

if __name__ == '__main__':
  main()
