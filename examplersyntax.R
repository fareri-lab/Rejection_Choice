
library(lme4)
library(lmerTest)
library(dplyr)
library(ggplot2)
library(scales)

library(dplyr)

library(tidyr)  # For drop_na()

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

# Step 1: Compute the overall median of recoded_stress
overall_median_stress <- median(data$recoded_stress, na.rm = TRUE)

# Step 2: Create binary affect group based on median
data_withbins <- data %>%
  mutate(
    Group = case_when(
      recoded_stress > overall_median_stress ~ "Positive",
      recoded_stress <= overall_median_stress ~ "Negative",
      TRUE ~ NA_character_
    )
  ) %>%
  drop_na(Group)

# Step 3: Create prediction dataset with *labeled* condition
data_new <- expand.grid(
  Group = c("Negative", "Positive"),
  condition_recode = c("Rejection", "Acceptance"),
  age = mean(data_withbins$age, na.rm = TRUE),
  sex = mean(data_withbins$sex, na.rm = TRUE),
  timebetween = mean(data_withbins$timebetween, na.rm = TRUE),
  order = mean(data_withbins$order, na.rm = TRUE)
)

# Step 4: Add median stress values for each group
group_medians <- data_withbins %>%
  group_by(Group) %>%
  summarise(recoded_stress = median(recoded_stress, na.rm = TRUE), .groups = "drop")

data_new <- left_join(data_new, group_medians, by = "Group")

# Step 5: Prepare numeric version of condition_recode for model
data_new$condition_numeric <- ifelse(data_new$condition_recode == "Acceptance", -1, 1)

# Step 6: Predict from GLM model
pred <- predict(glm4, newdata = data_new %>%
                  mutate(condition_recode = condition_numeric), 
                type = "link", se.fit = TRUE)

# Step 7: Add predictions and CIs to data_new
data_new$predicted_prob <- plogis(pred$fit)
data_new$lower_ci <- plogis(pred$fit - 1.96 * pred$se.fit)
data_new$upper_ci <- plogis(pred$fit + 1.96 * pred$se.fit)

# Step 8: Ensure correct factor levels for plotting
data_new$condition_recode <- factor(data_new$condition_recode, levels = c("Rejection", "Acceptance"))
data_new$Group <- factor(data_new$Group, levels = c("Negative", "Positive"))

# Step 9: Plot
problottery <- ggplot(data_new, aes(x = Group, y = predicted_prob, fill = condition_recode)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.9), color = "black") +
  geom_errorbar(aes(ymin = lower_ci, ymax = upper_ci),
                position = position_dodge(width = 0.9), width = 0.2, color = "black") +
  scale_y_continuous(labels = scales::percent_format(accuracy = 1)) +
  scale_fill_manual(values = c("Rejection" = "#FF6F61", "Acceptance" = "#88CCEE")) +
  labs(
    x = "Self-Reported Affect",
    y = "Predicted Probability of Self Choice",
    fill = "Condition"
  ) +
  theme_minimal() +
  theme(
    panel.grid = element_blank(),
    axis.title.x = element_text(size = 26, face = "bold", margin = margin(t = 25)),
    axis.title.y = element_text(size = 26, face = "bold", margin = margin(r = 25)),
    axis.text.x = element_text(size = 24, face = "bold"),
    axis.text.y = element_text(size = 24, face = "bold"),
    legend.title = element_text(size = 24, face = "bold"),
    legend.text = element_text(size = 22, face = "bold"),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 30)
  )

# Step 10: Save
ggsave("interaction_barplot.png", plot = problottery, width = 10, height = 8, dpi = 300)



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
# 👇 This is the only change: reversal of level order
data_new$condition_recode <- factor(data_new$condition_recode, 
                                    levels = c(1, -1), 
                                    labels = c("Rejection", "Acceptance"))

# Plot
futureint <- ggplot(data_new, aes(x = Group, y = predicted_salience, fill = condition_recode)) +
  geom_bar(stat = "identity", position = position_dodge(), color = "black") +
  geom_errorbar(aes(ymin = lower_ci, ymax = upper_ci), 
                position = position_dodge(width = 0.9), width = 0.2, color = "black") +
  labs(
    x = "Self-Reported Affect",
    y = "Likelihood of Future Interaction",
    fill = "Condition"
  ) +
  theme_minimal() +
  theme(
    panel.grid = element_blank(),
    axis.title.x = element_text(size = 26, face = "bold", margin = margin(t = 25)),
    axis.title.y = element_text(size = 26, face = "bold", margin = margin(r = 25)),
    axis.text.x = element_text(size = 24, face = "bold"),
    axis.text.y = element_text(size = 24, face = "bold"),
    legend.title = element_text(size = 24, face = "bold"),
    legend.text = element_text(size = 22, face = "bold"),
    plot.margin = margin(t = 20, r = 20, b = 20, l = 30)
  ) +
  scale_fill_manual(values = c("Acceptance" = "#88CCEE", "Rejection" = "#FF6F61"))

# Save with matching dimensions
ggsave("lm_interaction_barplot.png", plot = futureint, width = 10, height = 8, dpi = 300)

#old code ##################

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
