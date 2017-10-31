# -*- coding: utf-8 -*-
"""
AUTOMATIC TRIBE CHARACTERISATION

Created on Wed Oct  5 11:46:59 2016
@author: Andris
"""
from charTools3 import retrieveAll, findIndividuals, clusterData
from helpFiles import printToCSV as save
from collections import Counter
import sys
import os

if __name__ == '__main__':

	# -----------------------------------------------------------------------
	# SET-UP
	# -----------------------------------------------------------------------

	folderList 	= sys.argv[1]
	N_CLUSTERS 	= int(sys.argv[2])
	limits     	= [-float(sys.argv[3]), float(sys.argv[3])]
	clusterThemes   = sys.argv[4]
	search = [0,1,2]; # Look for individuals/corporate	

	themesToAnalyse = clusterThemes;

	print 'Cycling through each file in the directory ' + folderList
	files = [f for f in os.listdir(folderList) if not os.path.isfile(os.path.join(folderList, f))];
	for folderName in files:

		# -----------------------------------------------------------------------
		# READ ALL DATA
		# -----------------------------------------------------------------------
		print folderName
		data = retrieveAll(folderList+'/'+folderName)
		users = list(data.keys());
		themes = list(data[users[0]].keys());

		# -----------------------------------------------------------------------
		# FIND INDIVIDUALS/CORPORATE
		# -----------------------------------------------------------------------

		# 0 corresponds to individual, 1 to company, 2 to unknown.
		# Limits array (last argument, controls the quantity of unknown)  
		check = findIndividuals(data,limits)
		classDict = check[0]; # User classification
		composition = check[1]; # Total composition

		# -----------------------------------------------------------------------
		# CLUSTER ACCORDING TO CERTAIN THEMES
		# -----------------------------------------------------------------------

		# Create dicitonary of desired values
		dataForCluster = {};
		for user in users:

			if classDict[user] in search:
			
				themeArray = {};    
				for theme in data[user].keys():
					if theme in clusterThemes:            
						themeArray[theme] = (data[user][theme]);
					
				
				dataForCluster[user] = themeArray;


		legends = dataForCluster[list(dataForCluster.keys())[0]].keys();
		# Update dictionary with cluster number 
		clusterDict = clusterData(dataForCluster,N_CLUSTERS)



		# Update dictionary with individuals check
		for item in clusterDict:
			clusterDict[item].append({'Corporate?':classDict[item]})


		# -----------------------------------------------------------------------
		# LABELLING EACH CLUSTER
		# -----------------------------------------------------------------------

		clusterTotalScore = {};
		clusterUsers = {};
		for it in range(N_CLUSTERS):
			clusterTotalScore[it] = [];
			clusterUsers[it] = [];

		for item in clusterDict:

			currentName = item;
			currentCluster = clusterDict[currentName][1]['Cluster'];    
			currentScore = clusterDict[currentName][0]['Scores']
		 
			clusterTotalScore[currentCluster].append(currentScore); 
			clusterUsers[currentCluster].append(item); 
				
		totalScore = {};
		for item in clusterTotalScore:
			
			# Fresh dictionary
			keys = clusterTotalScore[0]
			newDict = {};
			for theme in legends:
				newDict[theme] = 0;
				
			A = Counter(newDict);    
			
			for element in clusterTotalScore[item]:
				
				B = Counter(element);
				
				A += B;
			
			totalScore[item] = (dict(A))
					

		# -----------------------------------------------------------------------
		# POSTPROCESSING/SAVE RESULTS
		# -----------------------------------------------------------------------

		# Reorder dictionaries so that the larger items come first
		order = [];
		for key in totalScore: 
			
			a = totalScore[key]
			items = [(v, k) for k, v in a.items()]
			items.sort();
			items.reverse()
			items = [(k, v) for v, k in items]
			order.append(items)
				

		def filterIt(order,themes):
			new = [];    
			for cluster in order:
				bleh= [];
				for term in cluster:        
					theme = term[0];        
					if theme in themes:            
						bleh.append((term[0],int(term[1])));            
				new.append(bleh[0:5])
			return new

		overallOrder = filterIt(order,themesToAnalyse)


		# Saving information

		csvName = folderList+'/'+folderName+'/clusterLabeled.csv';

		save(csvName,
			 ['Cluster ID','Total','Users'],
		range(N_CLUSTERS),overallOrder,clusterUsers.values())

		csvName = folderList+'/'+folderName+'/tribeUserInfo.csv';
		clusterInfo = [term[1]['Cluster'] for term in clusterDict.values()]

		"""
		save(csvName,
			 ['Users','Ind/Comp/Unknown'],
		classDict.keys(),classDict.values(),clusterInfo)
		"""
		




