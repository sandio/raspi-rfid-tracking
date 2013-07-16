d1 = read.table("rssi.distance.grid.r1", col.names=c("d0","d90","d180","d270"))
attach(d1)

pdf("rssi_distance_grid_r1.pdf", width=10, height=10)

par(mfrow=c(4,4))

s = c("(0,0)","(1,0)","(2,0)","(3,0)","(0,1)","(1,1)","(2,1)","(3,1)",
	"(0,2)","(1,2)","(2,2)","(3,2)","(0,3)","(1,3)","(2,3)","(3,3)")

for(i in 1:16) {
	barplot(as.matrix(d1[i,]), ylim=c(30,80), xpd=F, beside=T, col=gray.colors(2), density=20,
		xlab="Orientation of tag (degrees)", ylab="RSSI (unitless)")
	title(paste("Position", s[i]))
}

dev.off()
