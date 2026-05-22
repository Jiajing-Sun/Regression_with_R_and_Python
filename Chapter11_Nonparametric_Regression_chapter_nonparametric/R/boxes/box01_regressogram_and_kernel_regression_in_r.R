# Chapter 11, R box 01: Regressogram and kernel regression in R
# Source label: box:r_np_housing
# Full runnable chapter script: ../chapter11.R

df <- read.csv(file.path("data", "apartment_price_data.csv"))
df <- df[complete.cases(df[, c("living_area", "price")]), ]

ols <- lm(price ~ living_area, data = df)
x_grid <- seq(20, 140, length.out = 250)

gaussian_nw <- function(x0, h = 10) {
  w <- exp(-0.5 * ((df$living_area - x0) / h)^2)
  sum(w * df$price) / sum(w)
}

kernel_fit <- vapply(x_grid, gaussian_nw, numeric(1), h = 10)

bin_breaks <- seq(15, 175, by = 10)
df$bin <- cut(df$living_area, breaks = bin_breaks, include.lowest = TRUE)
regressogram <- aggregate(
  cbind(price, living_area) ~ bin,
  data = df,
  FUN = mean
)
bin_counts <- aggregate(price ~ bin, data = df, FUN = length)
names(bin_counts)[2] <- "n"
regressogram$n <- bin_counts$n
regressogram_plot <- regressogram[regressogram$n >= 10, ]

selected_output <- data.frame(
  estimator = c("Linear regression at 50 sqm",
                "Regressogram, 45-55 sqm",
                "Gaussian kernel, h = 10"),
  estimate = round(c(
    predict(ols, newdata = data.frame(living_area = 50)),
    mean(df$price[df$living_area >= 45 & df$living_area <= 55]),
    gaussian_nw(50, h = 10)
  ), 3)
)
print(selected_output)

dir.create("pdf", showWarnings = FALSE)
pdf(file.path("pdf", "apartment_price_nonparametric.pdf"),
    width = 5.69, height = 4.35, family = "serif")
par(mar = c(4.1, 4.2, 0.7, 0.8), mgp = c(2.4, 0.7, 0), las = 1)
plot(df$living_area, df$price,
     pch = 16, cex = 0.34, col = adjustcolor("#F26B2A", alpha.f = 0.75),
     xlab = "Apartment size (sqm)", ylab = "Price (M. SEK)",
     xlim = c(15, 150), ylim = c(0, 10), bty = "l",
     cex.lab = 0.95, cex.axis = 0.9)
linear_fit <- predict(ols, newdata = data.frame(living_area = x_grid))
lines(x_grid, linear_fit, col = "gray15", lwd = 1.45, lty = 1)
lines(x_grid, kernel_fit, col = "#005DAA", lwd = 1.75, lty = 4)
lines(regressogram_plot$living_area, regressogram_plot$price,
      type = "s", col = "#009E73", lwd = 1.45, lty = 2)
legend("topleft", bty = "n", cex = 0.82,
       legend = c("Linear regression", "Gaussian kernel", "Regressogram"),
       col = c("gray15", "#005DAA", "#009E73"),
       lty = c(1, 4, 2), lwd = c(1.45, 1.75, 1.45),
       seg.len = 2.0)
dev.off()
