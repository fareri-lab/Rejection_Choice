getwd()

setwd("/Users/dfareri/Dropbox/Dominic/Github/fareri-lab/Rejection_Choice/")

data<-read.csv(file="longformdata_DF.csv",header=TRUE, sep=',')

short_data<-read.csv(file="shortformdata_DF.csv",header=TRUE,sep=",")

data$condition_recode[data$condition_recode==2]<- -1
unique(data$condition_recode)

data$playlottery[data$playlottery==999]<-NA
test<-lm(short_data$choice~short_data$condition_recode)
summary(test)

glmer1<-glmer(playlottery~condition_recode + age + sex + timebetween + order + (1|PROLIFIC_ID),family=binomial,data=data)
summary(glmer1)

glm1<-glm(playlottery~condition_recode + age + sex + timebetween + order,family=binomial,data=data)

plot_model(glm1,type=c("pred"),axis.title = c('Social Condition','Predicted Probability of Playing Lottery'),title='',colors=("circus"),mrdt.values="meansd")

