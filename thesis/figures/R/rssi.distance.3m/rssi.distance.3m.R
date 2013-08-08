deg = "315"
d1 = read.table(paste("rssi.distance.3m.los.", deg, "deg", sep=""), col.names=c("r01","r02","r03"))
d2 = read.table(paste("rssi.distance.3m.nlos.", deg,"deg", sep=""), col.names=c("r11","r12","r13"))

x1 = seq(0, 3, by=.5)
x2 = seq(.5, 3, by=.5)

x1range = range(x1)
x2range = range(x2)
y1range = range(d1[1], d1[2], d1[3])
y2range = range(d2[1], d2[2], d2[3])

cols = c("red", "green", "blue")

pdf(paste("rssi_distance_3m_", deg, "deg.pdf", sep=""), width=10, height=5)

par(mfrow=c(1,2))

plot(x1range, y1range, type="n", xlab="Distance (m)", ylab="RSSI (unitless)")
attach(d1)
lines(x1, r01, type="b", pch=1, col=cols[1])
lines(x1, r02, type="b", pch=2, col=cols[2])
lines(x1, r03, type="b", pch=3, col=cols[3])
title(paste("Line-of-sight at", deg, "degrees"))
legend("topright", c("1","2","3"), pch=1:3, title="Readers", col=cols)

plot(x2range, y2range, type="n", xlab="Distance (m)", ylab="RSSI (unitless)")
attach(d2)
lines(x2, r11, type="b", pch=1, col=cols[1])
lines(x2, r12, type="b", pch=2, col=cols[2])
lines(x2, r13, type="b", pch=3, col=cols[3])
title(paste("Non-line-of-sight at", deg, "degrees"))
legend("topright", c("1","2","3"), pch=1:3, title="Readers", col=cols)

dev.off()
