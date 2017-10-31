
def labelText(text,model,themes):

	labels = [];

	for it in range(len(text)):

		simIndex = {};

		for theme in themes:
		
			simVal = [];

			for token in text[it]:
			
				try:
					simVal.append(model.similarity(theme,token));
				except:

					continue;

			if len(simVal) > 0:
				simIndex[theme] = sum(simVal)/len(simVal);
			else:

				simIndex[theme] = 'NaN'


		labels.append(simIndex);



	return labels




