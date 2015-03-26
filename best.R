best <- function(state,outcome){

## check if state and outcome are valid values
outcome <- tolower(outcome)
if (outcome ==  'heart attack' || outcome == 'heart failure' ||
outcome == 'pneumonia') { 


	## Read the csv file into a dataframe
	careDF <- read.csv("outcome-of-care-measures.csv",colClasses= c(rep("character",2),rep("NULL",4), "character",rep("NULL",3),"character",rep("NULL",5),"character", rep("NULL",5),"character",rep("NULL",23)),header= TRUE)
	
	## check if state is valid value
	if (nrow(careDF[careDF$State %in% c(state), ]) > 0) {
		careDF <- careDF [careDF[3] == state,]
		## Customize and set the column names
		colnames(careDF)[4] <- 'HeartAttack'
		colnames(careDF)[5] <- 'HeartFailure'
		colnames(careDF)[6] <- 'Pneumonia'
		careDF <- careDF[order(careDF[,4],careDF[,2]),]
		head(careDF$Hospital.Name,1)

	}
	else{

	## print invalid state value
	stop(	"Invalid state")
	
	}

}
else{
	##print invalid outcome value
	stop("invalid outcome")	

}
}
