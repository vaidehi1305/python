
mydata = read.csv("C:/Users/Vaidehi Deshpande/Documents/vaidehi/NEU/Subjects/classFile.csv")

min(mydata[,2])

max(mydata[,2])

median(mydata[,2])

mean(mydata[,2])

min(mydata[,3])

max(mydata[,3])

median(mydata[,3])

mean(mydata[,3])

v = mydata[,4]

getmode <- function(v) {
     uniqv <- unique(v) 
 uniqv[which.max(tabulate(match(v, uniqv)))]
 }

result <- getmode(v)

print(result)

table(mydata[,7])

countData <- table(mydata[,7])

percent <- countData/sum(countData)

print(percent)

dataStudent <- mydata[,8]

newStudent <- subset(dataStudent, dataStudent>500)

resultStudent <-length(newStudent)

print(resultStudent)

InterQuarterSalary <- mydata[,9]

IQR(InterQuarterSalary, na.rm = "True")


