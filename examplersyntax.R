
library(lme4)
library(lmerTest)

getwd()

setwd("/Users/jordansiegel/Documents/Github/Rejection_Choice/")

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

learningglm<-glm(choice~chunk*condition_recode, data = learningdata)
summary(learningglm)

plot_model(model=learningglm,type="int")

learningmodel <-plot_model(model=learningglm,type="int")
learningmodel +
  +     theme_minimal() + # Remove the background
  +     scale_color_manual(values = c("blue", "red", "green")) + # Change the colors
  +     labs(title = "Customized Interaction Plot", x = "X1", y = "Predicted Y") # Customize label


#customizeplot
# Generate prediction data using ggpredict
pred_data <- ggpredict(maineffect_affect, terms = "recoded_stress")

# Plot the predictions using ggplot2
ggplot(pred_data, aes(x = x, y = predicted)) +
  geom_line(color = "#0073C2FF") +
  geom_ribbon(aes(ymin = conf.low, ymax = conf.high), alpha = 0.2, fill = "#0073C2FF") +
  labs(
    x = 'Self-Reported Affect',
    y = 'Predicted Probability of Playing Lottery',
    title = ''
  ) +
  theme_classic() +
  theme(
    panel.grid.major = element_blank(), # Remove major grid lines
    panel.grid.minor = element_blank(), # Remove minor grid lines
    axis.line = element_line(color = "black"), # Add axis lines
    panel.border = element_blank(), # Remove panel border
    plot.background = element_blank(), # Remove plot background
    panel.background = element_blank() # Remove panel background
  )

library(dplyr)

rej <- data %>% filter(condition_recode == 1)
acc <- data %>% filter(condition_recode == -1)

# Median split for 'rej' based on 'recoded_stress'
median_value_rej <- median(rej$recoded_stress, na.rm = TRUE)
rej <- rej %>%
  mutate(Group = ifelse(recoded_stress > median_value_rej, "Rej_Pos", "Rej_Neg"))

# Print result
print(rej)

# Median split for 'acc' based on 'recoded_stress'
median_value_acc <- median(acc$recoded_stress, na.rm = TRUE)
acc <- acc %>%
  mutate(Group = ifelse(recoded_stress > median_value_acc, "Acc_Pos", "Acc_Neg"))

# Print result
print(acc)

library(dplyr)
library(ggplot2)
library(scales)
library(tidyr)  # For drop_na()

# Step 1: Compute the Overall Median of `recoded_stress`
overall_median_stress <- median(data$recoded_stress, na.rm = TRUE)

# Step 2: Create a Binary Affect Group Based on Overall Median
data_withbins <- data %>%
  mutate(
    Group = case_when(
      recoded_stress > overall_median_stress ~ "Positive",  # Higher than median
      recoded_stress <= overall_median_stress ~ "Negative", # Lower than median
      TRUE ~ NA_character_
    )
  ) %>%
  drop_na(Group)  # Remove NA values

# Step 3: Create Prediction Dataset (Only Two Affect Groups & Two Conditions)
data_new <- expand.grid(
  Group = unique(data_withbins$Group),  # Two affect categories: Positive & Negative
  condition_recode = c(-1, 1),  # Only Acceptance (-1) and Rejection (1)
  age = mean(data_withbins$age, na.rm = TRUE),  
  sex = mean(data_withbins$sex, na.rm = TRUE),  
  timebetween = mean(data_withbins$timebetween, na.rm = TRUE),  
  order = mean(data_withbins$order, na.rm = TRUE) 
)

# Step 4: Assign Representative `recoded_stress` Values for Each Group
group_medians <- data_withbins %>%
  group_by(Group) %>%
  summarise(recoded_stress = median(recoded_stress, na.rm = TRUE), .groups = "drop")

# Merge median recoded_stress into prediction dataset
data_new <- left_join(data_new, group_medians, by = "Group") %>%
  drop_na(Group)  # Remove NA values

# Step 5: Predict Probabilities from GLM Model
pred <- predict(glm4, newdata = data_new, type = "link", se.fit = TRUE)

# Step 6: Add Predictions and Confidence Intervals
data_new$predicted_prob <- plogis(pred$fit)
data_new$lower_ci <- plogis(pred$fit - 1.96 * pred$se.fit)  # Lower bound
data_new$upper_ci <- plogis(pred$fit + 1.96 * pred$se.fit)  # Upper bound

# Step 7: Convert Factors for Plotting
data_new$condition_recode <- factor(data_new$condition_recode,
                                    levels = c(-1, 1), 
                                    labels = c("Acceptance", "Rejection"))

data_new$Group <- factor(data_new$Group, levels = c("Negative", "Positive"))

# Step 8: Create Bar Plot (Final Visualization)
ggplot(data_new, aes(x = Group, y = predicted_prob, fill = condition_recode)) +
  geom_bar(stat = "identity", position = position_dodge(), color = "black") +  # Bars
  geom_errorbar(aes(ymin = lower_ci, ymax = upper_ci),  # Error bars
                position = position_dodge(width = 0.9), width = 0.2, color = "black") +
  scale_y_continuous(labels = scales::percent_format(accuracy = 1)) +  # Format y-axis
  labs(
    x = "Self-Reported Affect",
    y = "Predicted Probability of Playing Lottery",
    fill = "Condition") +
  theme_minimal() +
  theme(panel.grid = element_blank())+
  scale_fill_manual(values = c("Acceptance" = "#DDCC77", "Rejection" = "#88CCEE"))  # Brown & Gold

ggsave("interaction_barplot.png", width = 8, height = 6, dpi = 300)


# Create Prediction Dataset (Keep condition_recode Numeric)
data_new <- expand.grid(
  Group = c("Negative", "Positive"),  
  condition_recode = c(-1, 1),  # Keep numeric
  age = mean(data_withbins$age, na.rm = TRUE),  
  sex = mean(data_withbins$sex, na.rm = TRUE),  
  order = mean(data_withbins$order, na.rm = TRUE) 
)

# Compute Group Medians Once and Merge
group_medians <- data_withbins %>%
  group_by(Group) %>%
  summarise(recoded_stress = median(recoded_stress, na.rm = TRUE), .groups = "drop")

data_new <- left_join(data_new, group_medians, by = "Group")

# Predict Values from `lm()` Model
pred <- predict(lm(salience_mean ~ recoded_stress * condition_recode + age + sex + order, data = data), 
                newdata = data_new, se.fit = TRUE)

# Add Predictions and Confidence Intervals
data_new <- data_new %>%
  mutate(
    predicted_salience = pred$fit,
    lower_ci = pred$fit - 1.96 * pred$se.fit,
    upper_ci = pred$fit + 1.96 * pred$se.fit
  )

# Convert condition_recode to Factor AFTER Predictions (For Plotting)
data_new$condition_recode <- factor(data_new$condition_recode, 
                                    levels = c(-1, 1), 
                                    labels = c("Acceptance", "Rejection"))

# Plot
ggplot(data_new, aes(x = Group, y = predicted_salience, fill = condition_recode)) +
  geom_bar(stat = "identity", position = position_dodge(), color = "black") +
  geom_errorbar(aes(ymin = lower_ci, ymax = upper_ci), 
                position = position_dodge(width = 0.9), width = 0.2, color = "black") +
  labs(
    x = "Self-Reported Affect",
    y = "Predicted Salience",
    fill = "Condition"
  ) +
  theme_minimal() +
  theme(panel.grid = element_blank())+
  scale_fill_manual(values = c("Acceptance" = "#DDCC77", "Rejection" = "#88CCEE"))

ggsave("lm_interaction_barplot.png", width = 8, height = 6, dpi = 300)