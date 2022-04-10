library(ggplot2)
library(ggpmisc)
library(ggpubr)
setwd("C:/Users/lr201/code/gene_prediction_pipeline")
# using pred_stat inquire ass_stat

# gen
data = read.csv("stat_data_Ha_6700.txt", sep = " ")
gs_gn = ggplot(data = data, aes(x = genome_size, y = gene_num)) +
  geom_point() + 
  geom_smooth(method = lm, level = 0.95, colour = "#009900") + 
  stat_poly_eq(formula = y ~ x, 
             aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")), 
             parse = TRUE)

my.formula <- y ~ x
ggplot(data = data, aes(x = gene_num, y = ips_item_num)) +
  geom_point() + 
  geom_smooth(method = lm, level = 0.95, colour = "#009900") + 
  stat_poly_eq(formula = my.formula, 
               aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")), 
               parse = TRUE)

ggplot(data = data, aes(x = genome_size, y = ips_item_num)) +
  geom_point() + 
  geom_smooth(method = lm, level = 0.95, colour = "#009900") + 
  stat_poly_eq(formula = my.formula, 
               aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")), 
               parse = TRUE)

ggplot(data = data, aes(x = gene_num, y = running_time)) +
  geom_point() + 
  geom_smooth(method = lm, level = 0.95, colour = "#009900") + 
  stat_poly_eq(formula = my.formula, 
               aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")), 
               parse = TRUE)


ggplot(data = data, aes(x = contig_num, y = running_time)) +
  geom_point() + 
  geom_smooth(method = lm, level = 0.95, colour = "#009900") + 
  stat_poly_eq(formula = y ~ x, 
               aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")), 
               parse = TRUE)

ggplot(data = data, aes(x = genome_size, y = running_time)) +
  geom_point() + 
  geom_smooth(method = lm, level = 0.95, colour = "#009900") + 
  stat_poly_eq(formula = my.formula, 
               aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")), 
               parse = TRUE)


ggplot(data = data, aes(x = contig_N50, y = running_time)) +
  geom_point() + 
  geom_smooth(method = lm, level = 0.95, colour = "#009900") + 
  stat_poly_eq(formula = my.formula, 
               aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")), 
               parse = TRUE)


ggplot(data = data, aes(x = contig_N50, y = gene_num)) +
  geom_point() + 
  geom_smooth(method = lm, level = 0.95, colour = "#009900") + 
  stat_poly_eq(formula = my.formula, 
               aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")), 
               parse = TRUE)

ggplot(data = data, aes(x = contig_num, y = gene_num)) +
  geom_point() + 
  geom_smooth(method = lm, level = 0.95, colour = "#009900") + 
  stat_poly_eq(formula = my.formula, 
               aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")), 
               parse = TRUE)

ggplot(data = data, aes(x = contig_num, y = genome_size)) +
  geom_point() + 
  geom_smooth(method = lm, level = 0.95, colour = "#009900") + 
  stat_poly_eq(formula = my.formula, 
               aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")),
               parse = TRUE)

ggplot(data = data, aes(x = contig_num, y = contig_N50)) +
  geom_point() + 
  geom_smooth(method = lm, level = 0.95, colour = "#009900") + 
  stat_poly_eq(formula = my.formula, 
               aes(label = paste(..eq.label.., ..rr.label.., sep = "~~~")), 
               parse = TRUE)
ggarrange(bxp, dp, bp, sp + rremove("x.text"), 
          labels = c("A", "B", "C","D"),
          ncol = 2, nrow = 2)



# -------------------------------------------------------------------------
lab = c(0:25)
sha = c(1:26)
shap = data.frame(lab = lab,sha = sha)
ggplot(data = shap, aes(x = 1:26,y = sha)) +
  geom_point(shape = lab, size = 3) +
  geom_text(aes(label = lab,vjust = -1.5)) +
  ylim(0,28) +
  ggtitle("数字代表的点型")

ggplot(data = data, aes(x = genome_size, y = gene_num)) +
  geom_point(colour="#339911", shape = 19,size = 1.5)

library(scales)
ggplot(data = data,aes(x=Petal.Length,y=Sepal.Length,colour=Species))+
  geom_point()
