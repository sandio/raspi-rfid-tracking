d1 = read.table("error.boxplot")

pdf("error_boxplot.pdf", width=10, height=7)

names = c(expression(paste("0",degree)), expression(paste("90",degree)), expression(paste("180",degree)), expression(paste("270",degree)))
#reps = c(rep("#4D4D4D", 2), rep("#969696", 2), rep("#C3C3C3", 2), rep("#E6E6E6", 2))
reps = c(rep("red", 2), rep("green", 2), rep("blue", 2), rep("darkorange", 2))
boxplot(d1, col=reps, names=c("x","y","x","y","x","y","x","y"), 
	main="Accumulated errors for different tag orientations for all grid positions", xlab="X and Y accumulated errors", ylab="Error (meters)")
abline(h=mean(as.matrix(d1)))
legend("topleft", names, fill=c(reps[1],reps[3],reps[5],reps[7]), title="Orientation of tag")

dev.off()
