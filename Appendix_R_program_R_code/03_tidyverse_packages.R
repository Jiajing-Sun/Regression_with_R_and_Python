# Appendix R section: Tidyverse packages
# Source: Appendix R program.tex
# Extracted from the current textbook LaTeX source in original order.

# ------------------------------------------------------------------------------
# Chunk 001
# Chapter: The R Programming Language
# Section: Tidyverse packages
# Subsection: Data Manipulation with dplyr
# ------------------------------------------------------------------------------

# If needed:
# install.packages(c("dplyr", "tibble"))
library(dplyr)

# Inspect the data
starwars %>% 
  select(name, species, homeworld, height, mass) %>%
  head()

# ------------------------------------------------------------------------------
# Chunk 002
# Chapter: The R Programming Language
# Section: Tidyverse packages
# Subsection: Data Manipulation with dplyr
# Paragraph: Filtering and selecting.
# ------------------------------------------------------------------------------

starwars %>%
  filter(species == "Human", !is.na(height)) %>%
  select(name, sex, homeworld, height, mass) %>%
  arrange(desc(height)) %>%
  head(10)

# ------------------------------------------------------------------------------
# Chunk 003
# Chapter: The R Programming Language
# Section: Tidyverse packages
# Subsection: Data Manipulation with dplyr
# Paragraph: Creating new variables with mutate().
# ------------------------------------------------------------------------------

starwars %>%
  filter(!is.na(height), !is.na(mass)) %>%
  mutate(height_m = height / 100,
         bmi      = mass / (height_m^2)) %>%
  select(name, species, height, mass, bmi) %>%
  arrange(desc(bmi)) %>%
  head(10)

# ------------------------------------------------------------------------------
# Chunk 004
# Chapter: The R Programming Language
# Section: Tidyverse packages
# Subsection: Data Manipulation with dplyr
# Paragraph: Grouped summaries.
# ------------------------------------------------------------------------------

starwars %>%
  filter(!is.na(height), !is.na(mass), !is.na(species)) %>%
  group_by(species) %>%
  summarise(
    avg_height = mean(height),
    avg_mass   = mean(mass),
    n          = n(),
    .groups    = "drop"
  ) %>%
  filter(n >= 5) %>%
  arrange(desc(avg_height))

# ------------------------------------------------------------------------------
# Chunk 005
# Chapter: The R Programming Language
# Section: Tidyverse packages
# Subsection: Data Visualization with ggplot2
# ------------------------------------------------------------------------------

# If needed:
# install.packages("ggplot2")
library(ggplot2)

# ------------------------------------------------------------------------------
# Chunk 006
# Chapter: The R Programming Language
# Section: Tidyverse packages
# Subsection: Data Visualization with ggplot2
# Subsubsection: Starting with the data
# ------------------------------------------------------------------------------

ggplot(data = diamonds) +
  labs(title = "The diamonds dataset (ggplot2)")

# ------------------------------------------------------------------------------
# Chunk 007
# Chapter: The R Programming Language
# Section: Tidyverse packages
# Subsection: Data Visualization with ggplot2
# Subsubsection: Adding aesthetics and a geometric layer
# ------------------------------------------------------------------------------

ggplot(diamonds, aes(x = carat, y = price, colour = cut)) +
  geom_point(alpha = 0.4) +
  labs(title = "Diamond Price and Carat (coloured by cut)",
       x = "Carat", y = "Price (USD)")

# ------------------------------------------------------------------------------
# Chunk 008
# Chapter: The R Programming Language
# Section: Tidyverse packages
# Subsection: Data Visualization with ggplot2
# Subsubsection: Histograms and density
# ------------------------------------------------------------------------------

ggplot(diamonds, aes(x = price)) +
  geom_histogram(binwidth = 500, fill = "skyblue", color = "black") +
  labs(title = "Distribution of Diamond Prices",
       x = "Price (USD)", y = "Count")

# ------------------------------------------------------------------------------
# Chunk 009
# Chapter: The R Programming Language
# Section: Tidyverse packages
# Subsection: Data Visualization with ggplot2
# Subsubsection: Facets (small multiples)
# ------------------------------------------------------------------------------

ggplot(diamonds, aes(x = carat, y = price)) +
  geom_point(alpha = 0.3) +
  facet_wrap(~ cut) +
  labs(title = "Price vs Carat by Cut",
       x = "Carat", y = "Price (USD)")

# ------------------------------------------------------------------------------
# Chunk 010
# Chapter: The R Programming Language
# Section: Tidyverse packages
# Subsection: Data Visualization with ggplot2
# Subsubsection: Statistical transformations (smoothing)
# ------------------------------------------------------------------------------

ggplot(diamonds, aes(x = carat, y = price)) +
  geom_point(alpha = 0.15) +
  geom_smooth(method = "lm", se = FALSE, color = "firebrick") +
  labs(title = "Linear Trend: Price vs Carat",
       x = "Carat", y = "Price (USD)")

# ------------------------------------------------------------------------------
# Chunk 011
# Chapter: The R Programming Language
# Section: Tidyverse packages
# Subsection: Data Visualization with ggplot2
# Subsubsection: Coordinates and zooming
# ------------------------------------------------------------------------------

ggplot(diamonds, aes(x = carat, y = price, colour = cut)) +
  geom_point(alpha = 0.3) +
  coord_cartesian(xlim = c(0, 2), ylim = c(0, 15000)) +
  labs(title = "Zoomed View: Price vs Carat",
       x = "Carat", y = "Price (USD)")

# ------------------------------------------------------------------------------
# Chunk 012
# Chapter: The R Programming Language
# Section: Tidyverse packages
# Subsection: Data Visualization with ggplot2
# Subsubsection: Themes
# ------------------------------------------------------------------------------

ggplot(diamonds, aes(x = carat, y = price)) +
  geom_point(alpha = 0.25) +
  facet_wrap(~ cut) +
  theme_minimal() +
  labs(title = "Price vs Carat by Cut (minimal theme)",
       x = "Carat", y = "Price (USD)")

# ------------------------------------------------------------------------------
# Chunk 013
# Chapter: The R Programming Language
# Section: Tidyverse packages
# Subsection: Data Visualization with ggplot2
# Subsubsection: Saving and reusing plots
# ------------------------------------------------------------------------------

p <- ggplot(diamonds, aes(x = carat, y = price, colour = cut)) +
  geom_point(alpha = 0.3) +
  labs(title = "Diamond Price vs Carat",
       x = "Carat", y = "Price (USD)")

# Save as a PNG file in the working directory
ggsave("diamond_price_vs_carat.png", p, width = 7, height = 5, dpi = 300)

# Keep the plot object for later modification
p
