rankall <- function(outcome,num="best"){

## check if state and outcome are valid values
outcome <- tolower(outcome)
if (outcome ==  'heart attack' || outcome == 'heart failure' ||
outcome == 'pneumonia') { 


	## Read the csv file into a dataframe
	careDF <- read.csv("outcome-of-care-measures.csv",colClasses= c(rep("character",2),rep("NULL",4), "factor",rep("NULL",3),"character",rep("NULL",5),"character", rep("NULL",5),"character",rep("NULL",23)),header= TRUE)
	
	## check if state is valid value
		
		## Customize and set the column names
		colnames(careDF)[4] <- 'heart attack'
		colnames(careDF)[5] <- 'heart failure'
		colnames(careDF)[6] <- 'pneumonia'

		careDF <- careDF [careDF[outcome] != 'Not Available' ,]

		x <- 4
		if (outcome ==  'heart attack') {
			x <- 4
			careDF[,x] <- sapply(careDF[,x],as.numeric)

		}
		else if(outcome == 'heart failure'){
			x <- 5
			careDF[,x] <- sapply(careDF[,x],as.numeric)

		}
		else if (outcome == 'pneumonia') {
			x <- 6
			careDF[,x] <- sapply(careDF[,x],as.numeric)

		}

		
		
		if (num == "worst"){
		
			careDF <- careDF[order(-xtfrm(careDF[,x]),careDF[,2]),]
		}
		else if (num == "best"){
			print ('commg hjere')
			careDF <- tapply(careDF[,x],careDF[,2],min)
			##careDF <- careDF[order(careDF[,x], careDF[,2]),]

		}
		else{
			## take the specified element.
			print ('coming here')
			careDF <- careDF[order(careDF[,x],careDF[,2]),]
			## filter based on num
			careDF <- careDF[num,]

		}
		##head(careDF$Hospital.Name,1)
		careDF
	
}
else{
	##print invalid outcome value
	print ("Invalid outcome")
}
}
