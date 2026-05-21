# Chapter 10, R box 04: Regression tree in R
# Source label: box:regression_tree
# Full runnable chapter script: ../chapter10.R
# This file mirrors the printed code box; use the full chapter script for end-to-end execution.
# --- Code block 1 ---
# install.packages(c("rpart", "rpart.plot"))  # run once if needed
# --- Code block 2 ---
library(rpart)
library(rpart.plot)

df <- read.csv(file.path("data", "apartment_price_data.csv"))
tree_model <- rpart(price ~ living_area + monthly_fee,
                    data = df,
                    control = rpart.control(minsplit = 20,
                                            minbucket = 5,
                                            cp = 0))
rpart.plot(tree_model)
printcp(tree_model)
pruned_tree <- prune(tree_model, cp = .03)
rpart.plot(pruned_tree)
