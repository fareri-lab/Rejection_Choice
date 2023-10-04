getwd()

setwd("/Users/jordansiegel/Documents/GitHub/Rejection_Choice")

data<-read.csv(file="longformdata_DF.csv",header=TRUE, sep=',')

short_data<-read.csv(file="shortformdata_DF.csv",header=TRUE,sep=",")

test<-lm(short_data$choice~short_data$condition_recode)
summary(test)

glm1<-glmer(playlottery~condition_recode + age + sex + timebetween + order + (1|PROLIFIC_ID),family=binomial,data=data)
summary(glm1)

data$condition_recode[data$condition_recode==2]<- -1
unique(data$condition_recode)

plot_model(glm1,type=c("pred"))