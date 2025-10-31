#In README.md, answer: 1. What is the “size” (i.e., slope) of this relationship? Interpret the slope in plain language. Does it match your plot? 2. Is the relationship significant? How do you know? Explain the p-value in plain but precise language.

#Ans (2.2): the slope is 0.3776, which is the degree to which the number of maternal inherited de novo mutations that can be explained by the moternal age. The points on the graph are more randomly distributed. The p-value is less than 2.2x10-16, which makes this relationship significant. There is a 2.2x10-16 probability that the spread of the number of maternally-inherited dnms is due to random chance.



#Ans (2.3): the slope here is 1.35384, which means there is a stronger correlation between father's age and the number of paternally-inherited dnms. This makes sense because the line seems more fitted. There is a 2.2x10-16 probability that the spread of the number of maternally-inherited dnms is due to random chance (p-value). 



#Step 2.4 — Predict for a 50.5-year-old father
#Use the paternal regression model to predict the expected number of paternal DNMs for a father of age 50.5. You are welcome to do this manually or using a built-in function, but show your work in README.md.
y = mx + b
num_paternal_inherited_dnms = father_age_slope * paternal_age + y-intercept
print((1.35384*50.2)+10.32632)

#Ans (2.4): expected number of paternal DNMs is 78.289 ~ 78.
