# Extracted R code for Chapter 13: Nonparametric Regression
# Source: nonparametric-chapter.tex
# Generated from the current textbook LaTeX source.
# Code blocks are kept in textbook order; relative paths follow the book examples.

# ------------------------------------------------------------------------------
# Box 01: Nonparametric RD in R (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:619-619
# ------------------------------------------------------------------------------

install.packages(c("sandwich", "lmtest", "ivreg", "rdrobust"))

# ------------------------------------------------------------------------------
# Box 02: Nonparametric RD in R (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:630-639
# ------------------------------------------------------------------------------

df <- read.csv("municip_data.csv")
df <- df[df$municip_name != "Gotland", ]

c0 <- .5
df$rv <- df$share_seats_left_last_election - c0
df$change_tax_rate <- df$tax_rate - df$tax_rate_4_years_back
df <- df[!is.na(df$change_tax_rate), ]

df$Z   <- ifelse(df$rv >= 0, 1, 0)   # cutoff indicator
df$Zrv <- df$Z * df$rv              # slope interaction

# ------------------------------------------------------------------------------
# Box 03: Nonparametric RD in R (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:644-648
# ------------------------------------------------------------------------------

tri <- function(u) pmax(0, 1 - abs(u))

h <- .10
df_h <- df[abs(df$rv) <= h, ]
df_h$w <- tri(df_h$rv / h)

# ------------------------------------------------------------------------------
# Box 04: Nonparametric RD in R (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:653-663
# ------------------------------------------------------------------------------

rd_fs_np <- lm(left_coalition_last_term ~ Z + rv + Zrv,
               data = df_h, weights = w)

rd_rf_np <- lm(change_tax_rate ~ Z + rv + Zrv,
               data = df_h, weights = w)

library(sandwich)
library(lmtest)

coeftest(rd_fs_np, vcov = vcovHC(rd_fs_np, type = "HC0"))
coeftest(rd_rf_np, vcov = vcovHC(rd_rf_np, type = "HC0"))

# ------------------------------------------------------------------------------
# Box 05: Nonparametric RD in R (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:672-685
# ------------------------------------------------------------------------------

delta_hat <- coef(rd_fs_np)["Z"]
alpha_hat <- coef(rd_rf_np)["Z"]
wald_hat  <- alpha_hat / delta_hat

library(ivreg)

rd_fuzzy_np <- ivreg(change_tax_rate ~ left_coalition_last_term + rv + Zrv |
                       Z + rv + Zrv,
                     data = df_h, weights = w)

coeftest(rd_fuzzy_np, vcov = vcovHC(rd_fuzzy_np, type = "HC0"))

c(wald_hat = wald_hat,
  iv_hat   = coef(rd_fuzzy_np)["left_coalition_last_term"])

# ------------------------------------------------------------------------------
# Box 06: Nonparametric RD in R (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:690-747
# ------------------------------------------------------------------------------

fig_dir <- "pdf"
dir.create(fig_dir, showWarnings = FALSE, recursive = TRUE)

binwidth <- .01
df$bin <- pmin(floor(df$share_seats_left_last_election / binwidth) * binwidth,
               1 - binwidth) + binwidth/2

agg_fs <- aggregate(left_coalition_last_term ~ bin, data = df, mean)
agg_rf <- aggregate(change_tax_rate ~ bin, data = df, mean)

xlim <- c(c0 - h, c0 + h)

## helper: fitted values on each side from the interacted local-linear model
fitted_side <- function(b, x, side = c("left","right")) {
  side <- match.arg(side)
  rv <- x - c0
  b0 <- b["(Intercept)"]; b1 <- b["Z"]; b2 <- b["rv"]; b3 <- b["Zrv"]
  if (side == "left")  return(b0 + b2 * rv)
  return((b0 + b1) + (b2 + b3) * rv)
}

## --- First stage plot ---
b_fs <- coef(rd_fs_np)
xL <- seq(xlim[1], c0, length.out = 200)
xR <- seq(c0, xlim[2], length.out = 200)

pdf(file.path(fig_dir, "rd_municip_fs_agg_np.pdf"),
    width = 4.2, height = 3.4, family = "serif")
par(mar = c(4.6, 4.8, 0.6, 0.6))

agg_fs2 <- agg_fs[agg_fs$bin >= xlim[1] & agg_fs$bin <= xlim[2], ]
plot(agg_fs2$bin, agg_fs2$left_coalition_last_term,
     pch = 16, cex = .85, col = "#F47939",
     xlab = "# seats left-wing parties",
     ylab = "Left-wing ruling coalition",
     xlim = xlim, ylim = c(0, 1), bty = "l")
abline(v = c0, lty = 2, lwd = 1.2)
lines(xL, fitted_side(b_fs, xL, "left"),  lwd = 2.2)
lines(xR, fitted_side(b_fs, xR, "right"), lwd = 2.2)
dev.off()

## --- Reduced form plot ---
b_rf <- coef(rd_rf_np)

pdf(file.path(fig_dir, "rd_municip_rf_agg_d_np.pdf"),
    width = 4.2, height = 3.4, family = "serif")
par(mar = c(4.6, 4.8, 0.6, 0.6))

agg_rf2 <- agg_rf[agg_rf$bin >= xlim[1] & agg_rf$bin <= xlim[2], ]
plot(agg_rf2$bin, agg_rf2$change_tax_rate,
     pch = 16, cex = .85, col = "#F47939",
     xlab = "# seats left-wing parties",
     ylab = "Change in tax rate",
     xlim = xlim, bty = "l")
abline(v = c0, lty = 2, lwd = 1.2)
lines(xL, fitted_side(b_rf, xL, "left"),  lwd = 2.2)
lines(xR, fitted_side(b_rf, xR, "right"), lwd = 2.2)
dev.off()

# ------------------------------------------------------------------------------
# Box 07: Nonparametric RD in R (local linear + triangular kernel)
# Source lines: nonparametric-chapter.tex:752-758
# ------------------------------------------------------------------------------

library(rdrobust)

out_np <- rdrobust(y = df$change_tax_rate,
                   x = df$share_seats_left_last_election,
                   c = .5, kernel = "triangular",
                   fuzzy = df$left_coalition_last_term)
summary(out_np)
