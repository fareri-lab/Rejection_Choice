
library(lme4)
library(lmerTest)

getwd()

setwd("/Users/dfareri/Dropbox/Dominic/Github/fareri-lab/Rejection_Choice/")

data<-read.csv(file="longformdata_DF.csv",header=TRUE, sep=',')

short_data<-read.csv(file="shortformdata_DF.csv",header=TRUE,sep=",")

#recode variables so 0 = neutral, 1 = rejection, -1 = acceptance
#original coding: 0 = neutral, , 1 =rejection, 2 = acceptance

data$condition_recode[data$condition_recode==2]<- -1
unique(data$condition_recode)


#recode order from 12 (rejection first) to 0 and 21 (acceptance first) to 1
data$order[data$order==12]<-0
data$order[data$order==21]<-1

#convert missed trials from 999 to NA
data$playlottery[data$playlottery==999]<-NA
test<-lm(short_data$choice~short_data$condition_recode)
summary(test)

glmer1<-glmer(playlottery~condition_recode + age + sex + timebetween + order + (1|PROLIFIC_ID),family=binomial,data=data)
summary(glmer1)

glm1<-glm(playlottery~condition_recode + age + sex + timebetween + order,family=binomial,data=data)

glm4 <- glm(playlottery~recoded_stress*condition_recode + age + sex + timebetween + order,family=binomial,data=data)

plot_model(glm1,type=c("pred"),axis.title = c('Social Condition','Predicted Probability of Playing Lottery'),title='',colors=("circus"),mrdt.values="meansd")

plot_model(model=lm,type="int")

plot_model(model=lm, type = 'int', title = "",
           +            axis.title = c("Self-Reported Affect", "Likelihood to Share in Future"),
           +            colors = c("#0073C2FF", "#EFC000FF"),
           +            legend.title = "Social Condition",
           +            legend.labels = c("Acceptance", "Rejection"),
           +            show.values = TRUE,
           +            value.offset = 0.4,
           +            value.size = 4) + theme(
             +     panel.background = element_blank(),
             +     panel.grid.major = element_blank(),
             +     panel.grid.minor = element_blank(),
             +     plot.background = element_blank()
             + )

ggplot(data3, aes(x = condition_recode, y = playlottery)) +
  +     geom_point() +
  +     stat_smooth(method = "glm", color = "green", se = FALSE, 
                    +                 method.args = list(family = binomial)) +
  +     labs(x = "Condition Recode", y = "Play Lottery", title = "Logistic Regression with ggplot2") +
  +     theme_minimal()