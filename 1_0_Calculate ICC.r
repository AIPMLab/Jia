library(psych)

setwd("D:/Apple-paper/Radiomics/survival analysis/survival analysis/APPLE/965/1_files") # nolint

T1 <- read.csv("Total_GBM+LGG_t2_s_add_os_age_gender_label.csv", header = TRUE)
T2 <- read.csv("Total_GBM+LGG_t2_s1_add_os_age_gender_label.csv", header = TRUE)
T1 <- T1[, 2:(dim(T1)[2]-5)]
T2 <- T2[, 2:(dim(T2)[2]-5)]
dim(T1)
dim(T2)
View(T1)
View(T2)
x <- dim(T1)[1]
y <- dim(T1)[2]
T12 <- cbind(T1, T2)
dim(T12)

icc <- c(1:y)
# Loop calculation ICC
for (i in 1:y) {
    tryCatch({
        # Check if all features are 0
        if (all(T12[, i] == 0) && all(T12[, i + y] == 0)) {
            icc[i] <- NA  # If all eigenvalues ​​are 0, set ICC to NA
        } else if (all(T12[, i] == T12[, i + y])) {
            icc[i] <- 1  # If the manual and automatic segmentation features are exactly the same, set ICC to 1 or 0.9999 (highest)
        } else {
            icc[i] <- ICC(T12[, c(i, i + y)])$results$ICC[2]  # Normal calculation ICC
        }
    }, error = function(e) {
        icc[i] <- NA  # If the calculation fails, set ICC to NA
    })
}
mean(icc) # Calculate and output the mean ICC.
median(icc) # Calculate and output the median ICC.
m <- length(which(icc >= 0.80)) # Calculate the number of features with ICC values ​​greater than or equal to 0.80 and store it in the variable m
m

summary(icc)
dt <- as.data.frame(icc)
dt$FeatureName <- names(T1)
write.csv(dt, file = "D:/Apple-paper/Radiomics/survival analysis/survival analysis/APPLE/965/2_1_calculate icc/Total_GBM+LGG_t2_s+s1_ICC_965.csv")
