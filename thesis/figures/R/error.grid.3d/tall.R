tall = read.table("tall", header=TRUE)

pdf("tall.pdf", width=10, height=7)

names = c("8cm","75cm", "170cm")

s3d <- scatterplot3d(tall, xlim=c(0,4), ylim=c(0,6), zlim=c(0,2), lab=c(8, 6, 1), 
	type="h", highlight.3d=T, angle=57, grid=TRUE, pch=15, 
	xlab="X (m)", ylab="Y (m)", zlab = "Average error (m)",
	main="Accumulated errors for each position of the grid")

s3d.coords <- s3d$xyz.convert(tall$X,tall$Y,tall$Z)

text(s3d.coords$x, s3d.coords$y, labels=tall$Z, cex=.85, pos=4)

#legend("topleft", names, fill=c("red","green","blue"), title="Elevation of tag")

dev.off()
