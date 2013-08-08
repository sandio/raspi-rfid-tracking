d1 = read.table("rssi.distance.13m.los", col.names=c("r01","r02","r03"))
d2 = read.table("rssi.distance.13m.nlos", col.names=c("r11","r12","r13"))

x1 = seq(1, 13, by=1)
x2 = seq(2, 13, by=1)

x1range = range(x1)
x2range = range(x2)
y1range = range(d1[1], d1[2], d1[3])
y2range = range(d2[1], d2[2], d2[3])

cols = c("red","green","blue")

pdf("rssi_distance_13m.pdf", width=12, height=5)

par(mfrow=c(1,2))

plot(x1range, y1range, type="n", xlab="Distance (m)", ylab="RSSI (unitless)")
attach(d1)
lines(x1, r01, type="b", pch=1, col=cols[1])
lines(x1, r02, type="b", pch=2, col=cols[2])
lines(x1, r03, type="b", pch=3, col=cols[3])
title("Line-of-sight")
legend("topright", c("1","2","3"), pch=1:3, title="Readers", col=cols)

plot(x2range, y2range, type="n", xlab="Distance (m)", ylab="RSSI (unitless)")
attach(d2)
lines(x2, r11, type="b", pch=1, col=cols[1])
lines(x2, r12, type="b", pch=2, col=cols[2])
lines(x2, r13, type="b", pch=3, col=cols[3])
title("Non-line-of-sight")
legend("topright", c("1","2","3"), pch=1:3, title="Readers", col=cols)

dev.off()
