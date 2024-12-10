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
# 循环计算 ICC
for (i in 1:y) {
    tryCatch({
        # 检查特征是否全为0
        if (all(T12[, i] == 0) && all(T12[, i + y] == 0)) {
            icc[i] <- NA  # 如果特征值全为0，设置 ICC 为 NA
        } else if (all(T12[, i] == T12[, i + y])) {
            icc[i] <- 1  # 如果人工和自动分割特征完全一致，设置 ICC 为 1或者0.9999（最高）
        } else {
            icc[i] <- ICC(T12[, c(i, i + y)])$results$ICC[2]  # 正常计算 ICC
        }
    }, error = function(e) {
        icc[i] <- NA  # 如果计算失败，将 ICC 设置为 NA
    })
}
mean(icc)
median(icc)
m <- length(which(icc >= 0.80))
m

summary(icc)
dt <- as.data.frame(icc)
dt$FeatureName <- names(T1)
write.csv(dt, file = "D:/Apple-paper/Radiomics/survival analysis/survival analysis/APPLE/965/2_1_calculate icc/Total_GBM+LGG_t2_s+s1_ICC_965.csv")
