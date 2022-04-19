# Exploratory Data Analysis - Github programming languages


library(dplyr)


setwd("D:/Meus documentos/dev/personal-projects/github-languages_EDA")
getwd()
dir()

repos <- read.csv("repos.csv")
View(repos)
issues <- read.csv("issues.csv")
View(issues)

issues$name = as.character(issues$name)
issues$year = as.factor(issues$year)
issues$quarter = as.factor(issues$quarter)

summary(repos)
str(repos)
summary(issues)
str(issues)


repos_summary <- repos %>% group_by(language) %>% 
  arrange(desc(num_repos)) %>% head(15)
View(repos_summary)

issues_summary <- issues %>% group_by(name) %>% 
  summarise(sum_issues = sum(count)) %>%
  arrange(desc(sum_issues)) %>% head(15)
View(issues_summary)


