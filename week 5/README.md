#In README.md, answer: 1. What is the “size” (i.e., slope) of this relationship? Interpret the slope in plain language. Does it match your plot? 2. Is the relationship significant? How do you know? Explain the p-value in plain but precise language.

#Ans (2.2): the slope is 0.3776, which is the degree to which the number of maternal inherited de novo mutations that can be explained by the maternal age, or the strength of the correlation between maternal age and maternal inherited dnms. The points on the graph are more randomly distributed. The p-value is less than 2.2x10-16, which makes this relationship significant. There is a 2.2x10-16 probability that the null hypothesis is true, which is that there is no chnage in the number of maternally inherited dnms as a function of maternal age.


#Ans (2.3): the slope here is 1.35384, which means there is a stronger correlation between father's age and the number of paternally-inherited dnms. This makes sense because the line seems more fitted. There is a 2.2x10-16 probability that the spread of the number of maternally-inherited dnms is due to random chance (p-value). 


#Step 2.4 — Predict for a 50.5-year-old father
#Use the paternal regression model to predict the expected number of paternal DNMs for a father of age 50.5. You are welcome to do this manually or using a built-in function, but show your work in README.md.
y = mx + b
num_paternal_inherited_dnms = father_age_slope * paternal_age + y-intercept
print((1.35384*50.2)+10.32632)

#Ans (2.4): expected number of paternal DNMs is 78.289 ~ 78.


#Ans (2.6): the mean difference in counts of maternal and paternal dnms is -39.23. On average, an individual will have about 39 more paternally-inherited de novo mutations compared to those that are maternally inherited. It seems to match the plot, because the maternal mean is around 10 and the paternal mean is around 50, so the difference is about 40, which is close to -39.23.The relationship is significant because the p-value is less than 2.2x10^-16.  The is less than a 2.2x10^-16 probability that the difference in means between maternally and paternally inherited dnms = -39.23 if the null hypothesis is true. The null hypothesis is that there is no mean difference between counts of maternal and paternal dnms. 

#QUESTION 3

#Step 3.1 — Pick a TidyTuesday dataset
#Choose a dataset from the bottom of the TidyTuesday README. Record which one you chose in README.md.
#(Ans 3.1) I chose spotify_songs.csv

#Step 3.2 — Explore and visualize
#Generate figures and note any interesting patterns in README.md; save figures as ex4_<something>.png.
spotifysongs_df <- read_csv("~/qb25-answers/week5/spotify_songs.csv")

#total number of rows = 32833
#total number of unique artists represented = 10693
print(length(unique(spotifysongs_df$track_artist)))

#length of songs in general 
overall_track_lengths <- ggplot(spotifysongs_df, aes(x = duration_ms)) +
  geom_histogram()
  ggsave("ex4_overall_track_lengths.png", plot = overall_track_lengths, path = "~/qb25-answers/week5")

#comparing the length of songs in by genre
tracklength_genre <- ggplot(spotifysongs_df, aes(x = duration_ms)) +
  geom_histogram() +
  facet_wrap((. ~ playlist_genre))
  ggsave("ex4_tracklength_genre.png", plot = tracklength_genre, path = "~/qb25-answers/week5")
#all genres' track lengths have a peak of around 2e05ms. 

#comparing the tempo of songs by genre
tempo_genre <- ggplot(spotifysongs_df, aes(x = tempo)) +
  geom_histogram() +
  facet_wrap((. ~ playlist_genre))
  ggsave("ex4_tempo_genre.png", plot = tempo_genre, path = "~/qb25-answers/week5")
#edm songs are mostly within a very narrow range of tempo, compared to the other genres 

#how much does track length correlate with popularity?
lm(data = spotifysongs_df, formula = track_popularity ~ 1 + duration_ms) %>%
  summary()
#the estimate for track duration(ms) is -5.999e-5, which means track length was negatively correlated with popularity. As track length increases, popularity decreases. 

#how much does tempo correlate with popularity?
lm(data = spotifysongs_df, formula = track_popularity ~ 1 + tempo) %>%
  summary()
#the slope estimate is -.004994, which is a slight negative correlation between track tempo and popularity, but very miniscule. 

#danceability vs. popularity
lm(data = spotifysongs_df, formula = track_popularity ~ 1 + danceability) %>%
+   summary()
  

#Step 3.3 — Pose and test a linear-model hypothesis
#State a hypothesis, fit a linear model, evaluate fit, and report results in README.md.

#Hypothesis: tracks with shorter track lengths will be more popular. Track length are inversely correlated with popularity. 

lm(data = spotifysongs_df, formula = track_popularity ~ 1 + duration_ms) %>%
  summary()

#the estimate for track duration(ms) is -5.999e-5, which means track length was negatively correlated with popularity. As track length increases, popularity decreases. 
