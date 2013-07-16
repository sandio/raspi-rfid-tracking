d1 = read.table("error.distance.grid")

pdf("error_distance_grid.pdf", width=10, height=10)

par(mfrow=c(4,4))

s = c("(0,0)","(1,0)","(2,0)","(3,0)","(0,1)","(1,1)","(2,1)","(3,1)",
	"(0,2)","(1,2)","(2,2)","(3,2)","(0,3)","(1,3)","(2,3)","(3,3)")
cols = c("red", "green", "blue", "black")

theta = seq(0, 2 * pi, length=100)
r = range(d1)
for(i in 1:16) {
	plot(r, r, xlim=c(-r[2],r[2]), ylim=c(-r[2],r[2]), type="n",
		xlab="x error (m)", ylab="y error (m)")
	title(paste("Position", s[i]))
	t = 1
	for(j in seq(1, 8, by = 2)) {
		x = d1[i,j] * cos(theta)
		y = d1[i, j+1] * sin(theta)
		lines(x, y, type="l", col=cols[t])
		t = t + 1
	}
}
dev.off()
