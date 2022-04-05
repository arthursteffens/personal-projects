# Exploratory Data Analysis - Github programming languages


library(dplyr)


setwd("D:/Meus documentos/dev/personal-projects/github-languages_EDA")
getwd()
dir()

repos <- read.csv("repos.csv")
View(repos)
issues <- read.csv("issues.csv")
View(issues)

summary(repos)
str(repos)
summary(issues)
str(issues)

issues$name = as.character(issues$name)
issues$year = as.factor(issues$year)
issues$quarter = as.factor(issues$quarter)

issues_summary <- issues %>% group_by(name, year) %>% 
  summarise(max_issues = max(count)) %>% 
  arrange(desc(maxim))
View(issues_summary)


